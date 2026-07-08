# INSTRUCTIONAL AGENTS: LLM Agents on Automated Course Material Generation for Teaching Faculties


![visitors](https://visitor-badge.laobi.icu/badge?page_id=wingsweihua.instructional_agents&style=flat)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fhyan-yao.github.io%2Finstructional_agents_homepage%2F&up_message=Instructional%20Agents&style=flat)](https://hyan-yao.github.io/instructional_agents_homepage/)
![GitHub Repo stars](https://img.shields.io/github/stars/Hyan-Yao/instructional_agents?style=flat&color=red)



An AI-powered instructional design system based on the ADDIE model for automated course creation and evaluation.

---

## 🎯 Background & Motivation

This project began as an evaluation question, not a build-a-tool project.

Prof. Kurt created **Mnemo**, a broader instructional-agent ecosystem at Indiana University. **Clio**, one of the agents within Mnemo, was purpose-built as an AI lecture coach for the Software Engineering course (P465/P565), tightly coupled to that course's classroom logistics (GitHub PR workflows, Canvas rubrics, team roles). The core question driving this independent study was simple: **how good is Clio?**

Answering that required a reliable way to measure instructional quality. Traditional NLG metrics such as BLEU, ROUGE, and METEOR measure surface-level lexical overlap and cannot capture conceptual correctness, pedagogical clarity, or reasoning quality, so they are unsuitable for judging instructional artifacts like slides, scripts, and assessments. That gap is what motivated everything else in this repo.

### G-Eval: rubric-based LLM-as-judge scoring

The first evaluator built was based on **G-Eval** (Liu et al., 2023, [arXiv:2303.16634](https://arxiv.org/abs/2303.16634)), which uses an LLM itself as a structured evaluator instead of a fixed-vocabulary metric. The implementation (`evaluators/`) follows G-Eval's three-stage structure:

1. **Evaluation-step generation**: the evaluator LLM is prompted to produce a criterion-specific evaluation procedure (e.g. for conceptual accuracy, pedagogical clarity, logical flow, alignment with learning objectives, quality of examples, instructional usefulness).
2. **Form-filling evaluation**: the LLM applies those steps to the artifact, producing a structured `{THOUGHT, SCORE}` JSON with chain-of-thought reasoning before each numeric score.
3. **Probability-weighted scoring**: rather than trusting the emitted score token directly, the evaluator requests token log-probabilities for each possible rating (1 through 5) and computes an expected value:

   ```
   expected_score = Σ score × P(score)
   ```

   This reduces the randomness of a single sampled token and is the detail from the original G-Eval paper that most differentiates it from naive "ask the LLM to grade it 1-5" prompting. If logprobs are unavailable, the evaluator falls back to the emitted score.

Each chapter artifact (`slides.tex`, `script.md`, `assessment.md`) is scored per-criterion and per-file, then aggregated. Scores are explicitly *not* a proxy for student learning outcomes; they represent **instructor revision effort** (5 = ready to use with minimal edits, 3 = usable but needs moderate revision, 1 = requires substantial rework).

### The leniency problem

Initial G-Eval runs against Clio, Gemini-generated artifacts, and the default pipeline's output all scored within a narrow, high band (**Clio 4.91, Gemini 4.85, default 4.82**, all out of 5), with almost no separation between systems of presumably different quality. This lack of discrimination was flagged directly by Prof. Kurt: an evaluator that assigns near-ceiling scores to everything is not actually measuring anything.

### Controlled degradation experiments

To determine whether the evaluator was truly insensitive to quality, or simply hadn't yet seen a low-quality artifact, two controlled experiments were built and are included in `exp/` and `eval/`:

- **`weak_openai`**: the same chapter-generation pipeline re-run with a deliberately weaker model (`gpt-4.1-nano`) instead of the primary model, producing 4 chapters. Average overall score dropped to **4.67** (range 4.38-4.93) versus Clio's **4.89**, a real but small gap.
- **`manual_weak`**: the strongest baseline (Clio's first 7 chapters) copied verbatim, then hand-edited to insert specific, verifiable factual errors while preserving structure and formatting exactly. Chapters 1-2 were left unchanged as controls, chapters 3-5 received moderate conceptual errors, and chapters 6-7 received severe ones. Examples of inserted claims: *"developers should avoid branches and push directly to main," "if tests pass, no bugs remain," "inheritance is almost always better than composition."* Average overall score across the 7 chapters was **4.51**.

The `manual_weak` results exposed the key finding: for chapter 6 (severely degraded), `conceptual_accuracy` collapsed to **1.34/5**, correctly detecting the inserted errors, but `logical_flow` stayed at **4.85** and `pedagogical_clarity` at **4.43**, so the blended **overall score only fell to 3.93**. Chapter 7 showed the same pattern (`conceptual_accuracy` 1.83, overall 4.08). This demonstrates **structural bias**: G-Eval's per-criterion averaging lets well-formatted, fluently written, well-organized content mask serious factual errors in the overall score, because only one of six criteria actually detects the problem.

### Pairwise comparison as a cross-check

To reduce reliance on absolute rubric scoring alone, a second evaluator (`evaluate_pairwise.py`) implements an **MT-Bench-style** ([Zheng et al., 2023](https://arxiv.org/abs/2306.05685)) pairwise judge. For each pair of artifacts, an LLM judge picks a winner on clarity, instructional alignment, accuracy/depth, and pedagogical effectiveness. To control for position bias (judges tending to favor whichever response is shown first), every comparison runs bidirectionally, once as `[A vs B]` and once as `[B vs A]`, and a verdict is only accepted if both directions agree; otherwise the result is recorded as a tie. `itertools.combinations` generates the full round-robin matchup across however many systems are being compared, so the harness scales to N models without additional code. A 3-model round-robin run (Clio, `pyfunds_gemini`, `test`) executed 204 bidirectional API calls (some exceeding 25k tokens) and took roughly 45 minutes, producing `pyfunds_gemini: 10W-3L-53T`, `test: 4W-5L-61T`, `Clio: 2W-8L-62T`. The dominant tie rate (53-62 out of ~68 comparisons per system) reflects the same underlying issue as the G-Eval leniency problem: most instructional artifacts are similar enough on the criteria being judged that the LLM judge cannot reliably discriminate them.

### From Clio to the domain-agnostic Chapter Agent

To contextualize Clio's scores against other systems, including this repo's own multi-agent ADDIE pipeline, Clio had to be made comparable. Clio itself is deeply coupled to P465-specific logistics (GitHub PR workflows, Canvas rubrics, team role assignments), so it was rebuilt as a domain-agnostic **Chapter Agent**: a single-agent system retaining Clio's pedagogical principles (an eleven-section output structure including Learning Objectives mapped to Bloom's Taxonomy, an I-WE-YOU core-content scaffold, and separated Instructor Notes) while adopting the same **ADDIE** framework (Analysis, Design, Development, Implementation, Evaluation) that structures this repo's `ADDIE.py` pipeline. That shared structural backbone is what makes a like-for-like comparison between Clio's output and this repo's generated chapters possible.

### What this repo actually is

The codebase here, the ADDIE-based multi-agent generation pipeline (`ADDIE.py`, `agents.py`, `slides.py`) and its G-Eval / pairwise evaluation harness (`evaluate.py`, `evaluators/`), is the outcome of that investigation: a system for generating instructional course material, and, just as importantly, an experimental harness for testing whether LLM-as-judge evaluation of that material can actually be trusted. The findings so far (score inflation, structural bias favoring form over correctness, high pairwise tie rates) point toward a hybrid evaluation approach as future work: combining rubric-based and pairwise methods, separating conceptual-accuracy scoring from structural/stylistic scoring, and eventually validating against human judgment.

```
@misc{yao2025instructionalagentsllmagents,
  title={Instructional Agents: LLM Agents on Automated Course Material Generation for Teaching Faculties},
  author={Yao, Huaiyuan and Xu, Wanpeng and Turnau, Justin and Kellam, Nadia and Wei, Hua},
  year={2025},
  eprint={2508.19611},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  url={https://arxiv.org/abs/2508.19611},
}
```

---

## 🔧 Quick Start

### 1. Setup Configuration

Create or edit `config.json`:
```json
{
  "OPENAI_API_KEY": "your_openai_api_key_here"
}
````

### 2. Install Dependencies

```bash
pip install openai pandas pathlib pdflatex
```

---

## 🚀 Usage Examples

### 🔹 Basic Workflow Execution

**Entry Point**: `run.py` – Main workflow entry point

```bash
# Simple course generation
python run.py "Introduction to Machine Learning"

# With specific model
python run.py "Data Structures" --model gpt-4o-mini

# With experiment name
python run.py "Web Development" --exp web_dev_v1

# Interactive copilot mode
python run.py "Database Systems" --copilot
```

---

### 🔹 Use Catalog Mode

You can now specify a catalog name using `--catalog [name]`. If only `--catalog` is given without a name, a default value will be used (`default_catalog.json`).

```bash
# Use default catalog
python run.py "Software Engineering" --catalog

# Use a specific catalog file (e.g., catalog/ai_catalog.json)
python run.py "AI Fundamentals" --catalog ai_catalog

# Combine catalog mode and copilot
python run.py "Educational Psychology" --copilot --catalog edu_psy
```

---

### 🔹 Command Line Arguments

```bash
python run.py <course_name> [OPTIONS]

Required:
  course_name              Name of the course to design

Options:
  --copilot                Enable interactive copilot mode
  --catalog [name]         Use structured data from catalog/ directory
                           (optional: specify catalog name without '.json')
  --model MODEL            OpenAI model to use (default: gpt-4o-mini)
  --exp EXP_NAME           Experiment name for saving output (default: exp1)
```

---

## ✅ Automatic Evaluation

**Entry Point**: `evaluate.py` – Automatic assessment and scoring

```bash
# Evaluate a specific experiment
python evaluate.py --exp web_dev_v1
```

---

## 🧵 Background Execution with Logging

### Using `nohup` for Long-Running Tasks

```bash
# Run in background with log file
nohup python run.py "Advanced Machine Learning" --exp ml_advanced > logs/ml_course.log 2>&1 &

# Monitor progress
tail -f logs/ml_course.log
```

---

## 📚 Example Workflows

### 🔸 Complete Course Design

```bash
# Step 1: Generate course using catalog
python run.py "Python Fundamentals" \
  --catalog python_catalog \
  --model gpt-4o \
  --exp py_course_v1

# Step 2: Evaluate results
python evaluate.py --exp py_course_v1
```

### 🔸 Interactive Development (Copilot)

```bash
python run.py "Advanced Algorithms" --copilot --exp algo_course_v2

# You'll be prompted for feedback after each phase:
# - Analysis → feedback
# - Design → feedback
# - Development → feedback
```

---

## 📁 View Results

```bash
# List output files
tree exp/your_experiment_name/

# View evaluation summary
cat eval/your_experiment_name/evaluation_results/evaluation_summary.md

# View detailed validation reports
ls eval/your_experiment_name/validation_reports/
```

---

## 📌 Notes

* If you specify `--catalog` without a value, the system defaults to `default_catalog.json` inside the `catalog/` folder.
* If you provide a name (e.g., `--catalog mydata`), the system expects `catalog/mydata.json`.

---

## 📜 License

MIT License
