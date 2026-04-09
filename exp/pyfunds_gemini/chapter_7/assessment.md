# Assessment: Slides Generation - Chapter 7: Functions: Creating Reusable Code

## Section 1: Chapter 7: Functions: Creating Reusable Code

### Learning Objectives
- Understand concepts from Chapter 7: Functions: Creating Reusable Code

### Activities
- Practice exercise for Chapter 7: Functions: Creating Reusable Code

### Discussion Questions
- Discuss the implications of Chapter 7: Functions: Creating Reusable Code

---

## Section 2: Why Do We Need Functions?

### Learning Objectives
- Explain the 'Don't Repeat Yourself' (DRY) principle and its connection to functions.
- Describe how functions improve code readability and maintainability.
- Articulate how code isolation within functions simplifies the debugging process.
- Define abstraction and provide an example of how functions enable it in programming.

### Assessment Questions

**Question 1:** The programming principle 'Don't Repeat Yourself' (DRY) is most directly addressed by which benefit of functions?

  A) Enabling Abstraction
  B) Improving Readability
  C) Simplifying Debugging
  D) Reducing Redundancy

**Correct Answer:** D
**Explanation:** The DRY principle is fundamentally about avoiding the duplication of code. Functions allow you to write a piece of logic once and call it multiple times, which directly reduces code redundancy and adheres to this principle.

**Question 2:** When you use a function like Python's `len()` without needing to understand its internal code, you are benefiting from which concept?

  A) Abstraction
  B) Redundancy
  C) Repetition
  D) Debugging

**Correct Answer:** A
**Explanation:** Abstraction is the concept of hiding complex implementation details. By using `len()`, you interact with a simple interface (giving it a list) to get a result (an integer) without needing to know the complex process it uses internally.

**Question 3:** A program is written as one long, 500-line script. How would breaking it down into smaller, well-named functions primarily improve it for other developers?

  A) It would make the program run faster.
  B) It would improve readability by organizing the code into logical blocks.
  C) It would eliminate the need for comments.
  D) It would reduce the file size of the script.

**Correct Answer:** B
**Explanation:** Well-named functions act like chapters in a book, allowing a reader to understand the program's overall structure and purpose at a glance. This significantly improves the code's readability and maintainability.

**Question 4:** An error message (traceback) in your program points directly to a function named `calculate_final_grade()`. How does this feature of functions aid in development?

  A) It proves the function is reusable.
  B) It simplifies debugging by isolating the problem to a small section of code.
  C) It automatically fixes the bug within the function.
  D) It shows that the code is readable.

**Correct Answer:** B
**Explanation:** Functions create isolated scopes for logic. When an error occurs inside a function, the error message points to that specific location, narrowing the search for the bug and making the debugging process much faster and more efficient.

### Activities
- {'title': 'Code Refactoring Exercise', 'description': 'Examine the following repetitive script that calculates and prints shipping costs. Your task is to refactor it by creating a single function called `calculate_shipping` that takes `weight` as an input, calculates the cost, and returns it. Then, call this function for each item to produce the same output.', 'code_before': "```python\n# Item 1\nweight1 = 5\ncost1 = 5 + (weight1 * 0.75)\nprint(f'Shipping for item 1 (5 lbs): ${cost1:.2f}')\n\n# Item 2\nweight2 = 12\ncost2 = 5 + (weight2 * 0.75)\nprint(f'Shipping for item 2 (12 lbs): ${cost2:.2f}')\n\n# Item 3\nweight3 = 2.5\ncost3 = 5 + (weight3 * 0.75)\nprint(f'Shipping for item 3 (2.5 lbs): ${cost3:.2f}')\n```", 'code_after_solution': "```python\ndef calculate_shipping(weight):\n    base_cost = 5\n    cost_per_lb = 0.75\n    return base_cost + (weight * cost_per_lb)\n\nweight1 = 5\nweight2 = 12\nweight3 = 2.5\n\nprint(f'Shipping for item 1 (5 lbs): ${calculate_shipping(weight1):.2f}')\nprint(f'Shipping for item 2 (12 lbs): ${calculate_shipping(weight2):.2f}')\nprint(f'Shipping for item 3 (2.5 lbs): ${calculate_shipping(weight3):.2f}')\n```"}

