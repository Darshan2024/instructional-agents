# Assessment: Slides Generation - Chapter 2: Expressions, Operators, and User Input

## Section 1: Chapter 2: Expressions, Operators, and User Input

### Learning Objectives
- Identify the four main topics of the chapter: expressions, operators, user input, and type casting.
- Explain the fundamental difference between a static program and an interactive one.
- Articulate the importance of user input for creating dynamic and useful applications.
- Recognize why type casting is a necessary step when handling user-provided data for calculations.

### Assessment Questions

**Question 1:** What is the primary shift in programming skills being introduced in this chapter?

  A) Moving from writing static scripts to creating dynamic, interactive programs.
  B) Learning how to design complex graphical user interfaces.
  C) Focusing on advanced memory management techniques.
  D) Understanding how to compile code for different operating systems.

**Correct Answer:** A
**Explanation:** The slide explicitly states we are moving from static programs with fixed output to dynamic ones that can take user input and perform calculations, making them interactive.

**Question 2:** According to the slide, what is the role of an 'operator' in programming?

  A) To store values like numbers and text.
  B) To act as 'action words' that perform specific operations on data.
  C) To get input directly from the user.
  D) To convert a program from one language to another.

**Correct Answer:** B
**Explanation:** Operators are defined as the 'action words' or 'verbs' (e.g., +, -, *) that perform operations on operands (data) to produce a result.

**Question 3:** Why is 'Type Casting' essential when working with user input for mathematical calculations?

  A) It makes the program's text output appear in a different font.
  B) User input is always considered a number, and it needs to be converted to text.
  C) It is a security feature to prevent hacking.
  D) User input is typically read as text (a string), and must be converted to a numerical type (like an integer) before it can be used in math.

**Correct Answer:** D
**Explanation:** The speaker notes highlight that when a user types a number like '42', the program reads it as a string. Type casting is required to convert this string into an actual number for calculations.

**Question 4:** Which of the following best defines an 'expression' as described in the chapter overview?

  A) Any line of code that prints text to the screen.
  B) A special keyword that defines the start of a program.
  C) A combination of values, variables, and operators that computes to produce a new value.
  D) The process of saving data to a file.

**Correct Answer:** C
**Explanation:** The slide content defines expressions as the 'phrases' of code that combine values, variables, and operators to be interpreted and computed into a new value.

### Activities
- Think-Pair-Share: With a partner, brainstorm three real-world applications (e.g., calculator app, online shopping cart, ATM). For each, identify: 1) What input does the user provide? 2) What operations might the program perform on that input? 3) What is the final result shown to the user?
- Quick Poll: Raise your hand if you have ever filled out a form online. The process of taking your typed information and using it is exactly what we're learning about. What kinds of information did you provide?

### Discussion Questions
- The speaker notes use the analogy of 'learning the alphabet' (Chapter 1) vs. 'forming sentences' (Chapter 2). Can you think of another analogy to describe this progression?
- Why is it crucial for a program to distinguish between the text '50' and the number 50? What problems could arise if it couldn't?
- Besides a calculator, what is a simple, interactive program you would want to build using the skills from this chapter?

---

## Section 2: Lesson Agenda

### Learning Objectives
- Familiarize with the topics to be covered in the lesson.
- Understand the logical flow from expressions to creating a complete interactive program.
- Anticipate the connection between user input, data types, and calculations.
- Set expectations for the lesson's key learning outcome.

### Assessment Questions

**Question 1:** According to the agenda, what is the primary purpose of the `input()` function?

  A) To perform mathematical calculations.
  B) To allow a program to get information from the user.
  C) To change the data type of a variable.
  D) To display a final message on the screen.

**Correct Answer:** B
**Explanation:** The `input()` function is specifically designed to make programs interactive by pausing execution and waiting for the user to type in data.

**Question 2:** Which topic on the agenda deals with converting data from one form to another, such as turning text into a number?

  A) What is an Expression?
  B) Performing Math: Arithmetic Operators
  C) Combining Text: String Operators
  D) Changing Data Types with Type Casting

