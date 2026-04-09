# Assessment: Slides Generation - Chapter 8: Midterm Review & Exam

## Section 1: Chapter 8: Midterm Review & Exam

### Learning Objectives
- Understand the agenda, structure, and objectives for the midterm review session.
- Recognize the importance of synthesis (connecting concepts) over simple memorization for exam success.
- Identify the four key components of the session: Logistics, Review, Practice, and Q&A.
- Articulate personal learning goals for the review session.

### Assessment Questions

**Question 1:** What is the primary goal of this review session?

  A) To synthesize concepts from the first half of the course in preparation for the midterm.
  B) To introduce new advanced topics for the second half of the course.
  C) To complete the final project for the course.
  D) To learn about the history of programming.

**Correct Answer:** A
**Explanation:** The slide explicitly states, 'Our goal is to synthesize the core programming concepts from the first seven weeks' to prepare you for the midterm exam. The focus is on connecting existing knowledge, not learning new material.

**Question 2:** According to the agenda, what is the main purpose of the 'Integrated Practice Problem'?

  A) To introduce a completely new programming challenge.
  B) To see a complete problem-solving process in action that combines multiple concepts learned so far.
  C) To test individual coding speed under time pressure.
  D) To review each topic from Weeks 1-7 one by one.

**Correct Answer:** B
**Explanation:** The slide content explains that the integrated practice problem is where 'theory meets practice' and will require combining concepts to solve a sample exam-style problem from start to finish.

**Question 3:** What key mindset is emphasized for successfully approaching this review session?

  A) Memorizing the exact syntax of every command.
  B) Focusing on speed above all else.
  C) Understanding how and why different programming concepts connect and work together.
  D) Working in isolation without asking questions.

**Correct Answer:** C
**Explanation:** The slide explicitly states, 'Key Mindset for Today: Think synthesis, not just memorization. Focus on how and why concepts work together.'

**Question 4:** Which of the following is NOT a planned component of the midterm review session's agenda?

  A) An open Q&A session for clarifying doubts.
  B) A detailed lecture on a new, advanced data structure.
  C) A review of exam logistics and strategy.
  D) A comprehensive recap of topics from the first seven weeks.

**Correct Answer:** B
**Explanation:** The agenda focuses on reviewing and synthesizing existing material from Weeks 1-7. Introducing a new, advanced topic would be contrary to the purpose of a review session.

### Activities
- Conduct a quick poll: 'Which topic from the first seven weeks (e.g., variables, loops, functions, lists) are you most nervous about?' Use the results to guide the emphasis during the review.
- Think-Pair-Share: Ask students to take one minute to think about a specific concept they hope to understand better by the end of the session. Then, have them share this with a partner for another minute. This helps set personal learning goals.
- Goal Setting in Chat: Ask students to write one sentence in the chat about what a 'successful' review session would look like for them personally. This helps tailor the Q&A and review focus.

### Discussion Questions
- Looking at the agenda, which of the four parts are you most looking forward to, and why?
- Why is 'synthesis' more important than 'memorization' when it comes to solving complex programming problems you might see on an exam?
- Can you think of an example from the first seven weeks where two different topics had to be used together to solve a problem?

---

## Section 2: Exam Logistics & Strategy

### Learning Objectives
- Identify the key logistical details of the midterm exam, including its format, duration, and platform.
- List the major programming topics that will be assessed.
- Articulate and apply a multi-step strategy for managing time and maximizing performance on a timed coding exam.
- Distinguish between permitted (e.g., course notes) and prohibited (e.g., Stack Overflow) resources during the exam.

### Assessment Questions

**Question 1:** According to the recommended strategy, what is the very first thing you should do when the exam begins?

  A) Immediately start coding the first problem.
  B) Take 2-3 minutes to read through all the questions.
  C) Review your notes on the most difficult topic.
  D) Write placeholder functions for every question.

**Correct Answer:** B
**Explanation:** The 'Skim and Plan' phase is the first step. Reading all questions helps you create a mental map, identify easy wins, and budget your time effectively before you start coding.