### Discussion Questions
- Besides a car, what is another real-world analogy for abstraction? How does it relate to using a function you didn't write yourself?
- Imagine you are working on a large software project with a team of 10 developers. Why does adhering to the DRY principle become critically important in this scenario?
- Is it possible to overuse functions by making them too small or too numerous? What might be the downside of breaking a program into too many tiny functions?

---

## Section 3: Anatomy of a Python Function

### Learning Objectives
- Identify all components of a basic function definition: `def` keyword, name, parentheses, colon, and indented body.
- Understand that indentation is a critical and mandatory part of Python's syntax for defining code blocks.
- Differentiate between required and optional parts of a function, such as the `return` statement.
- Recognize and correct common syntax errors in a function definition.

### Assessment Questions

**Question 1:** Which symbol is used to mark the end of a function header and signal the beginning of the indented function body?

  A) A semicolon (;)
  B) A colon (:)
  C) A period (.)
  D) An equals sign (=)

**Correct Answer:** B
**Explanation:** The colon (:) is a crucial part of Python syntax. It terminates the function header line (the `def` statement) and indicates that the following indented block of code is the body of the function.

**Question 2:** How does Python determine which lines of code are part of a function's body?

  A) By using curly braces { }
  B) By consistent indentation
  C) By using the 'end' keyword
  D) By enclosing them in parentheses ( )

**Correct Answer:** B
**Explanation:** Python's syntax relies on indentation (typically 4 spaces) to define code blocks. All lines indented at the same level after the function header are considered part of the function's body.

**Question 3:** Which of the following is NOT a required part of a Python function definition?

  A) The 'def' keyword
  B) The function name and parentheses ()
  C) A 'return' statement
  D) An indented code block (the body)

**Correct Answer:** C
**Explanation:** A function definition requires the `def` keyword, a name, parentheses, a colon, and an indented body. The `return` statement is optional; a function can perform actions without sending a value back. If omitted, the function implicitly returns `None`.

**Question 4:** What is the primary role of parameters like `num1` and `num2` in a function definition `def my_func(num1, num2):`?

  A) They are global variables accessible anywhere.
  B) They are placeholder variables for the inputs the function will receive.
  C) They are the values the function returns.
  D) They are decorative and have no functional role.

**Correct Answer:** B
**Explanation:** Parameters are local variables that act as placeholders for the arguments (actual values) that will be passed into the function when it is called. They only exist within the scope of the function.

### Activities
- Syntax Correction Challenge: Provide students with several broken function definitions and ask them to identify and fix the errors. For example: `function_one(a, b) # Missing 'def'`, `def function_two(a, b) # Missing colon`, `def function_three(a, b): print(a+b) # Missing indentation`.
- Anatomy Labeling: Present a complete function definition and ask students to label each part: `def` keyword, function name, parameters, colon, indented body, and `return` statement.
- Code Scramble: Provide the components of a function definition (`def`, `greet_user`, `(name)`, `:`, `message = 'Hello, ' + name`, `return message`) out of order and ask students to assemble them into a valid function.

### Discussion Questions
- Why is choosing a descriptive function name (like `calculate_area` instead of `x`) important for writing readable and maintainable code?
- Python uses indentation to define code blocks, while other languages like Java or C++ use curly braces `{}`. What do you think are the pros and cons of Python's approach?
- What happens if a function doesn't have a `return` statement? What value does it give back to the caller?

---

## Section 4: Defining and Calling a Simple Function

### Learning Objectives
- Distinguish between a function definition and a function call.
- Understand that a function's code is not executed until the function is explicitly called.
- Correctly use the `def` keyword to define a simple function.
- Identify and use the correct syntax (parentheses `()`) to call a function.

### Assessment Questions

