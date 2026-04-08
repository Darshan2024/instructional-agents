import json
import math
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from agents import LLM


CHAPTER_RUBRIC = {
    "conceptual_accuracy": "The chapter presents domain concepts correctly, without misleading claims, factual errors, or technically invalid explanations.",
    "pedagogical_clarity": "The chapter explains ideas in language suitable for the target learners and makes the instructional intent easy to follow.",
    "logical_flow": "The chapter is organized in a coherent sequence, with sections building on each other naturally.",
    "alignment_with_learning_objectives": "The chapter content, examples, and assessments support the stated learning objectives of the artifact.",
    "quality_of_examples": "The examples are relevant, correct, sufficiently concrete, and helpful for understanding the concept.",
    "instructional_usefulness": "The chapter would be practically useful to an instructor or student as a teaching and learning artifact.",
}


def build_chapter_artifacts(root_dir: Path, read_file_content) -> List[Dict[str, Any]]:
    artifacts: List[Dict[str, Any]] = []

    learning_objectives = ""
    objectives_path = root_dir / "result_instructional_goals.md"
    if objectives_path.exists():
        learning_objectives = read_file_content(str(objectives_path))

    syllabus = ""
    syllabus_path = root_dir / "result_syllabus_design.md"
    if syllabus_path.exists():
        syllabus = read_file_content(str(syllabus_path))

    for chapter_dir in sorted(root_dir.glob("chapter_*")):
        if not chapter_dir.is_dir():
            continue

        section_contents: Dict[str, str] = {}
        for filename in ("slides.tex", "script.md", "assessment.md"):
            filepath = chapter_dir / filename
            if filepath.exists():
                section_contents[filename] = read_file_content(str(filepath))

        if not section_contents:
            continue

        artifact_text_parts = []
        if learning_objectives:
            artifact_text_parts.append("# Course Learning Objectives\n\n" + learning_objectives)
        if syllabus:
            artifact_text_parts.append("# Course Syllabus Context\n\n" + syllabus)
        for filename, content in section_contents.items():
            artifact_text_parts.append(f"# {filename}\n\n{content}")

        artifacts.append(
            {
                "artifact_id": chapter_dir.name,
                "artifact_type": "chapter",
                "content": "\n\n".join(artifact_text_parts),
                "files": sorted(section_contents.keys()),
                "source_dir": str(chapter_dir),
            }
        )

    return artifacts