**Correct Answer:** D
**Explanation:** Type Casting is the explicit process of converting a value's data type. This is crucial for using user input (which is text) in mathematical calculations.

**Question 3:** Based on the speaker's notes, an 'expression' is best described as:

  A) A complete, multi-line program.
  B) A question you ask Python that results in a single answer.
  C) A way to store text in a variable.
  D) The final output of the program shown to the user.

**Correct Answer:** B
**Explanation:** An expression is a combination of values, variables, and operators that Python evaluates to produce a single resulting value, like `5 + 3` evaluating to `8`.

**Question 4:** What is the key, practical skill you are expected to have by the end of this lesson?

  A) To build a complex website.
  B) To write a simple, interactive program that performs a calculation.
  C) To understand only the theory of Python syntax.
  D) To create professional graphics and animations.

**Correct Answer:** B
**Explanation:** The key goal stated is to combine all the lesson's concepts to create a program that can take user input, calculate something, and display a result.

### Activities
- KWL Chart: In your notes, create three columns: 'What I Know', 'What I Want to Know', and 'What I Learned'. Fill out the first two columns now based on the agenda items. We will fill the last column at the end of the lesson.
- Predict the Code: For one of the agenda items, such as 'Performing Math', try to guess what the Python code might look like. For example, how would you write 'five plus ten' in code? Share your guess.

### Discussion Questions
- Looking at the agenda, which topic seems most interesting or challenging to you, and why?
- Can you think of a simple, real-world example of an app (on your phone or computer) that must perform the steps listed in the agenda?
- Why do you think it's important to have a specific function for user input instead of just writing the data directly into the code?

---

## Section 3: What is an Expression?

### Learning Objectives
- Define the term 'expression' in the context of programming.
- Identify the three core components of an expression: values, variables, and operators.
- Understand that every expression 'evaluates' to a single output value.
- Recognize valid expressions in Python code for numbers and strings.

### Assessment Questions

**Question 1:** Which of the following is the best definition of an expression in Python?

  A) A line of code that does not produce a value.
  B) Any statement that is printed to the screen.
  C) A combination of values, variables, and operators that evaluates to a new, single value.
  D) A special keyword used to define a function.

**Correct Answer:** C
**Explanation:** An expression's core characteristic is that it can be evaluated or reduced to a single resulting value. It is the fundamental building block for creating data within a program.

**Question 2:** Given `items = 12`, which of the following is an expression that evaluates to a new value?

  A) `items = 12`
  B) `items * 2`
  C) `def count_items():`
  D) `print(items)`

**Correct Answer:** B
**Explanation:** `items * 2` is an expression that combines a variable (`items`) and a value (`2`) with an operator (`*`). Python evaluates it to produce the new value `24`. The other options are an assignment statement, a function definition, and a function call statement.

**Question 3:** The process by which Python computes an expression to find its resulting single value is called:

  A) Assignment
  B) Concatenation
  C) Execution
  D) Evaluation

**Correct Answer:** D
**Explanation:** Evaluation is the specific term for reducing an expression to its single output value. Execution is a broader term for running code, while assignment stores a value and concatenation joins strings.

**Question 4:** In the expression `'Total: ' + '100'`, what is the `+` symbol an example of?

  A) A variable
  B) An operator
  C) A literal value
  D) A data type

**Correct Answer:** B
**Explanation:** The `+` symbol is an operator. In this context, it performs string concatenation, joining the two string values together to produce `'Total: 100'`.

### Activities
- {'title': 'Predict the Output', 'description': 'For each line of code below, write down the single value that the expression will evaluate to.', 'tasks': ['Expression: `100 - 25` -> Predicted Output: ?', "Expression: `'First' + ' ' + 'Last'` -> Predicted Output: ?", 'Code: `base = 8; height = 4;` Expression: `0.5 * base * height` -> Predicted Output: ?']}
- {'title': 'Expression Spotting', 'description': 'Read the following Python code snippet. Identify and write down at least three distinct expressions found within it.', 'code_block': 'price = 99\ntax_rate = 0.07\nfinal_price = price + (price * tax_rate)\nprint(final_price)'}