**Question 1:** What is the primary difference between defining and calling a function in Python?

  A) There is no difference; they are two terms for the same action.
  B) Defining creates and stores the function's code, while calling executes that stored code.
  C) Calling creates the function, while defining executes the code inside it.
  D) Defining checks the function for errors, while calling runs the code.

**Correct Answer:** B
**Explanation:** Defining a function (using the `def` keyword) is like writing a recipe; it creates a set of instructions and stores them under a name. The code inside does not run. Calling the function (using its name followed by parentheses `()`) is like following the recipe; it executes the stored instructions.

**Question 2:** Which line of code correctly **calls** a function named `calculate_total`?

  A) def calculate_total()
  B) calculate_total
  C) call calculate_total()
  D) calculate_total()

**Correct Answer:** D
**Explanation:** To call, or execute, a function, you must write its name followed by a set of parentheses `()`. The name alone (`calculate_total`) refers to the function object itself but does not run its code.

**Question 3:** What will be the output of the following Python code?

```python
print("Program Start")

def show_message():
    print("Inside Function")

print("Program End")
```

  A) Program Start
   Inside Function
   Program End
  B) Program Start
   Program End
  C) Inside Function
  D) The code will produce a syntax error.

**Correct Answer:** B
**Explanation:** The function `show_message` is defined, but it is never called. Therefore, the `print("Inside Function")` statement is never executed. Python runs the code line by line, skipping over the contents of the `def` block until it is called.

**Question 4:** Which keyword is used to **define** a new function in Python?

  A) function
  B) call
  C) def
  D) run

**Correct Answer:** C
**Explanation:** The `def` keyword is the standard Python syntax for starting a function definition. It is short for 'define'.

### Activities
- {'type': 'Live Coding', 'description': "Start with a script containing only a function definition, such as `def show_status(): print('System is online.')`. Run the script to demonstrate that nothing happens. Then, add the line `show_status()` to the end and run it again to show the message being printed, highlighting the effect of the function call."}
- {'type': 'Code Correction', 'description': "Provide students with this code snippet and ask them to fix it so the header is printed: \n```python\n# This code should print a report header\ndef print_header():\n    print('====================')\n    print('   ANNUAL REPORT    ')\n    print('====================')\n\nprint('Generating report...')\n# --- FIX ME: The header should be printed here ---\nprint('Report generation complete.')\n```\n The solution is to add `print_header()` in the 'FIX ME' section."}
- {'type': 'Reusability Challenge', 'description': 'Ask students to write a function `draw_separator()` that prints a line of 20 asterisks. Then, instruct them to call this function multiple times to structure a simple program output, for example, before and after a welcome message.'}

### Discussion Questions
- Why do you think programming languages separate the act of defining a function from calling it? What problems might occur if the code inside a function ran the moment it was defined?
- In our 'recipe' analogy, what would be the real-world equivalent of calling the same function multiple times from different parts of a program?
- Can you think of a task in a real program (like a video game, a social media app, or a calculator) where you would define a set of instructions once and need to execute it many times?

---

## Section 5: Passing Information with Parameters

### Learning Objectives
- Define the terms 'parameter' and 'argument' and accurately differentiate between them.
- Create a Python function that accepts a single argument to customize its behavior.
- Call a function multiple times with different arguments to demonstrate its reusability.
- Explain how parameters make code more flexible and powerful.

### Assessment Questions

**Question 1:** In the code `def personalized_greet(name):`, the variable `name` is known as a(n):

  A) Argument
  B) Function call
  C) Parameter
  D) String literal

**Correct Answer:** C
**Explanation:** A parameter is the placeholder variable defined inside the function's parentheses (`name`). An argument is the actual value (`"Alice"`) passed to the function when it is called.

**Question 2:** What is the primary benefit of using parameters in functions?

  A) To make functions run faster.
  B) To make functions more reusable and flexible.
  C) To ensure functions can only be called once.
  D) To automatically document the code.

**Correct Answer:** B
**Explanation:** Parameters allow a single function to operate on different data (arguments), making it highly reusable and flexible for various scenarios without needing to rewrite the logic.

