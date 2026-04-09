# Assessment: Slides Generation - Chapter 3: Control Flow: Conditional Logic

## Section 1: Chapter 3: Control Flow: Conditional Logic

### Learning Objectives
- Understand that this chapter will cover how to make programs 'smart' by enabling them to make decisions.
- Define 'control flow' as the order of execution in a program.
- Recognize the real-world analogy of decision-making in programming.
- Articulate the purpose of conditional logic in creating dynamic and responsive applications.

### Assessment Questions

**Question 1:** What is the primary purpose of conditional logic in programming?

  A) To allow a program to make decisions and execute different code based on certain conditions.
  B) To repeat a block of code multiple times.
  C) To store data in variables for later use.
  D) To organize code into reusable functions.

**Correct Answer:** A
**Explanation:** Conditional logic (using statements like 'if') is fundamental for creating programs that can respond dynamically to different inputs or states by choosing a specific path of execution.

**Question 2:** Which of the following best describes 'control flow'?

  A) The speed at which a program executes.
  B) The way data is stored in memory.
  C) The order in which the program's statements are executed.
  D) The process of debugging and fixing errors.

**Correct Answer:** C
**Explanation:** Control flow refers to the sequence in which instructions in a program are executed. Conditional statements are a primary tool for directing or altering this flow from a simple top-to-bottom sequence.

**Question 3:** Which real-world scenario is the best analogy for a conditional statement in a program?

  A) Following a recipe step-by-step to bake a cake.
  B) Making a list of groceries to buy.
  C) Choosing to wear a coat if the temperature is below 50°F (10°C).
  D) Repeating a set of exercises 10 times.

**Correct Answer:** C
**Explanation:** This scenario perfectly illustrates a condition (temperature is below 50°F) that leads to a specific action (wear a coat), which is the core concept of an 'if' statement in programming.

### Activities
- Think-Pair-Share: Think of a real-life decision you make every day (e.g., what to wear). What conditions influence your choice? (e.g., 'If it is raining, I will take a jacket'). Share your conditions and resulting actions with a partner.
- Flowchart Sketch: In small groups, sketch a simple flowchart for a common task like making coffee or deciding what to have for lunch. Use diamond shapes for decisions (conditions) and rectangles for actions.

### Discussion Questions
- Why is it essential for programs to be able to make decisions? What would a program without any conditional logic be like?
- Can you think of a feature in your favorite app or video game that clearly uses conditional logic? Describe the condition and the resulting action.
- What happens when a program encounters a condition it wasn't designed to handle? How might we prevent such situations?

---

## Section 2: What is Control Flow?

### Learning Objectives
- Define 'control flow' as the order of statement execution in a program.
- Differentiate between sequential and conditional control flow.
- Explain that sequential flow is the default, top-to-bottom execution order.
- Recognize that conditional flow allows a program to make choices and follow different paths.
- Connect the concept of conditional logic (evaluating to True/False) to the creation of conditional flow.

### Assessment Questions

**Question 1:** What is the default type of control flow in a Python script?

  A) Conditional Flow
  B) Sequential Flow
  C) Looping Flow
  D) Random Flow

**Correct Answer:** B
**Explanation:** By default, Python executes code line-by-line from top to bottom without deviation. This is known as sequential flow. Conditional flow is a deliberate change from this default behavior.

**Question 2:** Which of the following best defines 'control flow' in programming?

  A) The speed at which a program runs.
  B) The way a program stores variables in memory.
  C) The order in which a program's statements are executed.
  D) The process of finding and fixing bugs in the code.

**Correct Answer:** C
**Explanation:** Control flow specifically refers to the path or sequence the computer follows when executing the statements in a program. It can be a straight line (sequential) or have branches (conditional).

**Question 3:** The 'fork in the road' analogy is used to describe which programming concept?

  A) Sequential Flow, where each step follows the last.
  B) Conditional Flow, where a decision must be made to determine the next step.
  C) Variable assignment, where a value is stored for later use.
  D) Function calls, where a reusable block of code is executed.