### Discussion Questions
- Is a single value, like `42` or the string `'Python'`, also considered an expression? Why or why not?
- What is the key difference between the statement `area = width * height` and the expression `width * height`?
- Why is it useful for an expression to always simplify to a single value? How does this allow us to build more complex programs?

---

## Section 4: Core Arithmetic Operators

### Learning Objectives
- Identify and describe the purpose of Python's seven core arithmetic operators (+, -, *, /, //, %, **).
- Clearly differentiate between float division (`/`), integer division (`//`), and the modulo operator (`%`).
- Apply arithmetic operators to construct and evaluate basic mathematical expressions in Python.
- Use the modulo operator to solve practical problems like determining if a number is even or odd.

### Assessment Questions

**Question 1:** What is the result of the expression `17 // 3` in Python?

  A) 5.66
  B) 6
  C) 5
  D) 2

**Correct Answer:** C
**Explanation:** The `//` operator performs integer (or floor) division. It calculates how many times 3 can go into 17 completely, discarding any remainder. 3 goes into 17 five times (3 * 5 = 15), so the result is 5.

**Question 2:** Which Python expression correctly calculates the remainder when 25 is divided by 4?

  A) 25 / 4
  B) 25 // 4
  C) 25 % 4
  D) 25 ** 4

**Correct Answer:** C
**Explanation:** The modulo operator (`%`) is used to find the remainder of a division. 25 divided by 4 is 6 with a remainder of 1. Therefore, `25 % 4` evaluates to 1.

**Question 3:** What is the data type of the result of the expression `12 / 4`?

  A) Integer (int)
  B) Float (float)
  C) String (str)
  D) Boolean (bool)

**Correct Answer:** B
**Explanation:** The standard division operator (`/`) in Python always returns a float, even if the result is a whole number. The expression `12 / 4` evaluates to `3.0`.

**Question 4:** Which expression is equivalent to `5 * 5 * 5` in Python?

  A) 5 % 3
  B) 5 // 3
  C) 5 * 3
  D) 5 ** 3

**Correct Answer:** D
**Explanation:** The exponent operator (`**`) is used for raising a number to a power. `5 ** 3` means 5 to the power of 3, which is `5 * 5 * 5`.

### Activities
- {'type': 'coding_exercise', 'title': 'Pizza Party Calculator', 'description': 'You are organizing a pizza party. You have 35 slices of pizza and 8 guests. Write Python code to solve the following: \n1. Calculate how many slices each guest gets if they are distributed evenly. \n2. Calculate how many slices will be left over. \nUse the `//` and `%` operators and print both results.'}
- {'type': 'predict_the_output', 'title': 'Predict the Output', 'description': 'Without running the code, predict the final value of `result` in the following expression: `result = 10 + 20 % 7 - 2 ** 3`. Write down your answer and reasoning.'}

### Discussion Questions
- Why is it important for a programming language to have two distinct types of division (`/` and `//`)? Can you describe a scenario where using one over the other is critical?
- The modulo operator (`%`) is very useful for checking if a number is even or odd. What other real-world problems could you solve using the remainder of a division (e.g., scheduling, time calculations, cycling through a list of items)?
- If you perform the operation `10 / 0`, Python will raise an error. What do you think should happen, and why is dividing by zero a problem in mathematics and programming?

---

## Section 5: Order of Operations (PEMDAS)

### Learning Objectives
- Understand concepts from Order of Operations (PEMDAS)

### Activities
- Practice exercise for Order of Operations (PEMDAS)

### Discussion Questions
- Discuss the implications of Order of Operations (PEMDAS)

---

## Section 6: String Operators: Concatenation and Replication