**Question 3:** Consider the following code: `def show_price(item_cost): print(f"The cost is ${item_cost}")`. Which line of code correctly calls this function?

  A) show_price()
  B) show_price(item_cost = 25)
  C) def show_price(25)
  D) The function cannot be called.

**Correct Answer:** B
**Explanation:** The function `show_price` is defined with one parameter, `item_cost`. Therefore, it must be called with one argument. `show_price(25)` is a valid way to call it, and `show_price(item_cost = 25)` (using a keyword argument) is also correct and often clearer.

**Question 4:** What will be the output of the following Python code?

```python
def describe_pet(animal_type):
    print(f"I have a {animal_type}.")

describe_pet("cat")
```

  A) I have a animal_type.
  B) I have a {animal_type}.
  C) I have a cat.
  D) The code will produce a TypeError.

**Correct Answer:** C
**Explanation:** The argument `"cat"` is passed to the function, where it is assigned to the parameter `animal_type`. The f-string then correctly substitutes the value of the `animal_type` variable into the printed string.

### Activities
- {'type': 'Code Creation', 'title': 'Create a Temperature Converter', 'description': "Write a function named `celsius_to_fahrenheit` that takes one parameter, `temp_celsius`. Inside the function, calculate the equivalent temperature in Fahrenheit (Formula: F = C * 9/5 + 32) and print the result in a user-friendly format, like '25 C is 77 F'. Call your function with three different Celsius values: 0, 25, and 100."}
- {'type': 'Code Debugging', 'title': 'Fix the Greeting Function', 'description': 'The following code is supposed to greet a user by their city but has an error. Identify the error and fix the code so it runs correctly.', 'code': '```python\n# This code has an error. Find and fix it.\ndef welcome_message():\n    print(f"Welcome, visitor from {city}!")\n\nwelcome_message("Paris")\n```', 'solution_explanation': "The error is a `NameError` because the function `welcome_message` does not know what `city` is. It needs to be defined as a parameter in the function's signature, like this: `def welcome_message(city):`."}

### Discussion Questions
- Using the vending machine analogy from the slide, what would be an example of a function that needs *two* parameters? What might the arguments for that function call look like?
- What do you think would happen if you defined a function like `def my_func(my_number):` but called it with a string, like `my_func("hello")`? Would it work? Why or why not?
- How does using a parameter to pass information into a function compare to using a global variable that the function can access? What are the advantages of the parameter approach?

---

## Section 6: Getting Results with the `return` Statement

### Learning Objectives
- Explain the purpose of the `return` keyword in a function.
- Write a function that accepts parameters, performs a calculation, and returns the result.
- Demonstrate how to call a function and store its returned value in a variable.
- Describe what a function returns by default if no `return` statement is present.
- Understand that `return` causes a function to exit immediately.

### Assessment Questions

**Question 1:** What is the primary purpose of the `return` statement in a Python function?

  A) To print a value to the console.
  B) To stop the entire script from running.
  C) To send a value back to the code that called the function.
  D) To define a new global variable with the result.

**Correct Answer:** C
**Explanation:** The `return` statement's specific job is to pass a value from within a function back to the calling code, allowing the result of the function's work to be used elsewhere.

**Question 2:** Consider the code below. What will be the value of the `message` variable after it runs?

```python
def get_status(score):
    if score > 50:
        return "Pass"
    else:
        return "Fail"
    print("Grading complete.")

message = get_status(75)
```

  A) "Pass"
  B) "Fail"
  C) "Grading complete."
  D) The code will cause an error.

**Correct Answer:** A
**Explanation:** The function is called with `75`, which is greater than `50`, so the `if` block executes. The function hits `return "Pass"` and immediately exits, sending the string "Pass" back. The `print` statement after the if/else block is never reached.

**Question 3:** What value does a Python function return by default if it completes without an explicit `return` statement?

  A) 0
  B) The special value `None`
  C) An empty string ("")
  D) It raises a syntax error.

**Correct Answer:** B
**Explanation:** If a function's execution finishes without encountering a `return` keyword, Python automatically returns the special value `None` to indicate the absence of a return value.