**Correct Answer:** B
**Explanation:** Conditional flow is like a 'fork in the road' because the program evaluates a condition and chooses one path of execution over another, altering the standard top-to-bottom flow.

**Question 4:** What fundamental concept allows a program to implement conditional flow?

  A) Printing output to the console.
  B) Assigning values to variables.
  C) Evaluating a condition to be True or False.
  D) Writing comments in the code.

**Correct Answer:** C
**Explanation:** Conditional flow is built on conditional logic. A program asks a 'question' (evaluates a condition) which results in a True or False answer, and that answer dictates which block of code will run next.

### Activities
- On a piece of paper or a whiteboard, draw a simple flowchart for a sequential process (e.g., making a sandwich). Then, draw a flowchart for a conditional process (e.g., deciding whether to wear a jacket based on the outside temperature). Label the 'decision point' in your conditional flowchart.
- Write a short, non-code 'recipe' for a daily task. First, write it purely sequentially. Then, revise it to include at least one conditional step (e.g., 'IF the milk is expired, throw it out. OTHERWISE, pour it into the cereal.').

### Discussion Questions
- Besides a recipe, what is another real-life example of a sequential process? What would happen if you performed the steps out of order?
- Think about a simple video game. What is one example of a 'conditional flow' decision the game has to make? (e.g., IF player health is zero...)
- Why is sequential flow, on its own, not sufficient for creating interactive and 'smart' applications?
- The slide mentions a program's flow changes based on a `True` or `False` answer. What are some simple `True`/`False` questions a program could ask? (e.g., Is the user's password correct? Is the number greater than 10?)

---

## Section 3: The Foundation: Boolean Expressions

### Learning Objectives
- Define what a Boolean expression is and its purpose in programming.
- Identify the two Python keywords, `True` and `False`, that represent Boolean values, including the correct capitalization.
- Explain how Boolean expressions serve as the conditions that guide control flow statements.
- Write and evaluate simple Boolean expressions in Python by predicting their `True` or `False` result.

### Assessment Questions

**Question 1:** A Boolean expression in Python will always evaluate to one of which two values?

  A) Yes or No
  B) 1 or 0
  C) True or False
  D) On or Off

**Correct Answer:** C
**Explanation:** Boolean logic is based on two truth values: `True` and `False`. These are special keywords in Python and are the foundation of all conditional checks.

**Question 2:** Which of the following is the correct syntax for a Boolean value in Python?

  A) true
  B) 'True'
  C) TRUE
  D) True

**Correct Answer:** D
**Explanation:** Python is case-sensitive. The Boolean values must be written with the first letter capitalized: `True` and `False`. The other options are either lowercase, a string, or all-caps, which are not recognized as Boolean keywords.

**Question 3:** What is the primary role of a Boolean expression in a control flow statement (like an `if` statement)?

  A) To store a number
  B) To print text to the screen
  C) To act as the condition that determines which path the program takes
  D) To define a new function

**Correct Answer:** C
**Explanation:** Boolean expressions are the 'decision-makers'. Their `True` or `False` result is used by control flow statements to decide whether to execute a specific block of code, creating a 'fork in the road'.

**Question 4:** Consider the code: `items_in_cart = 0; is_cart_empty = (items_in_cart == 0);`. What value will the variable `is_cart_empty` hold?

  A) 0
  B) True
  C) False
  D) An error will occur

**Correct Answer:** B
**Explanation:** The Boolean expression `(items_in_cart == 0)` asks, 'Is the value of `items_in_cart` equal to 0?'. Since `items_in_cart` is 0, the expression evaluates to `True`, and this value is assigned to the `is_cart_empty` variable.