### Learning Objectives
- Use the `+` operator to perform string concatenation.
- Use the `*` operator to perform string replication.
- Distinguish the behavior of `+` and `*` with strings versus numbers.
- Recognize and predict `TypeError` when mixing strings and incompatible types (like integers) in concatenation.

### Assessment Questions

**Question 1:** What will be the value of the `result` variable after this code runs: `result = 'Ha' * 4`?

  A) 'HaHaHaHa'
  B) 'Ha4'
  C) '4Ha'
  D) This will cause a TypeError.

**Correct Answer:** A
**Explanation:** The `*` operator, when used with a string and an integer, performs replication. It repeats the string 'Ha' four times, resulting in 'HaHaHaHa'.

**Question 2:** Which line of code will result in a `TypeError`?

  A) `message = 'Chapter' + ' ' + '1'`,
  B) `message = 'Player ' + str(1)`
  C) `message = 'Score: ' + 100`
  D) `line = '*' * 20`

**Correct Answer:** C
**Explanation:** Python cannot directly concatenate a string ('Score: ') with an integer (100). The integer must first be converted to a string, for example, using `str(100)`.

**Question 3:** What is the output of the following code? `val1 = '10'; val2 = '5'; print(val1 + val2)`

  A) 15
  B) '15'
  C) '105'
  D) This code will produce an error.

**Correct Answer:** C
**Explanation:** When the `+` operator is used with strings, it performs concatenation. It joins the string '10' and the string '5' together to form '105', rather than performing mathematical addition.

**Question 4:** How would you create a string variable `border` containing 20 hyphen characters (`-`)?

  A) `border = '-' + 20`
  B) `border = '-' * 20`
  C) `border = '-' * '20'`
  D) `border = 20 * '-'`

**Correct Answer:** B
**Explanation:** The replication operator `*` is used to repeat a string a specified number of times. The order `an_integer * a_string` is also valid, so D is also technically correct, but B is the most common convention.

### Activities
- {'type': 'code_challenge', 'title': 'Build a Welcome Banner', 'description': "Create a welcome banner for a program. First, create a variable `separator` that contains the character `=` repeated 30 times. Then, create a `message` variable with the string `'  WELCOME TO THE PROGRAM!  '`. Finally, print the `separator`, then the `message` on a new line, and then the `separator` again on a third line."}
- {'type': 'code_challenge', 'title': 'Format an Address', 'description': "Create three string variables: `house_number = '123'`, `street = 'Innovation Drive'`, and `city = 'Techville'`. Use string concatenation to combine them into a single `address` variable with the format '123 Innovation Drive, Techville'. Remember to include the space and the comma. Print the final `address`."}

### Discussion Questions
- Why do you think Python raises an error for `'Agent ' + 7` instead of automatically converting the `7` to a string `'7'`? What are the pros and cons of this language design choice?
- Can you think of a real-world scenario where the string replication operator (`*`) would be very useful for formatting output in a program?
- What do you predict would happen if you tried `'test' * 0`? What about `'test' * -1`? Let's test it and discuss why the result is what it is.

---

## Section 7: Making Programs Interactive: The `input()` Function

### Learning Objectives
- Explain the purpose of the `input()` function for creating interactive programs.
- Use the `input()` function with a string prompt to get data from a user.
- Store the result returned by the `input()` function in a variable.
- State the crucial rule that `input()` always returns a string, regardless of the user's entry.

### Assessment Questions

**Question 1:** What is the data type of the value returned by the `input()` function?

  A) Integer
  B) Float
  C) It depends on what the user types.
  D) String

**Correct Answer:** D
**Explanation:** The crucial rule of the `input()` function is that it always captures user input as a string, regardless of whether the user enters digits, letters, or symbols.

**Question 2:** Consider the following code: `city = input('Enter your city: ')`. What is the text 'Enter your city: ' referred to as?

  A) The return value
  B) The variable
  C) The prompt
  D) The function call