class GEvalEvaluator:
    """
    Practical G-Eval implementation for instructional artifacts.
    """

    def __init__(self, llm: LLM):
        self.llm = llm
        self.evaluator_name = "g-eval"
        self.chapter_rubric = CHAPTER_RUBRIC
        self.geval_mode = "paper_faithful"
        self.step_generation_mode = "task_rubric_only"
        self.rubric_version = "chapter_v1"
        self._evaluation_step_cache: Dict[Tuple[str, str], List[str]] = {}

    def evaluate_chapter_artifacts(self, artifacts: List[Dict[str, Any]]) -> Dict[str, Any]:
        artifact_results = []
        overall_scores = []

        # G-Eval is more faithful when evaluation steps are fixed before scoring artifacts.
        for criterion_name, criterion_definition in self.chapter_rubric.items():
            self._get_or_create_evaluation_steps(
                artifact_type="chapter",
                criterion_name=criterion_name,
                criterion_definition=criterion_definition,
            )

        for artifact in artifacts:
            result = self.evaluate_single_artifact(artifact)
            artifact_results.append(result)
            overall_scores.append(result["overall_score"])

        return {
            "evaluator_name": self.evaluator_name,
            "artifact_type": "chapter",
            "model_name": self.llm.model_name,
            "geval_mode": self.geval_mode,
            "step_generation_mode": self.step_generation_mode,
            "logprob_scoring_enabled": self.llm.provider == "openai",
            "rubric_version": self.rubric_version,
            "artifacts": artifact_results,
            "summary": {
                "total_artifacts": len(artifact_results),
                "average_overall_score": sum(overall_scores) / len(overall_scores) if overall_scores else 0,
                "max_overall_score": max(overall_scores) if overall_scores else 0,
                "min_overall_score": min(overall_scores) if overall_scores else 0,
            },
        }

    def evaluate_single_artifact(self, artifact: Dict[str, Any]) -> Dict[str, Any]:
        evaluation_steps: Dict[str, List[str]] = {}
        criterion_scores: Dict[str, float] = {}
        criterion_reasons: Dict[str, str] = {}
        weighted_scores: Dict[str, Dict[str, Any]] = {}
        criterion_details: Dict[str, Dict[str, Any]] = {}
        fallback_used = False

        for criterion_name, criterion_definition in self.chapter_rubric.items():
            steps = self._get_or_create_evaluation_steps(
                artifact_type=artifact["artifact_type"],
                criterion_name=criterion_name,
                criterion_definition=criterion_definition,
            )
            evaluation_steps[criterion_name] = steps

            reason, emitted_score = self._run_form_filling_evaluation(
                artifact_id=artifact["artifact_id"],
                artifact_type=artifact["artifact_type"],
                criterion_name=criterion_name,
                criterion_definition=criterion_definition,
                evaluation_steps=steps,
                artifact_content=artifact["content"],
            )

            criterion_reasons[criterion_name] = reason

            weighted_score = self._score_with_logprobs(
                artifact_type=artifact["artifact_type"],
                criterion_name=criterion_name,
                criterion_definition=criterion_definition,
                evaluation_steps=steps,
                artifact_content=artifact["content"],
                reason=reason,
            )

            expected_score = None
            used_fallback = False
            if weighted_score is None:
                fallback_used = True
                used_fallback = True
                criterion_scores[criterion_name] = emitted_score
            else:
                expected_score = weighted_score["expected_score"]
                criterion_scores[criterion_name] = expected_score
                weighted_scores[criterion_name] = weighted_score

            criterion_details[criterion_name] = {
                "reason": reason,
                "emitted_score": emitted_score,
                "expected_score": expected_score,
                "used_fallback": used_fallback,
                "evaluation_steps": steps,
                "observed_score_tokens": weighted_score.get("observed_score_tokens") if weighted_score else [],
                "all_score_tokens_present": weighted_score.get("all_score_tokens_present") if weighted_score else False,
            }

        overall_score = sum(criterion_scores.values()) / len(criterion_scores) if criterion_scores else 0

        return {
            "artifact_id": artifact["artifact_id"],
            "model_name": self.llm.model_name,
            "evaluator_name": self.evaluator_name,
            "evaluation_steps": evaluation_steps,
            "scores": criterion_scores,
            "reasons": criterion_reasons,
            "weighted_scores": weighted_scores if weighted_scores else None,
            "criterion_details": criterion_details,
            "overall_score": overall_score,
            "fallback_scoring_used": fallback_used,
            "files": artifact.get("files", []),
        }

    def _get_or_create_evaluation_steps(
        self,
        *,
        artifact_type: str,
        criterion_name: str,
        criterion_definition: str,
    ) -> List[str]:
        cache_key = (artifact_type, criterion_name)
        if cache_key not in self._evaluation_step_cache:
            self._evaluation_step_cache[cache_key] = self._generate_evaluation_steps(
                artifact_type=artifact_type,
                criterion_name=criterion_name,
                criterion_definition=criterion_definition,
            )
        return self._evaluation_step_cache[cache_key]

    def _generate_evaluation_steps(
        self,
        *,
        artifact_type: str,
        criterion_name: str,
        criterion_definition: str,
    ) -> List[str]:
        prompt = f"""
Task Introduction:
You are designing an evaluation procedure for an instructional artifact using the G-Eval method.
Artifact type: {artifact_type}
Criterion: {criterion_name}
Criterion definition: {criterion_definition}

Instruction:
Generate 3 to 5 concrete evaluation steps that a careful evaluator should follow before assigning a score from 1 to 5.
The steps must be specific to this criterion and this artifact type.
The steps must rely only on evidence available inside the artifact during runtime scoring.
Do not include any step that requires learner feedback, pilot users, peer review, expert consultation,
surveys, classroom observation, or external references not present in the artifact itself.

Return JSON only in the following format:
{{
  "evaluation_steps": ["step 1", "step 2", "step 3"]
}}
"""
        response, _, _ = self.llm.generate_response(
            [
                {"role": "system", "content": "You are a meticulous evaluation planner. Return valid JSON only."},
                {"role": "user", "content": prompt},
            ],
            stream=False,
        )
        parsed = self._parse_json_object(response)
        steps = parsed.get("evaluation_steps", [])
        if isinstance(steps, list):
            normalized_steps = [str(step).strip() for step in steps if str(step).strip()]
            if normalized_steps:
                return normalized_steps

        return self._default_evaluation_steps(criterion_name, criterion_definition)

    def _default_evaluation_steps(self, criterion_name: str, criterion_definition: str) -> List[str]:
        return [
            f"Inspect the artifact strictly for {criterion_name}.",
            f"Compare observed evidence against this criterion definition: {criterion_definition}",
            "Assign a score from 1 to 5 using only evidence from the artifact.",
        ]
    def _run_form_filling_evaluation(
        self,
        *,
        artifact_id: str,
        artifact_type: str,
        criterion_name: str,
        criterion_definition: str,
        evaluation_steps: List[str],
        artifact_content: str,
    ) -> Tuple[str, float]:
        steps_text = "\n".join([f"{idx + 1}. {step}" for idx, step in enumerate(evaluation_steps)])
        prompt = f"""
Task Introduction:
You are evaluating an instructional artifact using G-Eval.
Artifact ID: {artifact_id}
Artifact type: {artifact_type}

Evaluation Criterion:
- Name: {criterion_name}
- Definition: {criterion_definition}

Evaluation Steps:
{steps_text}

Form-Filling Instructions:
Fill in the form below based only on the artifact content.
Return JSON only.

{{
  "criterion": "{criterion_name}",
  "reason": "2-4 sentences grounded in evidence from the artifact.",
  "score": 1
}}

Scoring scale:
1 = poor
2 = weak
3 = adequate
4 = strong
5 = excellent

Artifact:
{artifact_content}
"""
        response, _, _ = self.llm.generate_response(
            [
                {"role": "system", "content": "You are a strict instructional artifact evaluator. Return valid JSON only."},
                {"role": "user", "content": prompt},
            ],
            stream=False,
        )
        parsed = self._parse_json_object(response)
        reason = str(parsed.get("reason", "")).strip()
        score = self._coerce_score(parsed.get("score"))
        if not reason:
            reason = "Fallback reason: evaluator response did not contain a valid reason."
        return reason, score

    def _score_with_logprobs(
        self,
        *,
        artifact_type: str,
        criterion_name: str,
        criterion_definition: str,
        evaluation_steps: List[str],
        artifact_content: str,
        reason: str,
    ) -> Optional[Dict[str, Any]]:
        if self.llm.provider != "openai":
            return None

        steps_text = "\n".join([f"{idx + 1}. {step}" for idx, step in enumerate(evaluation_steps)])
        prompt = f"""
You are performing the final score selection step of G-Eval.

Artifact type: {artifact_type}
Criterion: {criterion_name}
Criterion definition: {criterion_definition}

Evaluation steps:
{steps_text}

Evaluation notes:
{reason}

Based on the artifact and the evaluation notes, output exactly one token: 1, 2, 3, 4, or 5.

Artifact:
{artifact_content}
"""
        try:
            metadata = self.llm.generate_response_with_metadata(
                [
                    {
                        "role": "system",
                        "content": "You are a strict evaluator. Output exactly one score token: 1, 2, 3, 4, or 5.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0,
                max_tokens=1,
                logprobs=True,
                top_logprobs=5,
            )
        except Exception:
            return None

        content_logprobs = metadata.get("content_logprobs") or []
        if not content_logprobs:
            return None

        first_token = content_logprobs[0]
        token_probs: Dict[str, float] = {}

        candidates = list(first_token.get("top_logprobs", []))
        candidates.append({"token": first_token.get("token", ""), "logprob": first_token.get("logprob", float("-inf"))})

        observed_score_tokens = []
        for candidate in candidates:
            normalized = self._normalize_score_token(candidate.get("token", ""))
            if normalized in {"1", "2", "3", "4", "5"}:
                observed_score_tokens.append(normalized)
                token_probs[normalized] = math.exp(candidate["logprob"])

        if not token_probs:
            return None

        total = sum(token_probs.values())
        if total <= 0:
            return None

        normalized_probs = {token: prob / total for token, prob in token_probs.items()}
        expected_score = sum(int(token) * prob for token, prob in normalized_probs.items())

        return {
            "expected_score": expected_score,
            "emitted_score": self._coerce_score(metadata.get("response", "").strip()),
            "used_fallback": False,
            "token_probabilities": normalized_probs,
            "observed_score_tokens": sorted(set(observed_score_tokens)),
            "all_score_tokens_present": all(score_token in normalized_probs for score_token in {"1", "2", "3", "4", "5"}),
            "raw_response": metadata.get("response", "").strip(),
        }

    def _parse_json_object(self, response: str) -> Dict[str, Any]:
        if not response:
            return {}

        response = response.strip()
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            pass

        fenced_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", response, re.DOTALL)
        if fenced_match:
            try:
                return json.loads(fenced_match.group(1))
            except json.JSONDecodeError:
                pass

        brace_match = re.search(r"(\{.*\})", response, re.DOTALL)
        if brace_match:
            try:
                return json.loads(brace_match.group(1))
            except json.JSONDecodeError:
                return {}

        return {}

    def _coerce_score(self, raw_score: Any) -> float:
        try:
            value = float(raw_score)
        except (TypeError, ValueError):
            return 3.0

        rounded = round(value)
        if rounded < 1:
            return 1.0
        if rounded > 5:
            return 5.0
        return float(rounded)

    def _normalize_score_token(self, token: str) -> str:
        return token.strip().strip('"').strip("'").strip(".")