### Activities
- {'type': 'code_prediction', 'description': 'Predict the output of the following Python code before running it. What will be the final value printed for each variable?', 'code': "player_level = 12\nhas_key = False\n\nis_high_level = (player_level > 10)\ncan_open_door = (has_key == True)\nis_beginner = (player_level <= 5)\n\nprint('Is high level?', is_high_level)\nprint('Can open door?', can_open_door)\nprint('Is beginner?', is_beginner)"}
- {'type': 'conceptual', 'description': "Translate the following real-world questions into Python Boolean expressions and assign them to a variable. Example: 'Is it raining?' becomes `is_raining = True` (or `False` depending on the weather!).\n1. Is the current month December?\n2. Is your age greater than 21?\n3. Is the light switch on?"}

### Discussion Questions
- In the code example, we stored the result of `(score >= 60)` in a variable called `is_passing`. What is the advantage of storing the `True`/`False` value in a variable instead of using the expression directly in an `if` statement?
- Can you think of a real-world example from a video game or a website (like an e-commerce site) where a Boolean expression would be used to make a decision? What is the 'question' and what happens if the answer is `True` vs. `False`?
- Why is it important that a Boolean expression can *only* result in `True` or `False`? What would happen if it could result in a third value, like 'Maybe'?

---

## Section 4: Comparison Operators

### Learning Objectives
- Identify the six comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) and their meanings.
- Differentiate between the assignment operator (`=`) and the equality comparison operator (`==`).
- Evaluate simple Boolean expressions that use comparison operators to determine if they result in `True` or `False`.

### Assessment Questions

**Question 1:** Which Python code snippet correctly checks if the variable `score` has a value of 100?

  A) `if score = 100:`
  B) `if score == 100:`
  C) `if score := 100:`
  D) `if score != 100:`

**Correct Answer:** B
**Explanation:** The double equals sign `==` is the comparison operator for equality. A single equals sign `=` is the assignment operator, used for assigning a value to a variable, which is not what you want inside a condition for checking equality.

**Question 2:** Given the code `age = 18`, which of the following expressions evaluates to `True`?

  A) `age > 18`
  B) `age != 18`
  C) `age >= 18`
  D) `age < 18`

**Correct Answer:** C
**Explanation:** The operator `>=` checks for 'greater than OR equal to'. Since `age` is exactly 18, the 'equal to' part of the condition is met, making the expression `True`. The expression `age > 18` would be `False`.

**Question 3:** What is the Boolean result of the expression `15 <= 10`?

  A) `True`
  B) `False`
  C) `SyntaxError`
  D) `None`

**Correct Answer:** B
**Explanation:** The expression `15 <= 10` asks, 'Is 15 less than or equal to 10?'. Since 15 is not less than 10 and is not equal to 10, the statement is `False`.

**Question 4:** Which operator is used to check if two values are NOT the same?

  A) `==`
  B) `><`
  C) `!=`
  D) `~=`

**Correct Answer:** C
**Explanation:** The `!=` operator, read as 'not equal to', evaluates to `True` if the two values being compared are different, and `False` otherwise.

### Activities
- Given `x = 15` and `y = 20`, manually evaluate the following expressions to `True` or `False`: `x > y`, `x <= 15`, `y != 20`, `x == y`.
- Find the bug: The following code is supposed to print 'Access Granted' if a user is 18, but it produces an error. Identify and fix the mistake. `user_age = 18 
if user_age = 18:
    print('Access Granted')`
- Fill in the blank with the correct comparison operator to make each expression `True`. Given `temperature = 75`: `temperature ___ 80` and `temperature ___ 75`.

### Discussion Questions
- Why is the distinction between `=` (assignment) and `==` (comparison) one of the most common sources of bugs for new programmers? What could happen in a larger program if you mixed them up?
- Can you think of a real-world scenario where you would need to use `>=` (greater than or equal to) instead of just `>` (greater than)? For example, in a game or an online store.
- We've seen these operators work with numbers. How do you think Python would handle an expression like `'apple' < 'banana'`? What might it be comparing?

---

## Section 5: The `if` Statement: The Basic Decision

### Learning Objectives
- Identify the key components of a basic `if` statement: the `if` keyword, the condition, the colon, and the indented code block.
- Explain that the code inside an `if` block only runs if the condition evaluates to `True`.
- Predict the output of a simple program containing an `if` statement for both `True` and `False` conditions.
- Write a syntactically correct `if` statement to solve a basic conditional problem.