**Correct Answer:** C
**Explanation:** The string passed inside the parentheses of the `input()` function is called the prompt. Its purpose is to give instructions to the user about what information they should enter.

**Question 3:** A user runs the script below and types `42` when prompted. What is the output?

  A) <class 'int'>
  B) <class 'string'>
  C) <class 'str'>
  D) 42

**Correct Answer:** C
**Explanation:** Even though the user typed numbers, `input()` returns the value as a string. The `type()` function correctly identifies the data type of the `user_age` variable as a string, which is represented as `<class 'str'>` in Python.

**Question 4:** What is the primary role of the `input()` function in a Python program?

  A) To print data to the console for the user to read.
  B) To perform mathematical calculations.
  C) To pause program execution and wait for user-provided data.
  D) To convert strings into numbers.

**Correct Answer:** C
**Explanation:** The main purpose of `input()` is to make a program interactive by pausing it, displaying a prompt, and waiting for the user to type something and press Enter. The entered data is then returned to the program.

### Activities
- Write a Program: Create a small Python script that asks the user for their favorite food and then prints a message saying, 'I like to eat [favorite food] too!'
- Mad Libs Style: Write a program that asks the user for a noun, a verb, and an adjective. Then, use these variables to print a funny sentence, such as 'The [adjective] [noun] decided to [verb] by the lake.'

### Discussion Questions
- Why is it important for a program to be able to get input from a user? Can you name three real-world examples of software that rely heavily on user input?
- The slide states you cannot directly perform math on the result of `input()`. If `age_str = input('Enter age: ')` and the user types `20`, what do you predict would happen if we tried to run `age_str + 5`? Why?
- What makes a good 'prompt' for the user? Why is `input('Enter your full name: ')` better than just `input()` with no prompt?

---

## Section 8: The `input()` Problem: A Common Bug

### Learning Objectives
- Identify the common `TypeError` that arises from mixing strings and integers with the `+` operator.
- Explain why performing mathematical operations directly on the output of `input()` causes an error.
- Interpret the meaning of the `TypeError: can only concatenate str (not "int") to str` message.

### Assessment Questions

**Question 1:** Why does the code `age_string = input('Age: '); age_next_year = age_string + 1` fail?

  A) Python cannot add the number 1 to a variable.
  B) The `input()` function is written incorrectly.
  C) Python cannot perform mathematical addition between a string and an integer.
  D) The variable `age_next_year` was not defined first.

**Correct Answer:** C
**Explanation:** This code causes a `TypeError` because the `input()` function returns a string. The `+` operator cannot be used to add two different data types (a string from `input()` and an integer `1`) in this way.

**Question 2:** If a user enters the number `50` at an `input()` prompt, what is the data type of the value returned by the function?

  A) Integer (`int`)
  B) String (`str`)
  C) Float (`float`)
  D) Number

**Correct Answer:** B
**Explanation:** The `input()` function always captures user input and returns it as a string, regardless of what the user types. So, entering `50` results in the string value `'50'`.

**Question 3:** What does the error message `TypeError: can only concatenate str (not "int") to str` specifically tell you?

  A) You used the wrong variable name for your string.
  B) You are trying to use the `+` operator to join an integer to a string, which is not allowed.
  C) You forgot to put quotes around the number `1`.
  D) The `input()` function has a bug and needs to be fixed.

**Correct Answer:** B
**Explanation:** The message indicates a type mismatch. Python interpreted the `+` as string concatenation because one of the operands was a string. It then failed because the other operand was an integer, not another string.

**Question 4:** Consider the code: `val = input('Enter a number: ')`. If the user enters `10`, what will be the result of `val + '5'`?

  A) 15
  B) 105
  C) '105'
  D) A TypeError

**Correct Answer:** C
**Explanation:** Since `input()` returns a string, `val` will be `'10'`. The `+` operator with two strings (`'10'` and `'5'`) performs concatenation, joining them to create the new string `'105'`.