**Question 2:** The exam is 'open-note' but not 'open-internet'. Which of the following resources is strictly prohibited?

  A) Your own completed lab assignments.
  B) The lecture slides provided by the instructor.
  C) A personal text file of notes you created.
  D) Searching for code solutions on Stack Overflow.

**Correct Answer:** D
**Explanation:** Using external websites like Stack Overflow, Chegg, or generative AI for answers is an academic integrity violation. The exam tests your understanding, using your own notes and course materials as a reference.

**Question 3:** What does the 'Don't get stuck' strategy advise you to do if you've made no progress on a problem for 10-15 minutes?

  A) Continue working on it until it's solved, no matter what.
  B) Leave a comment, move on to another problem, and return later if time permits.
  C) Guess the answer and submit it to get partial credit.
  D) Ask the teaching assistant for the solution.

**Correct Answer:** B
**Explanation:** It is far better to gain points on multiple problems than to waste all your time on a single one. The best strategy is to move on and come back to the difficult problem later.

**Question 4:** What is the primary goal of the 'Final Polish' phase (saving 5-10 minutes at the end)?

  A) To add detailed comments explaining every line of code.
  B) To make your code look prettier by reformatting it.
  C) To run all cells and check for simple errors or forgotten requirements.
  D) To start working on an extra credit problem.

**Correct Answer:** C
**Explanation:** The final review is for quality assurance. Running your code from top to bottom ensures it works as expected and helps you catch small but critical errors, like typos or incorrect function names.

### Activities
- Think-Pair-Share: In pairs, discuss which of the four strategic steps (Skim, Easy First, Don't Get Stuck, Review) you think will be most challenging for you to follow under pressure, and brainstorm one way to remind yourself to stick to the plan.
- Personal Strategy Plan: Take two minutes to write down a one-sentence commitment for how you will handle a situation where you get stuck on a problem for more than 10 minutes during the exam.

### Discussion Questions
- Why is it beneficial to solve the problems you are most confident in first, even if they are not the first questions on the exam?
- What are some common, simple errors that a final review of your code could help you catch?
- Beyond the strategies listed, what is one other thing you can do before the exam to feel more prepared and less anxious?

---

## Section 3: Core Concepts: Data & Expressions

### Learning Objectives
- Identify the four basic data types in Python: string, integer, float, and boolean.
- Explain the necessity of type casting when combining user input (strings) with numerical data.
- Use operators (`+`) for both arithmetic addition and string concatenation correctly.
- Write a simple program that takes user input, processes it, and prints a result.

### Assessment Questions

**Question 1:** What will the following code snippet print? `num_str = '25'; print('Value: ' + str(int(num_str) + 5))`

  A) Value: 255
  B) Value: 30
  C) A TypeError will occur.
  D) Value: '25'5

**Correct Answer:** B
**Explanation:** The string '25' is first cast to an integer using `int()`, resulting in the number 25. Then, 5 is added to it, yielding 30. Finally, the result (30) is cast back to a string using `str()` and concatenated with 'Value: ' for printing.

**Question 2:** The `input()` function in Python always returns a value of what data type?

  A) Integer
  B) Float
  C) String
  D) It depends on what the user types in.

**Correct Answer:** C
**Explanation:** Regardless of whether the user enters numbers, letters, or symbols, the `input()` function captures that input and returns it as a string. It is the programmer's responsibility to convert it to another type if needed.

**Question 3:** Which line of code will cause a `TypeError`?

  A) `print('Age: ' + str(21))`
  B) `print(10 + 20.5)`
  C) `print('Score: ' + 100)`
  D) `print(int('50') + 50)`

**Correct Answer:** C
**Explanation:** This line will cause a `TypeError` because the `+` operator cannot be used to concatenate a string ('Score: ') with an integer (100). The integer must first be converted to a string using `str(100)`.

**Question 4:** What is the data type and value of the `result` variable after this code runs? `result = int(15.7)`

  A) Float, 16.0
  B) Integer, 16
  C) Float, 15.0
  D) Integer, 15