### Assessment Questions

**Question 1:** In a Python `if` statement, what is required for the indented block of code to be executed?

  A) The condition must evaluate to `False`.
  B) The condition must be a number greater than 0.
  C) The condition must evaluate to `True`.
  D) The code block is always executed, regardless of the condition.

**Correct Answer:** C
**Explanation:** The fundamental purpose of an `if` statement is to execute a block of code conditionally. This execution only happens when the specified condition evaluates to `True`.

**Question 2:** Which of the following syntactical elements is used in Python to define the body (the code block) of an `if` statement?

  A) Curly braces `{}`
  B) Parentheses `()`
  C) Indentation (e.g., 4 spaces)
  D) Semicolons `;`

**Correct Answer:** C
**Explanation:** Unlike many other languages that use braces, Python uses indentation to group statements. All indented lines after the `if condition:` line are part of the `if` statement's body.

**Question 3:** What happens if the condition in an `if` statement evaluates to `False`?

  A) The program stops and reports an error.
  B) The indented code block is skipped, and execution continues with the next line after the block.
  C) The program asks the user for a new value to make the condition `True`.
  D) The indented code block is executed anyway.

**Correct Answer:** B
**Explanation:** If the condition is `False`, the control flow bypasses the entire indented block associated with the `if` statement and resumes at the first unindented line that follows.

**Question 4:** What will be the output of the following Python code?
```python
score = 85
if score < 80:
    print("Good job!")
print("Processing complete.")
```

  A) Good job!
Processing complete.
  B) Good job!
  C) Processing complete.
  D) The code will produce no output.

**Correct Answer:** C
**Explanation:** The condition `score < 80` evaluates to `False` because 85 is not less than 80. Therefore, the indented line `print("Good job!")` is skipped. The final `print` statement is not indented, so it is outside the `if` block and will always be executed.

### Activities
- {'type': 'coding_exercise', 'title': 'Check Class Size', 'description': "Write a Python `if` statement that checks if a variable `num_students` (pre-defined as 32) is greater than 25. If it is, print the message 'The class is large.'."}
- {'type': 'coding_exercise', 'title': 'Voting Age Check', 'description': "Create a variable `age` and set it to 19. Write an `if` statement that checks if `age` is greater than or equal to 18. If the condition is `True`, print 'You are eligible to vote.'."}
- {'type': 'bug_fix', 'title': 'Fix the Syntax', 'description': 'The following code has two syntax errors. Find and fix them so the code runs correctly.\n```python\n# Buggy Code\naccess_level = 5\nif access_level > 3\nprint("Access Granted.")\n```', 'solution': 'The code is missing a colon `:` after the condition and the `print` statement is not indented.\n```python\n# Corrected Code\naccess_level = 5\nif access_level > 3:\n    print("Access Granted.")\n```'}

### Discussion Questions
- Why do you think Python's designers chose to use indentation to define code blocks instead of symbols like curly braces `{}` which are common in other languages?
- Can you think of a real-world decision you make every day that works like an `if` statement? (e.g., 'If it is raining, I will take an umbrella.')
- What kind of problems might occur if you forget the colon at the end of the `if` line or use inconsistent indentation?

---

## Section 6: The `if-else` Statement: The Two-Way Path

### Learning Objectives
- Understand the syntax and structure of an `if-else` statement.
- Explain that the `else` block provides an alternative execution path when the `if` condition is `False`.
- Trace the flow of execution in an `if-else` block for both `True` and `False` conditions.
- Apply `if-else` statements to solve simple binary (two-outcome) problems.

### Assessment Questions

**Question 1:** Given `password = '12345'`, what is the output of the following code?
```python
if len(password) >= 8:
    print('Strong password')
else:
    print('Weak password')
```

  A) Strong password
  B) Weak password
  C) No output
  D) An error will occur