**Question 4:** Which line of code correctly calls the `calculate_area` function and stores its result?

  A) `calculate_area(12, 6)`
  B) `print(calculate_area)`
  C) `my_area = calculate_area(12, 6)`
  D) `return calculate_area(12, 6)`

**Correct Answer:** C
**Explanation:** To capture a returned value, you must use an assignment statement (`=`). The function call `calculate_area(12, 6)` is evaluated, its returned value is produced, and that value is then assigned to the variable `my_area`.

### Activities
- **Write a Function:** Create a function `to_celsius(fahrenheit)` that takes a temperature in Fahrenheit, converts it to Celsius using the formula `(F - 32) * 5/9`, and returns the result. Call the function with the value `98.6` and print the returned value.
- **Debugging Challenge:** The following function is supposed to greet a user, but it's not storing the greeting correctly. Find the bug and fix it.

```python
# Buggy Code
def create_greeting(name):
    message = f"Welcome, {name}!"
    # What's missing here?

user_greeting = create_greeting("Alex")
print(user_greeting)
# Expected output: Welcome, Alex!
# Actual output: None
```

### Discussion Questions
- When would you choose to use `return` in a function versus just using `print()`? What are the key differences in how the output can be used?
- Imagine you are building a simple e-commerce checkout system. How would functions with `return` statements be used to calculate a subtotal, add tax, and compute the final total?
- The speaker notes mention that code after a `return` statement is unreachable. Can you think of a scenario where you might have multiple `return` statements inside a single function (e.g., using `if` statements)?

---

## Section 7: Understanding Variable Scope: Local vs. Global

### Learning Objectives
- Define 'scope' in the context of programming and explain why it is important.
- Differentiate between local scope (inside a function) and global scope (outside all functions).
- Trace the lifecycle of a local variable: creation on function call and destruction on function completion.
- Predict whether a variable can be accessed from a specific part of a script and identify the potential for a `NameError`.

### Assessment Questions

**Question 1:** A variable created inside a function is called a 'local' variable. What is the primary characteristic of its scope?

  A) It can be accessed from anywhere in the program after the function has been called once.
  B) It can only be accessed by other functions, but not the main script.
  C) It only exists and can only be accessed while the function is running.
  D) It permanently overwrites any global variable that has the same name.

**Correct Answer:** C
**Explanation:** Local scope means the variable is confined to the function where it was created. It is instantiated when the function starts and destroyed when the function ends, making it inaccessible from outside.

**Question 2:** In the slide's code example, why can `my_function` successfully `print(global_var)`?

  A) Because `print()` is a special function that can access any variable.
  B) Because the function first looks for `global_var` locally, doesn't find it, and then looks in the global scope.
  C) Because `global_var` was passed as a hidden parameter to `my_function`.
  D) Because all functions automatically create a local copy of every global variable.

**Correct Answer:** B
**Explanation:** Python's scope resolution rule (LEGB: Local, Enclosing, Global, Built-in) means that when a variable is accessed, the interpreter first checks the local scope. If not found, it checks higher-level scopes, including the global scope.

**Question 3:** What is the direct result of trying to run `print(local_var)` outside of `my_function` after it has finished executing?

  A) It will print the last known value of `local_var`.
  B) It will print `None`.
  C) It will cause a `SyntaxError` because you cannot print variables there.
  D) It will cause a `NameError` because `local_var` no longer exists.

**Correct Answer:** D
**Explanation:** The variable `local_var` is destroyed when `my_function` completes. Attempting to access it from the global scope after this point results in a `NameError` because the name is not defined in that scope.

**Question 4:** Which of the following best describes a 'global' variable?

  A) A variable that can only be modified but not read from within a function.
  B) A variable defined inside a function that is used in many other functions.
  C) A variable defined in the main body of a script, outside of any function.
  D) A special type of variable that must have its name in all capital letters.

**Correct Answer:** C
**Explanation:** A global variable is one that exists in the top-level scope of the script, not enclosed within any function definition, making it accessible throughout the script.