**Correct Answer:** D
**Explanation:** When a float is cast to an integer using `int()`, the decimal part is truncated (cut off), not rounded. Therefore, 15.7 becomes the integer 15.

### Activities
- **Code Trace:** Ask students to predict the data type and value of the variable `result` after the following lines are executed: `x = 10.5; y = '2'; result = int(x) + int(y)`.
- **Debugging Challenge:** Present the following broken code snippet and ask students to identify and fix the error. The goal is to add the user's number to 10. `user_num = input('Enter a number: '); result = 10 + user_num; print(result)`
- **Pair Programming:** Have students work in pairs to write a small program that asks a user for their birth year, converts it to an integer, calculates their approximate age, and prints a message like 'You are approximately 25 years old.'

### Discussion Questions
- Why is it crucial to convert the value from `input()` before performing mathematical operations? What would happen if you tried to multiply an age received from `input()` by 2 without converting it first?
- Can you think of a real-world example where a number (like a zip code or a phone number) is best stored as a string instead of an integer? Why?
- What is the difference between the operators `=` and `==` in Python? Can you give an example of each?

---

## Section 4: Control Flow Part 1: Conditionals

### Learning Objectives
- Explain how `if`, `elif`, and `else` statements control the flow of a program.
- Predict the output of a given conditional block for a specific input value.
- Understand that only one branch of an if/elif/else chain will execute.
- Differentiate the behavior of an `if-elif-else` chain from a series of independent `if` statements.

### Assessment Questions

**Question 1:** Given the code on the slide, what is printed if `score = 89`?

  A) Excellent!
  B) Satisfactory.
  C) Needs improvement.
  D) Both 'Excellent!' and 'Satisfactory.'

**Correct Answer:** B
**Explanation:** The code first checks `if score >= 90` (89 >= 90 is false). It then checks the next condition, `elif score >= 60` (89 >= 60 is true), so it prints 'Satisfactory.' and the conditional block terminates.

**Question 2:** What is the output if `score = 59`?

  A) Satisfactory.
  B) Needs improvement.
  C) Nothing is printed.
  D) The program will produce an error.

**Correct Answer:** B
**Explanation:** The program checks `if 59 >= 90` (False), then `elif 59 >= 60` (False). Since all preceding conditions are false, the code in the final `else` block is executed, printing 'Needs improvement.'

**Question 3:** Consider this code: `if score >= 90: print('A')` and `if score >= 60: print('B')`. What is printed if `score = 95`?

  A) Only 'A'
  B) Only 'B'
  C) Both 'A' and 'B'
  D) Nothing is printed.

**Correct Answer:** C
**Explanation:** This code uses two separate `if` statements, not an `if-elif` chain. Each `if` is evaluated independently. Since 95 >= 90 is true, 'A' is printed. Then, since 95 >= 60 is also true, 'B' is printed.

**Question 4:** In a single `if-elif-else` structure, what is the maximum number of code blocks that can be executed?

  A) 0
  B) 1
  C) 2
  D) All of them, if their conditions are true.

**Correct Answer:** B
**Explanation:** The fundamental rule of an `if-elif-else` chain is that it is mutually exclusive. The program executes the first block whose condition is true and then immediately skips the rest of the chain. Therefore, a maximum of one block can ever run.

### Activities
- Modify the Code: Challenge students to add an `elif` condition to the example to print 'Good job!' for scores between 80 and 89, inclusive. The new condition must be placed correctly in the chain.
- Debug the Logic: Present this faulty code: `if score >= 60: print('Satisfactory') elif score >= 90: print('Excellent!')`. Ask students to explain why a score of 95 would produce the wrong output ('Satisfactory') and how to fix it by reordering the conditions.
- Trace the Path: Have students manually trace the execution flow for `score = 90`. They should write down each condition checked (e.g., 'Is 90 >= 90?'), its result (True/False), and the final action taken by the program.