**Correct Answer:** B
**Explanation:** The length of '12345' is 5. The condition `5 >= 8` evaluates to `False`. Therefore, the program skips the `if` block and executes the code inside the `else` block, printing 'Weak password'.

**Question 2:** In an `if-else` statement, which of the following is guaranteed to happen?

  A) The `if` block will always be executed.
  B) The `else` block will always be executed.
  C) Both the `if` and `else` blocks will be executed.
  D) Exactly one of the two blocks (`if` or `else`) will be executed.

**Correct Answer:** D
**Explanation:** The `if-else` structure is mutually exclusive. If the condition is `True`, the `if` block runs. If the condition is `False`, the `else` block runs. It is guaranteed that one, and only one, of them will execute.

**Question 3:** Consider the code: `number = 10`. What will be printed?
```python
if number % 2 == 0:
    print('Even')
else:
    print('Odd')
```

  A) Even
  B) Odd
  C) Both 'Even' and 'Odd'
  D) Nothing will be printed

**Correct Answer:** A
**Explanation:** The modulo operator `%` gives the remainder of a division. `10 % 2` is `0`, because 10 divides evenly by 2. The condition `0 == 0` is `True`, so the `if` block is executed, printing 'Even'.

**Question 4:** Which statement best describes the purpose of the `else` clause in an `if-else` statement?

  A) It defines a second, independent condition to check.
  B) It provides a block of code to run only if the `if` condition is `False`.
  C) It is an optional comment that explains the `if` statement.
  D) It repeats the code in the `if` block if the condition is `True`.

**Correct Answer:** B
**Explanation:** The `else` clause acts as the alternative path. It does not have its own condition; it simply executes its block of code whenever the preceding `if` condition evaluates to `False`.

### Activities
- Write an `if-else` block that checks if a variable `temperature` is greater than 30. If it is, print 'It is a hot day.'; otherwise, print 'The weather is pleasant.' Test your code with `temperature = 35` and `temperature = 22`.
- Create a program that checks if a variable `score` is 50 or higher. If it is, print 'Result: Pass'. If not, print 'Result: Fail'.
- Write an `if-else` statement to determine if a user's `account_balance` is negative. If `account_balance < 0`, print 'Your account is overdrawn.'; otherwise, print 'Your account balance is positive.'

### Discussion Questions
- When is it more appropriate to use an `if-else` statement instead of just a simple `if` statement? Provide a real-world analogy.
- What happens if you forget to indent the code inside the `if` or `else` block? Why is indentation critical in Python's control structures?
- Can you nest an `if-else` statement inside another `if` block? What would be an example where that might be useful?

---

## Section 7: The `if-elif-else` Chain: Multi-Way Paths

### Learning Objectives
- Understand the purpose and syntax of the `elif` keyword.
- Explain that an `if-elif-else` chain is used to check multiple, mutually exclusive conditions.
- Recognize that only the first true block in the entire chain will be executed.
- Implement multi-way branching logic to solve problems with several possible outcomes.

### Assessment Questions

**Question 1:** In a long `if-elif-else` chain, how many code blocks can be executed at most?

  A) Zero
  B) Exactly one
  C) All blocks whose conditions are true
  D) As many as there are `elif` statements

**Correct Answer:** B
**Explanation:** The `if-elif-else` structure is designed to be mutually exclusive. Python checks each condition in order and executes the *first* one that is `True`, then skips the rest of the chain.

**Question 2:** What will be the output of the following code snippet?
```python
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("D")
```

  A) A
  B) B
  C) B
   C
  D) An error will occur

**Correct Answer:** B
**Explanation:** Python evaluates the conditions sequentially. The first condition `grade >= 90` (85 >= 90) is false. The second condition `grade >= 80` (85 >= 80) is true. The code block for this `elif` is executed, printing 'B'. The rest of the chain is then skipped.

**Question 3:** What is the primary purpose of the final `else` block in an `if-elif-else` chain?

  A) To check one final, specific condition before the chain ends.
  B) To act as a mandatory conclusion to every `if` statement.
  C) To execute a default block of code if all preceding conditions are false.
  D) To report errors if none of the conditions were met.