### Activities
- {'title': 'Predict the Output', 'description': 'Provide students with the following code snippet and ask them to write down the exact output. If they predict an error, they should name the error and explain why it occurs.\n\n```python\nteam = "Marketing"\n\ndef print_report():\n    report_id = 505\n    print(f"Generating report for {team} team.")\n    print(f"Report ID is {report_id}")\n\nprint_report()\nprint(f"Last used team was {team}")\n# print(f"Last report ID was {report_id}") # What would happen here?\n```'}
- {'title': 'Debug the Scope', 'description': 'Give students a broken piece of code that incorrectly relies on local scope. Their task is to fix it using function parameters and return values, as recommended in the \'Best Practices\'.\n\n**Broken Code:**\n```python\nuser_name = "Alex"\n\ndef create_greeting():\n    # This should create a greeting for the user_name\n    message = "Hello, " + user_name + "!"\n\ncreate_greeting()\nprint(message) # <-- This will fail!\n```\n\n**Task:** Modify the function `create_greeting` to accept a name as a parameter and return the message, then call it and print the returned result correctly.'}

### Discussion Questions
- Why is it generally considered better practice to pass data into functions via parameters and get data out via `return` statements, rather than relying on global variables?
- Can you think of a situation where using a global variable might be necessary or at least convenient? What are the risks?
- If two different functions both create a local variable with the exact same name (e.g., `counter`), do they interfere with each other? Why or why not?

---

## Section 8: The Power of Decomposition

### Learning Objectives
- Define problem decomposition and its purpose in programming.
- Apply decomposition to a problem statement by identifying the necessary sub-tasks.
- Explain how individual functions can be used to solve each sub-task.
- Articulate the key benefits of decomposition, such as clarity, reusability, and easier debugging.

### Assessment Questions

**Question 1:** Problem decomposition is the practice of:

  A) Writing one single function to solve a complex problem.
  B) Breaking a large problem into smaller, more manageable sub-problems.
  C) Converting all variables to a global scope.
  D) Combining multiple scripts into one file.

**Correct Answer:** B
**Explanation:** Decomposition is a problem-solving technique where a complex task is broken down into simpler parts. In programming, each part is typically implemented as a separate function.

**Question 2:** Which of the following is a primary benefit of using problem decomposition in programming?

  A) It guarantees the program will run faster.
  B) It eliminates the need for comments in the code.
  C) It improves code reusability and makes debugging easier.
  D) It automatically reduces the program's memory usage.

**Correct Answer:** C
**Explanation:** Decomposition leads to modular functions that are self-contained. This makes them easy to reuse in other parts of the program and easier to test and debug in isolation.

**Question 3:** In the provided example, what is the role of the 'Main Code' section?

  A) To perform all the complex mathematical calculations itself.
  B) To act as an 'orchestrator' that calls specialized functions in the correct order.
  C) To define the `calculate_discounted_price` and `add_tax` functions.
  D) To store the original price and final price in a database.

**Correct Answer:** B
**Explanation:** The main part of the program coordinates the high-level workflow. It calls the smaller, specialized functions in the correct sequence to solve the overall problem.

**Question 4:** If you needed to add a shipping fee calculation to the example, how would you best apply the principle of decomposition?

  A) Add the shipping fee logic directly into the `add_tax` function.
  B) Create a new, dedicated function like `add_shipping_fee(price, fee)`.
  C) Put all the calculations (discount, tax, shipping) into one large block in the main code.
  D) Declare a global variable for the shipping fee.

**Correct Answer:** B
**Explanation:** The principle of decomposition suggests that each distinct task should have its own function. Adding a shipping fee is a distinct sub-problem that warrants its own function for clarity, reusability, and maintainability.

### Activities
- {'type': 'group_planning', 'title': 'Plan a Grading Calculator', 'description': "Describe a problem like 'Calculate a student's final grade based on homework (40%), quizzes (20%), and a final exam (40%).' As a group, outline the functions you would create to solve this (e.g., `calculate_average()`, `calculate_weighted_score()`, `determine_letter_grade()`). Justify why each task deserves its own function."}
- {'type': 'code_challenge', 'title': 'Build a Trip Cost Calculator', 'description': 'Write a Python script that uses decomposition to solve the following problem: Calculate the total cost of a trip. The program should have separate functions to calculate flight costs, hotel costs, and daily spending. The main part of your script should call these functions and sum their results to get a final trip cost. For example, create `calculate_flight_cost(destination)`, `calculate_hotel_cost(nights)`, and `calculate_spending(days)`.'}