### Discussion Questions
- Why is the order of conditions in an `if-elif` chain so important? What would happen in the slide's example if we checked for `score >= 60` before checking for `score >= 90`?
- Can you think of a real-world scenario where you would need to use a series of separate `if` statements instead of an `if-elif-else` chain?
- What happens in a conditional structure that has an `if` and `elif` but no final `else` block if none of the conditions are met? What is the program's behavior?

---

## Section 5: Control Flow Part 2: Iteration

### Learning Objectives
- Differentiate between definite iteration (`for` loops) and indefinite iteration (`while` loops).
- Construct a `for` loop to iterate over a sequence like a list or a `range`.
- Identify the three essential components of a `while` loop: initialization, condition, and update.
- Explain the cause of an infinite loop and demonstrate how to prevent it in a `while` loop.

### Assessment Questions

**Question 1:** In the `while` loop example, what would happen if the line `count -= 1` was removed?

  A) The loop would run one extra time.
  B) The code would produce a syntax error.
  C) The loop would never execute.
  D) The loop would become an infinite loop.

**Correct Answer:** D
**Explanation:** Without the update step `count -= 1`, the value of `count` would remain 5 forever. The condition `count > 0` would always be true, causing the loop to print '5' indefinitely.

**Question 2:** Which statement best describes the primary use case for a `for` loop?

  A) To repeat a block of code until a user enters 'quit'.
  B) To execute a block of code a specific, known number of times.
  C) To run a game loop that continues as long as the player's health is above zero.
  D) To create a loop that can potentially run forever.

**Correct Answer:** B
**Explanation:** A `for` loop is used for definite iteration, meaning it's ideal when you know how many times you need to loop, such as iterating over all items in a list or using `range()` for a fixed count.

**Question 3:** What is the output of the following code snippet? `for i in range(4): print(i)`

  A) 1, 2, 3, 4
  B) 0, 1, 2, 3
  C) 0, 1, 2, 3, 4
  D) 4

**Correct Answer:** B
**Explanation:** The `range(n)` function generates a sequence of integers from 0 up to, but not including, `n`. Therefore, `range(4)` produces the sequence 0, 1, 2, 3.

**Question 4:** What is the final value of `total` after this code runs? `total = 0; numbers = [10, 20, 30]; for num in numbers: total += num`

  A) 30
  B) 50
  C) 60
  D) 0

**Correct Answer:** C
**Explanation:** The loop iterates through the `numbers` list. `total` is updated as follows: `0 + 10 = 10`, then `10 + 20 = 30`, and finally `30 + 30 = 60`.

### Activities
- Whiteboard Challenge: Ask students to write a `for` loop that iterates through the list `['a', 'b', 'c']` and prints each letter along with its index (e.g., '0: a', '1: b', '2: c'). This encourages thinking about how to get both the index and the value.
- Pair Programming - The Guessing Game: Have students pair up to write a `while` loop that implements a simple number guessing game. The program should pick a secret number, and the loop should continue asking the user for a guess until they get it right.
- Code Conversion: Present the `for` loop `for i in range(5): print(i)` and ask students to rewrite it as a `while` loop that produces the exact same output. This reinforces the three key parts of a `while` loop (initialization, condition, update).

### Discussion Questions
- Can you think of a real-world scenario where a `for` loop would be the best choice? What about a scenario where a `while` loop is clearly better?
- The DRY (Don't Repeat Yourself) principle is a core concept in programming. How do loops exemplify this principle, and what are the main benefits of avoiding repeated code?
- Infinite loops are a common bug. What are some strategies you could use to debug a program that seems to be stuck in a loop?

---

## Section 6: Data Structures: Lists

### Learning Objectives
- Define a list and explain its key properties: ordered and mutable.
- Create lists and access individual elements using both positive and negative indexing.
- Modify lists by adding elements with `.append()` and removing elements with `.pop()`.
- Utilize slicing to extract a sub-list from a larger list.
- Determine the size of a list using the built-in `len()` function.

### Assessment Questions

**Question 1:** Which two properties best describe a Python list?

  A) Ordered and Immutable
  B) Unordered and Mutable
  C) Ordered and Mutable
  D) Unordered and Immutable