**Correct Answer:** C
**Explanation:** The `else` block is optional and serves as a 'catch-all'. Its code runs only when every `if` and `elif` condition above it in the chain has evaluated to `False`.

**Question 4:** Consider the following code: `x = 20`. Why is the order of the `elif` statements important for the logic to work as intended for a discount system?

  A) The order does not matter; Python finds the best fit.
  B) If `elif x > 10:` came first, a value like 20 would trigger the smaller discount, and the `elif x > 15:` check would be skipped.
  C) Python requires conditions to be ordered from smallest to largest.
  D) The `else` block would execute incorrectly if the order were changed.

**Correct Answer:** B
**Explanation:** Because the chain executes the *first* true block it finds, conditions must be ordered correctly. For checks involving numerical ranges (like greater than), you typically check for the most specific/highest value first to ensure the correct logic is applied.

### Activities
- Write a Python script that determines a shipping cost based on weight. Ask the user for a package weight and use an `if-elif-else` chain to set the price: Free for weights under 1kg, $5 for weights from 1kg up to and including 5kg, and $10 for weights over 5kg. Print the final cost.
- Create a 'Grade Converter' program. The program should take a numerical score (0-100) as input and print the corresponding letter grade: 'A' for 90-100, 'B' for 80-89, 'C' for 70-79, 'D' for 60-69, and 'F' for below 60. This is a classic use-case for `if-elif-else`.
- Refactor the following nested `if` statements into a single, more readable `if-elif-else` chain:
```python
# Given code to refactor
color = "blue"
if color == "red":
    print("Stop")
else:
    if color == "yellow":
        print("Caution")
    else:
        if color == "green":
            print("Go")
        else:
            print("Invalid color")
```

### Discussion Questions
- When would you choose to use an `if-elif-else` chain over several separate `if` statements? What is the key difference in their behavior?
- Does the order of your `elif` conditions always matter? Provide an example where changing the order would lead to a different, incorrect result.
- The `else` block is optional. Can you think of a real-world scenario where you would want an `if-elif` chain with *no* final `else` block?

---

## Section 8: Example: Grading with `if-elif-else`

### Learning Objectives
- Apply the `if-elif-else` structure to solve a practical programming problem with mutually exclusive outcomes.
- Trace the execution flow of a program with multiple conditions to predict its output accurately.
- Explain the critical importance of condition order in an `if-elif-else` chain and identify potential logic errors from incorrect ordering.
- Understand the implicit logic that makes compound conditions (e.g., `and score < 90`) unnecessary in a well-structured `if-elif-else` chain.

### Assessment Questions

**Question 1:** Using the code from the slide, what is the output if `score = 69`?

  A) Your grade is: B
  B) Your grade is: C
  C) Your grade is: F
  D) The code will produce an error.

**Correct Answer:** C
**Explanation:** Python checks `if score >= 90` (False), `elif score >= 80` (False), and `elif score >= 70` (False). Since all conditions are false, the code in the final `else` block is executed, setting `grade` to 'F'.

**Question 2:** What is the primary reason the conditions are ordered from `score >= 90` down to `score >= 70`?

  A) It is a Python syntax requirement.
  B) To ensure the most specific condition (highest grade) is checked first, preventing a high score from incorrectly matching a lower grade's condition.
  C) It makes the code run faster.
  D) To handle negative scores correctly.

**Correct Answer:** B
**Explanation:** The order is critical. If `score >= 70` were checked first, a score of 95 would incorrectly receive a 'C' because `95 >= 70` is true, and the chain would exit before checking for an 'A'.

**Question 3:** If the code were changed so the first two conditions were `if score >= 70:` and `elif score >= 80:`, what grade would a `score` of 95 receive?

  A) A
  B) B
  C) C
  D) F

**Correct Answer:** C
**Explanation:** With the incorrect order, the first condition `if score >= 70:` would be checked. Since `95 >= 70` is `True`, the `grade` would be set to 'C', and the rest of the chain would be skipped entirely.