### Activities
- **Debug the Bug**: Copy the example bug from the slide into a Python file. Run it, enter a number, and observe the `TypeError`. Write one sentence explaining what the error message means in your own words.
- **Predict the Output**: Without running the code, predict the output or error for each of the following snippets. Then, run them to check your predictions and explain why they were right or wrong.
1. `x = '99'; print(x + 1)`
2. `y = '99'; print(y + '1')`
3. `z = input('Enter a number: '); print(z * 2)` (Hint: What does the `*` operator do with a string?)

### Discussion Questions
- Why do you think Python's designers chose to raise an error when you try to add a string and a number, instead of trying to guess what you mean?
- Can you think of a situation where you would want the `input()` function to return a string, even if the user enters only numbers (e.g., a phone number or a zip code)?
- Based on the error message, how could you change the line `age_next_year = age_string + 1` so that it no longer crashes, even if the result isn't mathematically correct? (Hint: Think about concatenation.)

---

## Section 9: Converting Data Types (Casting)

### Learning Objectives
- Define 'casting' as the explicit conversion of a value from one data type to another.
- Utilize the `int()`, `float()`, and `str()` functions to correctly convert between strings, integers, and floating-point numbers.
- Explain why casting is a necessary step to perform mathematical operations on user input received from the `input()` function.
- Identify and correct `TypeError` and `ValueError` exceptions that arise from incorrect data type operations and invalid casting attempts.

### Assessment Questions

**Question 1:** What is the primary reason for casting the result of the `input()` function to an integer or float?

  A) To make the text display in a different color.
  B) Because the `input()` function always returns a string, which cannot be used in mathematical calculations.
  C) To reduce the memory used by the variable.
  D) To convert the number into a format that can be saved in a file.

**Correct Answer:** B
**Explanation:** The `input()` function captures all user input as a string. If you want to perform arithmetic operations like addition or subtraction, you must first convert that string into a numeric type like `int` or `float`.

**Question 2:** Which line of code will result in a `ValueError`?

  A) `int("100")`
  B) `float("45.8")`
  C) `str(99)`
  D) `int("5.0")`

**Correct Answer:** D
**Explanation:** The `int()` function can only convert strings that represent whole numbers. The string '5.0' contains a decimal point, which is not valid for an integer conversion and will raise a `ValueError`. It would need to be converted to a `float` first.

**Question 3:** What will be the output of the following Python code snippet?
```python
x = 15.7
y = int(x)
print(str(y) + " items")
```

  A) `16 items`
  B) `15.7 items`
  C) `15 items`
  D) A TypeError

**Correct Answer:** C
**Explanation:** `int(15.7)` converts the float to an integer by truncating (not rounding) the decimal part, resulting in `y` being `15`. Then, `str(15)` converts the integer to the string '15', which is concatenated with ' items' for the final output.

**Question 4:** A user enters '3.14' when prompted. Which line of code correctly converts this input into a number that can be used for precise calculations?

  A) `num = int(user_input)`
  B) `num = str(user_input)`
  C) `num = float(user_input)`
  D) `num = cast(user_input)`

**Correct Answer:** C
**Explanation:** `float()` is used to convert a string into a floating-point number, which can represent numbers with decimal points. `int()` would cause an error because '3.14' is not a valid integer string. `str()` would keep it as a string, and `cast()` is not a built-in Python function.