**Correct Answer:** C
**Explanation:** Lists are 'ordered' because they maintain the sequence of items, and 'mutable' because they can be changed (add, remove, or modify items) after creation.

**Question 2:** Given the list `data = [10, 20, 30, 40, 50]`, what does the expression `data[-2]` return?

  A) 20
  B) 30
  C) 40
  D) An IndexError

**Correct Answer:** C
**Explanation:** Negative indexing counts from the end of the list. `data[-1]` is the last item (50), so `data[-2]` is the second-to-last item, which is 40.

**Question 3:** What is the final state of `items` after this code runs? `items = ['a', 'b', 'c']; items.append('d'); removed = items.pop(1)`

  A) ['a', 'c', 'd']
  B) ['a', 'b', 'c']
  C) ['a', 'b', 'd']
  D) ['b', 'c', 'd']

**Correct Answer:** A
**Explanation:** First, `.append('d')` adds 'd' to the end, making the list `['a', 'b', 'c', 'd']`. Then, `.pop(1)` removes the element at index 1 ('b'), resulting in the final list `['a', 'c', 'd']`.

**Question 4:** Consider the list `letters = ['p', 'q', 'r', 's', 't']`. Which slice produces the output `['q', 'r', 's']`?

  A) letters[1:3]
  B) letters[2:4]
  C) letters[1:4]
  D) letters[2:5]

**Correct Answer:** C
**Explanation:** Slicing `[start:stop]` includes the element at the `start` index but excludes the element at the `stop` index. To get 'q' (index 1), 'r' (index 2), and 's' (index 3), the slice must start at 1 and stop at 4.

### Activities
- Code Correction Challenge: The following code is supposed to replace the middle number with 99. Find and fix the error. `numbers = [1, 5, 10]; numbers[2] = 99`. (Hint: Remember zero-based indexing).
- List Building Exercise: Start with an empty list called `shopping_cart`. Use `.append()` to add 'milk', 'bread', and 'eggs'. Then, use `.pop()` to remove 'bread'. Finally, print the `shopping_cart` and its length using `len()`.
- Predict the Output: Without running the code, what will be the final value of `my_list`? `my_list = [10, 20, 30, 40]; my_list.pop(); my_list.append(my_list[0])`. Write down your prediction and then verify it.

### Discussion Questions
- Why is it useful for a list to be 'mutable'? Can you think of a real-world scenario where you would need to add or remove items from a collection?
- What do you think happens if you try to access an index that is out of bounds, for example, `my_list[10]` for a list with only 3 items? Why is this protective behavior important?
- The `.pop()` method removes an item and also *returns* it. When might it be useful to capture the removed item in a variable, like `removed_item = my_list.pop()`?

---

## Section 7: Modular Code: Functions

### Learning Objectives
- Explain why functions are used to create modular, readable, and reusable code, adhering to the DRY principle.
- Identify and describe the key components of a Python function: the `def` keyword, the function name, parameters, the function body, and the `return` statement.
- Distinguish between a function's parameters (placeholders in the definition) and the arguments (actual values passed during a call).
- Understand the flow of data in a function: input via parameters, processing in the body, and output via the `return` statement.

### Assessment Questions

**Question 1:** What is the primary purpose of the `return` keyword in a function?

  A) To print a value to the console.
  B) To stop the entire program from running.
  C) To send a value from the function back to where it was called.
  D) To define the function's parameters.

**Correct Answer:** C
**Explanation:** The `return` statement is used to exit a function and send a computed value (the function's output) back to the line of code that called the function. This allows the result to be stored in a variable or used in another expression.

**Question 2:** In the code `circle_area = calculate_area(5)`, what is the correct term for the value `5`?

  A) A parameter
  B) An argument
  C) A return value
  D) A variable

**Correct Answer:** B
**Explanation:** An argument is the actual value (in this case, `5`) that is passed to a function when it is called. This value is assigned to the function's corresponding parameter (in this case, `radius`).