**Question 4:** Why is it unnecessary to write the second condition as `elif score >= 80 and score < 90:`?

  A) Using `and` is not allowed in `elif` statements.
  B) Because if the first condition (`score >= 90`) is `False`, it is already guaranteed that the score is less than 90.
  C) The code would be less readable.
  D) Python automatically assumes the upper bound from the previous `if` statement.

**Correct Answer:** B
**Explanation:** The `if-elif` chain's sequential evaluation is key. When the program reaches the `elif score >= 80:` check, it has already determined that `score >= 90` was false. Therefore, the condition `score < 90` is implicitly true at that point.

### Activities
- Modify the grading code to include a 'D' grade for scores from 60 up to 69. The 'F' grade should now only be for scores below 60.
- Add a preliminary `if` statement to the code that first checks if the `score` is valid (i.e., between 0 and 100). If it's not, it should print an 'Invalid score' message and not attempt to assign a grade.
- Write a new Python script using an `if-elif-else` chain to determine a shipping fee. If an order total is over $100, shipping is free. If it's over $50, shipping is $5. If it's over $25, shipping is $10. Otherwise, shipping is $15.

### Discussion Questions
- When would you choose an `if-elif-else` chain over using several separate `if` statements? What is the key difference in their behavior?
- The current code assigns a grade. How could we modify it to also print a motivational message for each grade (e.g., 'Excellent work!' for an 'A')?
- Can you think of another real-world scenario (besides grading or shipping) where an `if-elif-else` chain would be the perfect tool to model the logic?

---

## Section 9: Combining Conditions: Logical Operators

### Learning Objectives
- Define the function of the `and`, `or`, and `not` logical operators.
- Use logical operators to combine multiple Boolean expressions into a single, more complex condition.
- Interpret the outcome of conditional statements that use logical operators.
- Construct complex logical conditions using parentheses to control the order of evaluation.

### Assessment Questions

**Question 1:** Which logical operator requires *both* of its connected conditions to be true for the entire expression to be true?

  A) `or`
  B) `not`
  C) `and`
  D) `is`

**Correct Answer:** C
**Explanation:** The `and` operator evaluates to `True` only if the expression on its left AND the expression on its right are both `True`.

**Question 2:** What is the output of the following code snippet?
```python
is_weekend = False
has_coupon = True
if is_weekend or has_coupon:
    print("You get a discount!")
else:
    print("No discount today.")
```

  A) You get a discount!
  B) No discount today.
  C) The code will produce an error.
  D) Nothing will be printed.

**Correct Answer:** A
**Explanation:** The `or` operator evaluates to `True` if at least one of its conditions is `True`. Since `has_coupon` is `True`, the entire condition `is_weekend or has_coupon` becomes `True`, executing the first block.

**Question 3:** Given `is_logged_in = True`, what is the value of the expression `not is_logged_in`?

  A) `True`
  B) `False`
  C) `None`
  D) `1`

**Correct Answer:** B
**Explanation:** The `not` operator inverts the Boolean value of its operand. Since `is_logged_in` is `True`, `not is_logged_in` evaluates to `False`.

**Question 4:** Consider the condition `age > 12 and (is_student or has_permission)`. Under which scenario will this condition be `False`?

  A) `age` is 15, `is_student` is `True`, `has_permission` is `False`
  B) `age` is 10, `is_student` is `True`, `has_permission` is `True`
  C) `age` is 14, `is_student` is `False`, `has_permission` is `True`
  D) `age` is 20, `is_student` is `False`, `has_permission` is `False`

**Correct Answer:** B
**Explanation:** The condition requires `age > 12` to be `True`. In option B, `age` is 10, so `age > 12` is `False`. Because of the `and` operator, if the first part is `False`, the entire expression becomes `False` regardless of the second part.