### Activities
- **Fix the Bug:** Using the buggy code from the previous activity (where adding 1 to the user's age produced an error), add a line that uses the `int()` function to cast the user's string input into an integer. Confirm that the program now runs correctly and calculates the age for the next year.
- **Simple Calculator:** Write a program that prompts the user for two numbers. Convert both inputs to floating-point numbers using `float()`. Then, calculate and print their sum. Ensure the final print statement combines text and the calculated number correctly, which may require a final `str()` cast.

### Discussion Questions
- In the example code, we cast `age_next_year` back to a string using `str()` before printing. What `TypeError` do you get if you try `print('Next year, you will be ' + age_next_year)` without the cast? Why?
- What happens if you try to cast a non-numeric string, like `int('hello')`, to an integer? What kind of error does this produce and why is it different from a `TypeError`?
- When would you choose to use `float()` over `int()` when converting user input? Provide a real-world example where `float()` is the more appropriate choice.

---

## Section 10: Chapter Summary & Key Takeaways

### Learning Objectives
- Summarize the roles of expressions, operators, `input()`, and casting in a Python program.
- Correctly apply the order of operations (PEMDAS) to predict the outcome of a complex expression.
- Differentiate the behavior of the `+` and `*` operators when used with numbers versus strings.
- Synthesize the chapter's concepts to write a complete, simple interactive program that takes numerical input and performs a calculation.

### Assessment Questions

**Question 1:** What is the final value of the `result` variable after this code runs? `result = 10 + 4 * 2 ** 2`

  A) 26
  B) 56
  C) 116
  D) 22

**Correct Answer:** A
**Explanation:** According to PEMDAS (Order of Operations), exponentiation (`**`) is first: `2 ** 2` is 4. Then multiplication (`*`): `4 * 4` is 16. Finally, addition (`+`): `10 + 16` is 26.

**Question 2:** A user runs the following code and enters `20` at the prompt. What is the output? `age = input('Enter your age: '); print('Next year you will be ' + age + 1)`

  A) Next year you will be 21
  B) Next year you will be 201
  C) The code runs without error but prints nothing.
  D) The code will raise a TypeError.

**Correct Answer:** D
**Explanation:** The `input()` function returns the string '20'. The code then tries to add a string ('20') to an integer (1), which is not allowed in Python and results in a TypeError. The string must first be cast to an integer using `int()`.

**Question 3:** Which line of code will produce the string `'Python-Python-Python-'`?

  A) `print('Python-' * 3)`
  B) `print('Python' * 3 + '-')`
  C) `print('Python' + '-' * 3)`
  D) `print(('Python' * 3) + '-')`

**Correct Answer:** A
**Explanation:** The string replication operator (`*`) repeats the entire string on its left. 'Python-' is treated as a single string, and multiplying it by 3 repeats it three times, resulting in 'Python-Python-Python-'.

**Question 4:** Which of the following lines of code correctly gets a user's age and calculates how old they were 5 years ago?

  A) `past_age = input('Enter age: ') - 5`
  B) `past_age = int(input('Enter age: ')) - 5`
  C) `past_age = str(input('Enter age: ') - 5)`
  D) `past_age = input(int('Enter age: ')) - 5`

**Correct Answer:** B
**Explanation:** This option correctly nests the `input()` function inside `int()`. This gets the user's input as a string and immediately casts it to an integer, allowing the subtraction to be performed correctly.

### Activities
- **Mini-Project: Simple Area & Perimeter Calculator.** Write a program that asks the user for the width and height of a rectangle. The program should then calculate both the area (width * height) and the perimeter (2 * width + 2 * height) and print the results in two separate, user-friendly sentences.
- **Exercise: Tip Calculator.** Create a program that asks the user for the total of a restaurant bill. Then, ask for the percentage of the tip they want to leave (e.g., 15, 18, 20). The program should calculate the tip amount and the total bill (bill + tip). Print the original bill, the tip amount, and the final total for the user. Remember to use `float()` for currency.

### Discussion Questions
- Why does Python's `input()` function *always* return a string, even if the user types only numbers? What are the advantages or potential problems with this design choice?
- Consider the expression `2 + 3 * 4`. We know it evaluates to 14. When would it be a good idea to write it as `2 + (3 * 4)` instead, even though the parentheses are not strictly necessary?
- The modulo operator (`%`) is often used to check if a number is even or odd. How would you use it to do that? Can you think of another practical use for the modulo operator (e.g., in games, time calculations, or data processing)?

---