**Question 3:** Which of the following best describes the 'DRY' (Don't Repeat Yourself) principle?

  A) Writing code that is as short as possible.
  B) Avoiding writing the same block of logic multiple times by using functions.
  C) Ensuring every variable has a unique name.
  D) Commenting on every line of code to explain it.

**Correct Answer:** B
**Explanation:** The DRY principle is about reducing repetition. Functions are the primary tool for this, as they allow you to define a piece of logic once and reuse it wherever needed, making the code more maintainable and less error-prone.

**Question 4:** What will be the value of the `result` variable after this code runs? `def greet(name): message = f'Hello, {name}'
result = greet('Alice')`

  A) 'Hello, Alice'
  B) 'Alice'
  C) An error
  D) None

**Correct Answer:** D
**Explanation:** The `greet` function does not have a `return` statement. In Python, if a function completes without an explicit `return`, it automatically returns the special value `None`. Therefore, the `result` variable will hold the value `None`.

### Activities
- Spot the Bug: Show the students this code: `def add(a, b): print(a + b)` followed by `result = add(3, 4)`. Ask them to predict the value of `result` and explain why it is `None` and not `7`. This exercise reinforces the critical difference between printing a value and returning it.
- Pair Programming - Write a Function: Ask students to pair up and write a function called `get_greeting` that takes one parameter, `name`, and returns a string like 'Welcome, [name]!'. They should then write a line of code to call this function and print the returned result.

### Discussion Questions
- What are the benefits of giving a function a clear, descriptive name like `calculate_area` instead of a short name like `ca`?
- Can you think of a real-world analogy for a function (e.g., a recipe, a coffee machine)? How does the 'input, process, output' model apply?
- What do you think would happen if you tried to call the `calculate_area` function without providing a number inside the parentheses, like `calculate_area()`? Why?

---

## Section 8: The Art of Problem-Solving & Debugging

### Learning Objectives
- List and describe the four key steps of the systematic problem-solving process.
- Articulate the purpose of pseudocode and use it to plan a simple algorithm.
- Identify critical information (error type, line number) from a Python traceback message to locate a bug.
- Explain why identifying and handling edge cases (like empty lists or lists with insufficient data) is a crucial part of the problem-solving process.

### Assessment Questions

**Question 1:** Which step in the four-step process involves writing pseudocode or drawing a flowchart?

  A) Understand the Problem
  B) Test & Debug
  C) Translate to Code
  D) Plan Your Algorithm

**Correct Answer:** D
**Explanation:** Planning your algorithm is the crucial step between understanding the problem and writing code. Pseudocode helps you outline the logic of your solution without getting bogged down in specific programming syntax.

**Question 2:** When 'Understanding the Problem', which of the following is considered an 'edge case' for a function that finds the largest number in a list?

  A) A list containing only positive numbers
  B) An empty list
  C) A list sorted in descending order
  D) A list containing duplicate numbers

**Correct Answer:** B
**Explanation:** An edge case is a special condition or input at the extreme boundaries that might cause the code to fail if not handled explicitly. An empty list is a classic example because it has no 'first' or 'largest' element, potentially causing an IndexError.

**Question 3:** What is the most valuable information a Python traceback message provides for debugging?

  A) A suggestion for a more efficient algorithm
  B) The amount of time the program ran before crashing
  C) The exact line number and type of error that occurred
  D) A link to the official Python documentation

**Correct Answer:** C
**Explanation:** A traceback's primary purpose is to pinpoint the location (file and line number) and the nature of the error (e.g., IndexError, TypeError). This information is critical for quickly locating and fixing bugs.

**Question 4:** If you write a function to calculate the average of a list and it crashes with a `ZeroDivisionError`, what step of the problem-solving process did you most likely overlook?

  A) Translate to Code
  B) Test & Debug
  C) Understand the Problem (specifically, an edge case)
  D) Plan Your Algorithm (specifically, the loop logic)