### Activities
- Write a single `if` statement that checks if a variable `hour` is outside of working hours (i.e., less than 9 or greater than 17). Use the `or` operator.
- Write a Python script that defines two variables: `password_length = 10` and `has_special_char = True`. Print 'Strong password' only if the `password_length` is greater than 8 AND `has_special_char` is `True`.
- Create a variable `is_premium_user = False`. Write a conditional statement that prints 'Please upgrade to a premium account to access this feature.' only if the user is NOT a premium user. Use the `not` operator.

### Discussion Questions
- Can you think of a real-world scenario (like a video game or a website login) where you would need to combine `and` and `or` in the same `if` statement?
- Why is it often a good idea to use parentheses when mixing `and` and `or` in a single condition, even if it's not strictly necessary due to operator precedence?
- When is it more readable to write `if not user_is_active:` versus `if user_is_active == False:`? Do they achieve the same result?

---

## Section 10: Chapter 3 Summary

### Learning Objectives
- Summarize the roles of `if`, `elif`, and `else` in controlling program flow.
- Recall how Boolean expressions, comparison operators, and logical operators work together to form conditions.
- Analyze a given `if-elif-else` block to predict its output.
- Construct basic conditional statements to solve a problem with multiple outcomes.

### Assessment Questions

**Question 1:** Given the code `score = 85`, what will be the output of the following `if-elif-else` chain?

  A) A
  B) B
  C) C
  D) B and C

**Correct Answer:** B
**Explanation:** The program checks each condition in order. `score >= 90` is false. `score >= 80` is true, so it prints 'B' and immediately exits the entire `if-elif-else` block, ignoring the remaining `elif` and `else` conditions.

**Question 2:** In an `if-elif-else` structure, when is the code inside the `else` block executed?

  A) Always, as it is the default action.
  B) Only when the initial `if` condition is false.
  C) Only when all preceding `if` and `elif` conditions are `False`.
  D) When any of the preceding `elif` conditions are `True`.

**Correct Answer:** C
**Explanation:** The `else` statement acts as a 'catch-all'. Its code block is only executed if every single condition in the `if` and `elif` statements before it evaluates to `False`.

**Question 3:** Which Boolean expression correctly checks if a user is older than 18 AND has permission?

  A) `age > 18 or has_permission`
  B) `age > 18 and has_permission`
  C) `age >= 18 not has_permission`
  D) `if age > 18, if has_permission`

**Correct Answer:** B
**Explanation:** The logical operator `and` is used to ensure that BOTH conditions on its left and right must be `True` for the entire expression to evaluate to `True`.

**Question 4:** What is the primary function of a comparison operator like `==` or `>`?

  A) To assign a new value to a variable.
  B) To execute a block of code.
  C) To create a Boolean expression that evaluates to `True` or `False`.
  D) To combine two different conditions into one.

**Correct Answer:** C
**Explanation:** Comparison operators compare two values and produce a Boolean result (`True` or `False`), which is then used by a conditional statement like `if` to make a decision.

### Activities
- **Code Correction Challenge:** The following code is supposed to check if a number is positive, negative, or zero, but it has a logical error. Fix the code and explain why the original order was incorrect. `num = 0; if num > 0: print('Positive'); elif num == 0: print('Zero'); elif num < 0: print('Negative');` (Hint: The code works but can be improved for clarity and structure).
- **Problem Solving:** Write a Python script that asks for a user's age. The script should then print one of the following based on their age: 'Child' (under 13), 'Teenager' (13-19), or 'Adult' (20 and older).
- **Concept Map:** On paper, draw a diagram that connects the following key terms from the chapter: `if`, `elif`, `else`, `Boolean Expression`, `Comparison Operator`, and `Logical Operator`. Use arrows and brief notes to show their relationships.

### Discussion Questions
- Why is the order of `elif` statements so important? Provide a simple example where changing the order would lead to a different, incorrect result.
- When would you choose to use a series of separate `if` statements instead of a single `if-elif-else` chain? What is the key difference in how they execute?
- Think of a non-programming, real-world scenario that can be described as an `if-elif-else` decision. For example, deciding what to wear based on the weather.

---