### Discussion Questions
- Think about a complex, non-programming task you do in your daily life (e.g., planning a trip, cooking a meal). How do you naturally use 'decomposition' to manage it?
- When might it be a bad idea to decompose a problem? Is there a point where a problem is 'too simple' to break down into more functions?
- In the example code, the result of `calculate_discounted_price` is passed as an argument to `add_tax`. Why is this flow of data between functions essential for solving the overall problem correctly?

---

## Section 9: Putting It All Together: A Complete Example

### Learning Objectives
- Analyze a complete program that is structured using multiple functions.
- Trace the flow of data as it is passed into functions as arguments and sent out as return values.
- Explain the benefits of decomposing a problem into smaller, single-purpose functions, such as modularity, readability, and reusability.

### Assessment Questions

**Question 1:** In the temperature converter example, what is the main benefit of having three separate functions (`get_celsius_input`, `convert_c_to_f`, `display_result`)?

  A) It makes the program run significantly faster.
  B) It uses less memory than a single block of code.
  C) Each function has a single, clear responsibility, which improves readability and makes the code easier to debug.
  D) It is the only way to get input from the user in Python.

**Correct Answer:** C
**Explanation:** This structure exemplifies the principle of problem decomposition. Each function handles one distinct part of the overall task (input, processing, output), which makes the program easy to read, test, and maintain.

**Question 2:** Which function in the script is primarily responsible for performing a calculation and returning a value, without directly interacting with the user?

  A) `get_celsius_input()`
  B) `convert_c_to_f()`
  C) `display_result()`
  D) The main part of the script

**Correct Answer:** B
**Explanation:** The `convert_c_to_f` function takes a number as a parameter, performs the conversion formula, and returns the result. It is self-contained and handles only the core logic, not user input or output.

**Question 3:** What would happen if you swapped the last two lines in the 'Main part of the script'?

  A) The program would run correctly but display the result first.
  B) The program would crash with a `NameError` because the `fahrenheit` variable has not been defined yet.
  C) The program would ask for input twice.
  D) The program would run without errors but produce an incorrect conversion.

**Correct Answer:** B
**Explanation:** The line `fahrenheit = convert_c_to_f(celsius)` must execute before `display_result(celsius, fahrenheit)` can be called. If not, the `fahrenheit` variable won't exist when `display_result` tries to access it, leading to a `NameError`.

**Question 4:** If you wanted to modify the program to convert Celsius to Kelvin, which is the only function you would need to change?

  A) You would need to rewrite the entire script.
  B) `get_celsius_input()`
  C) `display_result()`
  D) `convert_c_to_f()`

**Correct Answer:** D
**Explanation:** Thanks to modularity, the conversion logic is isolated within the `convert_c_to_f` function. You could change the formula inside it (e.g., to `kelvin = celsius_temp + 273.15`) without affecting the input or display functions.

### Activities
- **Code Tracing:** Manually trace the flow of execution in the temperature converter script. On a piece of paper, start at the 'Main part' and follow the function calls, keeping track of the values of the `celsius` and `fahrenheit` variables as they are created and updated. Assume the user inputs '20'.
- **Modify the Code:** Add a new function called `convert_c_to_k(celsius_temp)` that converts Celsius to Kelvin (Formula: K = C + 273.15). Modify the main part of the script to call this new function and change `display_result` to show the Kelvin temperature as well.
- **Refactor:** Below is the same program written without functions. Your task is to refactor it into the three-function structure shown on the slide to improve its readability and modularity.

```python
# Monolithic script
c_temp_str = input("Enter temp in Celsius: ")
c_temp_float = float(c_temp_str)
f_temp = (c_temp_float * 9/5) + 32
print(f"{c_temp_float:.1f}C is equal to {f_temp:.1f}F.")
```