**Correct Answer:** C
**Explanation:** A `ZeroDivisionError` in an average function typically happens when dividing the sum by the count of numbers, which is zero for an empty list. This is an edge case that should be identified and planned for during the 'Understand the Problem' step.

### Activities
- {'title': 'Pseudocode Practice', 'description': 'Write pseudocode for a function that takes a list of numbers and returns a new list containing only the even numbers. Be sure to consider the edge case of an empty input list.'}
- {'title': 'Traceback Detective', 'description': 'Given the following buggy Python code and its traceback, identify: 1) The type of error. 2) The line number where the error occurred. 3) The reason for the error and how you would fix it. \n\nCode:\n`def get_name_initials(names):\n    print(f"First initial: {names[0][0]}")\n    print(f"Last initial: {names[1][0]}")\n\nget_name_initials([\'Alice\'])`\n\nTraceback:\n`Traceback (most recent call last):\n  File "main.py", line 5, in <module>\n    get_name_initials([\'Alice\'])\n  File "main.py", line 3, in get_name_initials\n    print(f"Last initial: {names[1][0]}")\nIndexError: list index out of range`'}

### Discussion Questions
- Why is it often a mistake to start writing code immediately after reading a problem description? Share an experience where planning first might have saved you time.
- The slide says a traceback is your 'best friend.' Why might a beginner feel intimidated by a traceback, and how can they change that mindset to see it as a helpful tool?
- Besides an empty list, what other 'edge cases' might you need to consider for a function that finds the largest number in a list? (e.g., a list with one item, a list with all identical numbers, a list containing non-numeric data?)

---

## Section 9: Integrated Practice Problem

### Learning Objectives
- Apply the four-step problem-solving process (Understand, Plan, Code, Test) to a complete programming problem.
- Translate a pseudocode plan into a working Python function.
- Synthesize the concepts of functions, lists, `for` loops, and `if` statements to solve a single problem.
- Write and interpret test cases, including standard and edge cases, to verify code correctness.

### Assessment Questions

**Question 1:** Inside the `for` loop of the `filter_long_words` function, what is the correct conditional check to meet the problem's requirements?

  A) `if word > min_length:`
  B) `if len(word) >= min_length:`
  C) `if word.length() > min_length:`
  D) `if len(word) == min_length:`

**Correct Answer:** B
**Explanation:** The problem asks for words that are *longer than or equal to* the minimum length. In Python, the `len()` function returns the length of a string, and the `>=` operator correctly checks for 'greater than or equal to'.

**Question 2:** What is the primary purpose of the line `result_list = []` at the beginning of the function?

  A) To clear any previous data from the input `word_list`.
  B) To create a new, empty list to store the results, ensuring the original list is not modified.
  C) To declare a variable that will hold the length of the longest word.
  D) To satisfy a Python syntax requirement for `for` loops.

**Correct Answer:** B
**Explanation:** This line initializes an empty accumulator list. It is crucial for fulfilling the requirement to return a *new list* and avoids side effects by not changing the original input list.

**Question 3:** Given the test case `filter_long_words(['cat', 'dog', 'elephant'], 5)`, what will the function return?

  A) `['elephant']`
  B) `[]`
  C) `['cat', 'dog']`
  D) `None`

**Correct Answer:** A
**Explanation:** The function iterates through the list. 'cat' (len 3) and 'dog' (len 3) are less than 5. 'elephant' (len 8) is greater than or equal to 5, so it is appended to the result list, which is then returned.

**Question 4:** If the `return result_list` line was accidentally omitted from the function, what would a call like `filter_long_words(words, 5)` return?

  A) An empty list `[]`
  B) The original list `words`
  C) A `SyntaxError`
  D) `None`

**Correct Answer:** D
**Explanation:** In Python, if a function completes its execution without an explicit `return` statement, it implicitly returns the special value `None`.

### Activities
- Live Coding: Implement the `filter_long_words` function live, translating each line of pseudocode into Python. Ask students to predict what each line does before you type it.
- Think-Pair-Share: In pairs, students modify the function to create a new function called `filter_by_exact_length(word_list, exact_length)` that returns only the words with a length exactly matching `exact_length`.
- Code Debugging Challenge: Present a version of the function with a common bug (e.g., appending `len(word)` instead of `word`, or modifying the list being iterated over) and have students identify and fix the error.

### Discussion Questions
- Why is it important to create a *new* list instead of modifying the original one? What problems could modifying the original list cause in a larger program?
- Besides the edge case shown (no words are long enough), what are other edge cases you might test for this function? (e.g., an empty input list, a list containing non-string elements).
- How could you write this function in a single line using a list comprehension? What are the pros and cons of that approach compared to the `for` loop version?

---

## Section 10: Q&A and Final Reminders

### Learning Objectives
- Identify key resources and effective strategies for exam preparation (labs, assignments, office hours, Q&A forums).
- Articulate any remaining questions about course concepts to receive clarification.
- Recognize the importance of non-academic preparation, such as getting adequate rest and managing time during the exam.
- Differentiate between passive studying (re-reading) and active studying (problem-solving from scratch).

### Assessment Questions

**Question 1:** What is cited as the single best way to prepare for the midterm exam?

  A) Reading a new textbook on advanced Python.
  B) Memorizing every line of the lecture slides.
  C) Redoing the labs and programming assignments from Weeks 1-7.
  D) Getting a good night's sleep, as no other preparation is needed.

**Correct Answer:** C
**Explanation:** The slide explicitly states that redoing and understanding the practical assignments is the most effective form of preparation, as it involves active problem-solving.

**Question 2:** According to the speaker's notes, what is the key difference between a function that `print`s a value and one that `return`s a value?

  A) There is no functional difference; they both display output.
  B) A `return` statement sends a value back from the function that can be stored in a variable and used in other calculations, while `print` only displays it to the console.
  C) `print` is used for numbers and `return` is used for strings.
  D) A function with a `return` statement runs faster than a function with a `print` statement.

**Correct Answer:** B
**Explanation:** The notes highlight that `return` allows the function's output to be captured and reused programmatically, which is a fundamental concept. `print` is for display purposes only.

**Question 3:** When stuck on a concept for more than a few minutes, what is the recommended course of action?

  A) Give up on that concept and hope it is not on the exam.
  B) Continue working in isolation until the problem is solved, no matter how long it takes.
  C) Formulate a specific question and ask for help on the course Q&A forum or in office hours.
  D) Switch to reviewing lecture notes, as asking questions is inefficient.

**Correct Answer:** C
**Explanation:** The slide and notes advise against studying in isolation and encourage students to use available resources like forums and office hours when they are stuck.

**Question 4:** The speaker notes suggest that creating a one-page 'cheat sheet' is a valuable study technique. What is the primary benefit of this activity?

  A) To have a document to use secretly during the exam.
  B) The process of making it forces you to synthesize, prioritize, and organize the most important concepts.
  C) It is the fastest way to re-read all the course material.
  D) It allows you to copy code examples that can be memorized for the exam.

**Correct Answer:** B
**Explanation:** The value of creating a summary sheet lies in the active learning process of deciding what is most important and how concepts are related, which reinforces memory and understanding.

### Activities
- Open Q&A Session: Dedicate the remaining time to an open forum where students can ask any lingering questions about the topics reviewed or the exam logistics.
- Self-Assessment Minute: Ask students to take 60 seconds to silently write down the one or two topics they feel least confident about. This will help them prioritize their studying.
- Forum Post Draft: As a group, walk through creating a 'good' question for the Q&A forum based on a common confusion point (e.g., list mutability), demonstrating how to provide context and code for an effective post.

### Discussion Questions
- Why is re-solving a problem from a blank file a more effective study method than simply re-reading your previous solution?
- Let's discuss one of the common confusion points: When is a dictionary a much better choice for storing data than a list? Can someone provide a real-world example?
- What is the difference in how you approach a problem when you know you can earn partial credit for your logic versus an all-or-nothing grading scheme?
- Beyond what was mentioned, what is one study technique that you have personally found very effective for a technical course like this one?

---