### Discussion Questions
- What would be the disadvantages if the `convert_c_to_f` function also contained the `print` statement, making the `display_result` function unnecessary? How would that affect its reusability?
- Imagine this program needed to get the temperature from a web API or a file instead of user input. Which function(s) would you need to change? Why does the current design make this change relatively easy?
- The 'Main part of the script' acts as an 'orchestrator' that calls other functions to get a job done. Can you think of a real-world analogy for this relationship (e.g., a general contractor hiring a plumber and an electrician)?

---

## Section 10: Chapter 7: Summary

### Learning Objectives
- Summarize the syntax for defining a function with `def` and executing it with a call.
- Explain the roles of parameters as placeholders and arguments as actual values.
- Differentiate between a function that `prints` a value and one that `returns` a value.
- Define 'local scope' and explain why variables inside a function are not accessible globally.
- Describe how 'decomposition' is used to break complex problems into simpler functions.

### Assessment Questions

**Question 1:** What is the primary purpose of the `return` keyword in a Python function?

  A) To print a value to the console for the user to see.
  B) To stop the execution of the entire program immediately.
  C) To send a value back to the code that called the function.
  D) To define a new variable that can be used globally.

**Correct Answer:** C
**Explanation:** The `return` keyword is used to pass a value from the function's scope back to the caller's scope, allowing the result of the function's work to be stored in a variable or used in further calculations.

**Question 2:** Consider the following code snippet. What will happen when it is executed?

```python
def create_greeting(name):
    message = f"Welcome, {name}!"
    return message

my_greeting = create_greeting("Alex")
print(message)
```

  A) It will print 'Welcome, Alex!'.
  B) It will print 'message'.
  C) It will do nothing.
  D) It will raise a NameError.

**Correct Answer:** D
**Explanation:** The variable `message` is created inside the `create_greeting` function, so it has a local scope. It only exists within that function and is destroyed when the function completes. Trying to access it outside the function will result in a NameError.

**Question 3:** Which statement best describes the problem-solving technique of 'decomposition'?

  A) Combining multiple small functions into one large function to improve performance.
  B) Breaking down a large, complex problem into smaller, manageable sub-problems, each solved by a function.
  C) The process of a function calling itself repeatedly.
  D) Ensuring that variables created inside a function are not accessible outside of it.

**Correct Answer:** B
**Explanation:** Decomposition is a core programming strategy where a complex task is divided into simpler, more focused functions. This makes the overall program easier to design, read, test, and debug.

**Question 4:** In a function definition `def calculate(value1, value2):`, what are `value1` and `value2` called?

  A) Arguments
  B) Return values
  C) Local variables
  D) Parameters

**Correct Answer:** D
**Explanation:** In a function definition, the variables listed inside the parentheses are placeholders for the inputs and are called parameters. The actual values passed to the function during a call are called arguments.

### Activities
- {'title': 'Code Correction: Scope Sleuth', 'description': 'The following code is supposed to calculate the total cost of an item with tax and print a formatted summary, but it has a scope error. Find the error, explain why it happens, and fix the code so it runs correctly.', 'code': '```python\ndef calculate_total(price):\n    tax = price * 0.07\n    total = price + tax\n\ncalculate_total(50)\n# The line below will cause an error!\nprint(f"The total cost is ${total:.2f}")\n```'}
- {'title': 'Decomposition Challenge: Plan a Program', 'description': 'You need to write a program that asks a user for their first name and last name, combines them into a full name, and then prints a personalized greeting. Before writing any code, plan the program by describing at least two functions you would create. For each function, specify its name, its parameters (if any), and what it should `return`.'}

### Discussion Questions
- Why is local scope a beneficial feature in programming? What kind of problems might arise if all variables were global?
- Can you think of a real-world scenario where you would need a function to `return` a value instead of just `print`ing it? Why is the returned value more useful in that case?
- How does decomposing a problem into smaller functions make it easier for a team of programmers to collaborate on a single project?

---

