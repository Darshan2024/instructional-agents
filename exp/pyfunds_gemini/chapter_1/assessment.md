# Assessment: Slides Generation - Chapter 1: Introduction to Programming & Python

## Section 1: Chapter 1: Introduction to Programming & Python

### Learning Objectives
- Understand concepts from Chapter 1: Introduction to Programming & Python

### Activities
- Practice exercise for Chapter 1: Introduction to Programming & Python

### Discussion Questions
- Discuss the implications of Chapter 1: Introduction to Programming & Python

---

## Section 2: Core Concepts: Program and Algorithm

### Learning Objectives
- Define the term 'algorithm' as a finite, unambiguous, step-by-step plan for solving a problem.
- Define the term 'program' as the implementation of an algorithm in a specific, executable programming language.
- Distinguish between the abstract logic of an algorithm and the concrete syntax of a program using analogies.
- Explain the standard workflow: starting with a problem, designing an algorithm, and then writing a program.

### Assessment Questions

**Question 1:** What is the key difference between an algorithm and a program?

  A) An algorithm is the code written in Python, and a program is the idea behind it.
  B) An algorithm is the abstract set of logical steps to solve a problem, while a program is the implementation of those steps in a language a computer can execute.
  C) A program and an algorithm are exactly the same thing, just with different names.
  D) A program is a plan for solving a problem, and an algorithm is what the computer runs.

**Correct Answer:** B
**Explanation:** An algorithm is the language-independent logical plan (the 'recipe idea'), whereas a program is the concrete set of instructions written in a specific programming language that a computer can execute (the 'finished recipe card').

**Question 2:** Which of the following is a key characteristic of an ALGORITHM?

  A) It must be written in a specific programming language like Python.
  B) It must be unambiguous, with each step having a clear and single meaning.
  C) It must be executable by a computer's processor.
  D) It must follow strict syntax rules.

**Correct Answer:** B
**Explanation:** A core characteristic of a good algorithm is that its steps are clear and unambiguous. It is a conceptual plan, so it is not tied to a specific language, syntax, or the ability to be directly executed by a machine.

**Question 3:** You sketch a flowchart on a whiteboard to illustrate the steps for sorting a list of numbers from smallest to largest. This flowchart represents a(n):

  A) Program
  B) Syntax error
  C) Algorithm
  D) Executable file

**Correct Answer:** C
**Explanation:** A flowchart is a visual representation of the logical steps to solve a problem. Since it's a language-independent plan and not executable code, it is a perfect example of an algorithm.

**Question 4:** The correct workflow for creating software, as described in the slide, is:

  A) Program → Algorithm → Problem
  B) Problem → Algorithm → Program
  C) Algorithm → Problem → Program
  D) Program → Problem → Algorithm

**Correct Answer:** B
**Explanation:** The logical process is to first identify the problem, then design a step-by-step plan (the algorithm) to solve it, and finally, implement that plan as code (the program).

### Activities
- Write down the algorithm (a numbered list of steps) for a simple, non-computer task, like making a cup of tea or tying your shoelaces. Check if your steps are unambiguous and finite.
- In small groups, translate the algorithm for finding the average of three numbers into pseudo-code, similar to the coffee machine example. You don't need to write real code, just outline the program's logic.
- Given the problem 'Find the largest of three numbers', write out the algorithm you would use to solve it. Compare your algorithm with a partner's.

### Discussion Questions
- Why is it important to design a good algorithm *before* you start writing a program?
- Can you have a program without an algorithm? Why or why not?
- The slide mentioned an algorithm must be 'finite'. What could happen if an algorithm was not finite and a computer tried to run a program based on it?
- Think of an app you use every day (e.g., a map app). What is one algorithm that might be part of that app's program? (e.g., the algorithm for finding the shortest route).

---

## Section 3: Our Toolkit: Python and Google Colab

### Learning Objectives
- Identify Python as the programming language and Google Colab as the coding environment for the course.
- Explain the primary benefits of Python for beginners, such as its readable syntax.
- Describe the main advantages of using Google Colab, particularly its zero-installation nature.
- Distinguish between the role of a programming language (Python) and a coding environment (Google Colab).

### Assessment Questions

**Question 1:** According to the presentation, what is the primary reason Python is considered an excellent language for beginners?

  A) It is the most powerful language for machine learning.
  B) Its syntax is simple, clean, and resembles plain English.
  C) It was developed by Google for use in Colab.
  D) It runs faster than any other programming language.

**Correct Answer:** B
**Explanation:** The key reason Python is ideal for beginners is its emphasis on code readability. The simple, English-like syntax allows learners to focus on programming concepts rather than complex language rules.

**Question 2:** What is the most significant advantage of using Google Colab for this course?

  A) It provides access to paid, premium software libraries.
  B) It only works on computers with high-end processors.
  C) It allows you to code in a web browser without installing any software.
  D) It automatically backs up all files to your local hard drive.

**Correct Answer:** C
**Explanation:** The main benefit of Google Colab for a learning environment is its 'zero installation' nature. This removes technical barriers and ensures everyone has a consistent, ready-to-use coding workspace.

**Question 3:** Which statement best describes the relationship between Python and Google Colab?

  A) They are two different names for the same tool.
  B) Python is a feature within the Google Colab application.
  C) Google Colab is a specific version of the Python language.
  D) Python is the language, while Google Colab is the environment where we write and run the code.

**Correct Answer:** D
**Explanation:** This correctly summarizes the core distinction: Python is the 'what' (the programming language with its own rules and syntax), and Google Colab is the 'where' (the cloud-based platform or 'digital workspace' used to execute Python code).

### Activities
- Open a new browser tab and navigate to colab.research.google.com. Click 'New notebook' to create your first Colab notebook.
- In your new notebook, find the first code cell. Type `print('Success! I am using Python in Colab.')` and run the cell by clicking the play button or pressing Shift+Enter.
- Practice adding a text cell. Click the '+ Text' button and write a brief note about why you are interested in learning to code. Notice how you can mix notes and code in the same document.

### Discussion Questions
- The presentation compared Python's 'Hello, World!' to Java's. What were your initial thoughts on this comparison? Why is reducing this 'boilerplate' code helpful for learning?
- The speaker used the analogy 'Google Docs, but for code' to describe Colab. In what ways do you think this is an accurate comparison? Are there ways it might be different?
- Can you think of any potential downsides to using a cloud-based tool like Google Colab instead of installing Python directly on your own computer?

---

## Section 4: Navigating the Google Colab Environment

### Learning Objectives
- Distinguish between the purpose of a code cell and a text cell.
- Identify the two primary methods for executing a cell (Play button and keyboard shortcut).
- Understand that code in a cell must be explicitly run to produce an output.
- Describe the basic workflow of writing and running code within the Colab environment.

### Assessment Questions

**Question 1:** In Google Colab, what is the primary purpose of a 'Code Cell'?

  A) To write notes and explanations using formatted text.
  B) To display images and videos.
  C) To write and execute Python code.
  D) To change the notebook's file name.

**Correct Answer:** C
**Explanation:** Code cells are specifically designed for writing and running programming code, like Python. Text cells are used for notes and documentation.

**Question 2:** What is the most common and efficient keyboard shortcut to run a cell and move to the next one in Google Colab?

  A) Ctrl + S
  B) Alt + Enter
  C) Ctrl + C
  D) Shift + Enter

**Correct Answer:** D
**Explanation:** Shift + Enter is the standard shortcut to execute the current cell and advance to the next, making it a very efficient way to work through a notebook.

**Question 3:** If you want to add a title, headings, and explanations to your notebook, which type of cell should you use?

  A) A Code Cell
  B) A Text Cell
  C) An Output Cell
  D) A Terminal Cell

**Correct Answer:** B
**Explanation:** Text cells are designed for documentation. They use Markdown to allow for rich text formatting, including headings, lists, bold/italic text, and links, which is perfect for explaining your code.

**Question 4:** What happens immediately after you write code in a code cell?

  A) The code runs automatically.
  B) The code is saved but does not run until you execute it.
  C) A new text cell is created below it.
  D) The notebook is automatically shared.

**Correct Answer:** B
**Explanation:** Writing code in a cell simply places it there. To make the computer follow the instructions, you must explicitly 'run' or 'execute' the cell using the Play button or Shift+Enter.

### Activities
- Create a new Google Colab notebook. Add a text cell and type '# My First Notebook' to create a title. Below it, add a code cell with the following Python code: `print('Hello, Colab!')`. Practice running the code cell using both the 'Play' button and the Shift+Enter shortcut.
- In your notebook, create three separate code cells. In the first, define a variable `x = 10`. In the second, define `y = 20`. In the third, write `print(x + y)`. Run the cells in order using only the Shift+Enter shortcut to observe the workflow.

### Discussion Questions
- Why do you think it is beneficial to combine executable code and formatted text in a single document like a Colab notebook?
- What are the advantages of using a keyboard shortcut like Shift+Enter over repeatedly clicking the 'Play' button, especially in a long notebook?
- How does the write-run-repeat cycle in Colab differ from how you might write a program in a traditional text editor?

---

## Section 5: Your First Program: "Hello, World!"

### Learning Objectives
- Identify the `print()` function as the primary command for displaying output in Python.
- Explain the role of parentheses `()` and quotation marks `""` or `''` in a `print()` statement.
- Define the terms 'function', 'string', and 'argument' in the context of the 'Hello, World!' program.
- Write and execute a basic Python program to display a custom message.

### Assessment Questions

**Question 1:** Which line of code will correctly print the message 'Welcome!' to the screen?

  A) display("Welcome!")
  B) print "Welcome!"
  C) print('Welcome!')
  D) output('Welcome!')

**Correct Answer:** C
**Explanation:** The correct syntax in Python for displaying output is the `print()` function, with the text (a string) you want to display placed inside the parentheses and enclosed in either single or double quotes.

**Question 2:** In Python, what is the term for a piece of text, like "Hello, World!", that is enclosed in quotation marks?

  A) A function
  B) An argument
  C) A string
  D) A command

**Correct Answer:** C
**Explanation:** Textual data enclosed in single or double quotes is called a 'string' in Python. It is treated as literal text to be displayed or manipulated.

**Question 3:** A student writes the code `Print("Hello")`. Why will this code cause an error?

  A) It should use single quotes instead of double quotes.
  B) Python commands are case-sensitive, and the function name should be `print` (lowercase).
  C) Parentheses are not needed for this command.
  D) The text "Hello" is not a valid message.

**Correct Answer:** B
**Explanation:** Python is a case-sensitive language. The built-in function for printing is `print` (all lowercase). `Print` (with a capital P) is not a recognized command and will result in a `NameError`.

**Question 4:** In the line `print("Welcome!")`, what is the part `"Welcome!"` referred to as?

  A) The function
  B) The variable
  C) The argument
  D) The output

**Correct Answer:** C
**Explanation:** The data passed inside the parentheses of a function is called an argument. In this case, the string `"Welcome!"` is the argument being passed to the `print()` function.

### Activities
- In a code cell, write a single line of Python code to print your name and your favorite hobby.
- Write three separate `print()` statements. The first should print the name of your city, the second your state/province, and the third your country. Run the cell and observe how the output appears on three different lines.
- **Experiment with Errors:** Try running `print(Hello, World!)` without the quotation marks. Read the error message that Python gives you. What do you think it means?

### Discussion Questions
- Why do you think it's important that Python can tell the difference between a command (like `print`) and a piece of text (a string)?
- We used double quotes (`""`). Try running `print('Hello, World!')` with single quotes (`''`). Does it work? What does this tell you about creating strings in Python?
- What are some real-world examples where a program might need to display text output to a user?

---

## Section 6: Storing Information: Variables

### Learning Objectives
- Define 'variable' as a named container for storing data.
- Correctly use the assignment operator (`=`) to store a value in a variable.
- Use the `print()` function to display the value stored in a variable.
- Understand that the value of a variable can be updated or changed.

### Assessment Questions

**Question 1:** What is the primary purpose of a variable in programming?

  A) To perform a mathematical calculation.
  B) To store a value in memory with a memorable name.
  C) To stop the program from running.
  D) To print text directly to the screen.

**Correct Answer:** B
**Explanation:** Variables act as named containers or labels for data, allowing us to store information (like numbers or text) and refer to it later using its name.

**Question 2:** Which of the following lines of code correctly assigns the number 42 to a variable named `answer`?

  A) 42 = answer
  B) answer = 42
  C) answer == 42
  D) let answer = 42

**Correct Answer:** B
**Explanation:** The correct syntax for assignment is `variable_name = value`. The value on the right is stored in the variable on the left. `42 = answer` is incorrect because you cannot assign a value to a number.

**Question 3:** What will be the output of the following Python code?

`pet = "Cat"
pet = "Dog"
print(pet)`

  A) Cat
  B) Dog
  C) CatDog
  D) The code will produce an error.

**Correct Answer:** B
**Explanation:** Variables can be updated. The code first assigns 'Cat' to `pet`, but the next line re-assigns 'Dog' to the same variable. The original value is replaced, so `print(pet)` outputs the most recent value, which is 'Dog'.

**Question 4:** In the statement `score = 100`, the single equals sign (`=`) is known as the:

  A) Equality operator
  B) Comparison operator
  C) Assignment operator
  D) Execution operator

**Correct Answer:** C
**Explanation:** The `=` symbol is the assignment operator. Its job is to take the value from the right side and store it in the variable on the left side. It is different from the mathematical 'equals' sign.

### Activities
- Declare a variable called `planet_name` and assign it the string value "Earth". On the next line, use the `print()` function to display the value of this variable.
- Create a variable `current_year` and assign it the number `2024`. Print a message like 'The current year is: ' followed by the variable's value. Then, update the variable to `2025` and print it again to see the change.
- Create two variables: `first_name` and `last_name`. Assign your own first and last name to them as string values. Write two `print()` statements to display each variable on a separate line.

### Discussion Questions
- Why is it more useful to use a variable name like `player_score` instead of just using the number `100` everywhere in a game's code?
- In the 'labeled box' analogy, what happens to the old item in the box when you put a new item in? How does this relate to updating a variable's value?
- Can you think of a real-world example (outside of programming) where you use a label to refer to something that can change? (e.g., 'today's special' on a menu board).

---

## Section 7: Data Type 1: Strings (str)

### Learning Objectives
- Define a string as a sequence of characters for representing text.
- Correctly create a string variable using either single or double quotes.
- Explain why having both single and double quotes is useful for including quotes within a string.
- Use the `+` operator to concatenate two or more strings.

### Assessment Questions

**Question 1:** Which of the following is NOT a valid way to create a string in Python?

  A) `city = 'New York'`
  B) `country = "Canada"`
  C) `planet = Mars`
  D) `motto = "It's a wonderful day"`

**Correct Answer:** C
**Explanation:** Strings must be enclosed in either single ('') or double ("") quotes. Without quotes, Python will interpret `Mars` as a variable name, which will cause an error if it hasn't been defined.

**Question 2:** What is the output of the following Python code?
`first = "Ada"
last = "Lovelace"
print(first + last)`

  A) `Ada Lovelace`
  B) `AdaLovelace`
  C) `Ada + Lovelace`
  D) The code will produce an error.

**Correct Answer:** B
**Explanation:** The `+` operator, when used with strings, performs concatenation, which joins the strings directly end-to-end. It does not automatically add a space.

**Question 3:** Which line of code correctly creates a string that contains double quotes inside it?

  A) `quote = "She said, "Hello!""`
  B) `quote = 'She said, "Hello!"'`
  C) `quote = 'She said, 'Hello!''`
  D) `quote = She said, "Hello!"`

**Correct Answer:** B
**Explanation:** To include a double quote character inside a string, the entire string must be enclosed in single quotes. Using the same type of quote for both the outer container and inner content will result in a syntax error.

**Question 4:** The process of joining two strings together using the `+` operator is known as:

  A) Addition
  B) Combination
  C) Concatenation
  D) Stringification

**Correct Answer:** C
**Explanation:** Concatenation is the technical term for joining sequences, such as strings, end-to-end.

### Activities
- In a code cell, create two string variables: `first_name` and `last_name`. Assign your first and last names to them. Print each variable on a separate line.
- Using the variables from the previous activity, create a third variable called `full_name` by concatenating `first_name`, a literal space string (`" "`), and `last_name`. Print the `full_name` variable to see the complete name.
- Create a variable called `favorite_food` and assign it a string like `'My favorite food is "pizza"'`. The string should use single quotes on the outside and include the name of your favorite food in double quotes on the inside. Print the variable.

### Discussion Questions
- Why do you think Python offers two different ways (single and double quotes) to create strings? What problem does this solve?
- What might happen if you try to add a string and a number, like `'Age: ' + 25`? Why do you think that would be the result?
- Can you think of some real-world examples from websites or apps you use where strings are essential? (e.g., usernames, comments, search queries).

---

## Section 8: Data Type 2: Integers (int)

### Learning Objectives
- Define an integer as a positive, negative, or zero whole number.
- Correctly identify and create integer variables in Python.
- Recognize common use cases for integers, such as counting items or tracking scores.
- Differentiate between standard division (`/`), integer division (`//`), and the modulo operator (`%`) and apply them correctly.

### Assessment Questions

**Question 1:** Which of the following values would be stored as an integer (`int`) data type in Python?

  A) `98.6`
  B) `-50`
  C) `'100'`
  D) `"-25"`

**Correct Answer:** B
**Explanation:** An integer is a whole number without a fractional part. `98.6` is a float because it has a decimal. `'100'` and `"-25"` are strings because they are enclosed in quotes. `-50` is a whole number (negative) and is therefore an integer.

**Question 2:** What is the result of the Python expression `15 // 4`?

  A) `3.75`
  B) `3`
  C) `4`
  D) `Error`

**Correct Answer:** B
**Explanation:** The integer division operator `//` divides the numbers and discards any fractional part (it rounds down to the nearest whole number). 15 divided by 4 is 3.75, and discarding the decimal part leaves 3.

**Question 3:** A team has 20 cookies to share equally among 6 members. Which Python expression correctly calculates how many cookies are left over?

  A) `20 / 6`
  B) `20 // 6`
  C) `20 * 6`
  D) `20 % 6`

**Correct Answer:** D
**Explanation:** The modulo operator `%` is used to find the remainder of a division. `20 // 6` would give 3 (the number of cookies each person gets), but `20 % 6` gives 2, which is the number of cookies left over.

**Question 4:** Which of the following scenarios is BEST suited for using an integer data type?

  A) Storing the price of a coffee, like `$3.50`.
  B) Storing a user's name.
  C) Counting the number of pages in a book.
  D) Storing the average rainfall for a month.

**Correct Answer:** C
**Explanation:** Counting pages involves whole numbers, which is the primary purpose of integers. Prices and averages often require decimal points (floats), and names are text (strings).

### Activities
- Create a variable named `birth_year` and assign your year of birth to it. Create a second variable named `current_year` and assign the current year. Calculate your approximate age by subtracting `birth_year` from `current_year` and store it in a variable called `age`. Print the `age` variable.
- Declare an integer variable `total_items = 117` and another variable `box_capacity = 8`. Use integer division and the modulo operator to calculate and print how many full boxes you can pack and how many items will be left over. The output should be user-friendly, like: 'Number of full boxes: ...' and 'Items left over: ...'.

### Discussion Questions
- Why do you think Python has two different division operators (`/` and `//`)? Can you think of a real-world scenario where you would specifically need the result of `//`?
- The slide mentions that Python integers have 'unlimited precision.' What do you think this means, and how might it be an advantage over other programming languages or calculators that have a fixed limit on number size?
- If you ask a user to input their age, the input is often read as a string (e.g., `'25'`) instead of an integer (`25`). What problems could arise if you tried to perform math with the string version?

---

## Section 9: Data Type 3: Floats (float)

### Learning Objectives
- Define a float as a number containing a decimal point.
- Identify real-world scenarios where a float is more appropriate than an integer.
- Correctly declare and initialize a float variable in code.
- Understand the purpose of floats for representing values that require fractional precision.

### Assessment Questions

**Question 1:** A programmer needs to store a student's Grade Point Average (GPA), which is 3.75. Which data type is most appropriate?

  A) String (str)
  B) Integer (int)
  C) Float (float)
  D) Boolean (bool)

**Correct Answer:** C
**Explanation:** Because the value 3.75 contains a decimal point, a float is the correct data type. An integer can only store whole numbers, and a string would store it as text, preventing mathematical calculations.

**Question 2:** Which of the following values would be stored as a `float` in a programming language like Python?

  A) 42
  B) "42.0"
  C) 42.0
  D) True

**Correct Answer:** C
**Explanation:** A float is a number that contains a decimal point. `42` is an integer, `"42.0"` is a string, and `True` is a boolean. Only `42.0` is a floating-point number.

**Question 3:** What is the primary purpose of using a `float` data type instead of an `int`?

  A) To store very large numbers
  B) To represent numbers with fractional precision
  C) To store text and numbers together
  D) To make the code run faster

**Correct Answer:** B
**Explanation:** The main distinction and purpose of floats is their ability to represent numbers with decimal points, which is essential for fractional precision in measurements, prices, and calculations.

**Question 4:** Which of the following lines of code correctly creates a float variable named `item_price`?

  A) item_price = "9.99"
  B) item_price = 9,99
  C) item_price = 9.99
  D) item_price = float(9-99)

**Correct Answer:** C
**Explanation:** The correct syntax for assigning a float value is to use a decimal point (`.`). Option A creates a string, Option B uses a comma which is not valid syntax for a float literal, and Option D is an incorrect use of the `float()` function.

### Activities
- Create a variable called `pi_approx` and assign it the value `3.14159`. Print the variable and its data type using the `type()` function.
- Declare two float variables, `length` with a value of `12.5` and `width` with a value of `5.5`. Calculate the area (`length * width`) and store it in a new variable called `area`. Print the value of `area`.
- Create a variable `account_balance` and assign it the value `1500`. Then, update the balance by adding `75.50` in interest. Print the new balance.

### Discussion Questions
- Besides prices or GPA, what are three other real-world examples where a float would be necessary? Why wouldn't an integer work in those cases?
- What do you think might happen if you perform a mathematical operation between a float and an integer (e.g., `5 + 2.5`)? What would the data type of the result be, and why?
- Could you store a whole number like `10` in a float variable (e.g., `x = 10.0`)? What are the potential advantages or disadvantages of doing this?

---

## Section 10: Chapter 1 Recap and Next Steps

### Learning Objectives
- Recall the definitions of a program, algorithm, and variable.
- Identify and differentiate between three fundamental data types: string, integer, and float.
- Demonstrate the correct syntax for variable assignment using the `=` operator.
- Synthesize learned concepts to write a short, multi-line Python script that stores and displays data using the `print()` function.

### Assessment Questions

**Question 1:** What is the key difference between an algorithm and a program?

  A) An algorithm is the code written in a language like Python, while a program is the abstract plan.
  B) An algorithm is the logical set of steps to solve a problem, while a program is the implementation of that algorithm in code.
  C) There is no difference; the terms are interchangeable in programming.
  D) A program uses variables and functions, whereas an algorithm is only a flowchart.

**Correct Answer:** B
**Explanation:** An algorithm is the 'recipe' or logical plan. A program is the concrete set of instructions written in a specific programming language to execute that plan. The program is the implementation of the algorithm.

**Question 2:** Examine the following code:
```python
item_name = "Laptop"
quantity = 15
price = 1299.99
```
What are the data types of `item_name`, `quantity`, and `price` respectively?

  A) string, float, integer
  B) string, integer, float
  C) integer, string, float
  D) float, string, integer

**Correct Answer:** B
**Explanation:** `item_name` holds textual data in quotes, making it a string. `quantity` is a whole number, making it an integer. `price` contains a decimal point, making it a float.

**Question 3:** Which code snippet contains a syntax error that will prevent it from running?

  A) `user_age = 25`\n`print("Age:", user_age)`
  B) `course_name = "Intro to Python"`
  C) `book_price: 19.99`\n`print(book_price)`
  D) `item_count = 100`

**Correct Answer:** C
**Explanation:** Option C uses a colon (`:`) for assignment instead of the correct equals sign (`=`). This is invalid syntax in Python for variable assignment and will cause an error. The other options show correct syntax for creating variables and printing.

**Question 4:** A fellow student writes the following code, but it doesn't work as expected. Why?
```python
student_name = "Maria"
print(Student_Name)
```

  A) The `print()` function cannot be used with strings.
  B) Python variable names cannot contain underscores.
  C) The variable `student_name` should not be in quotes.
  D) Python variables are case-sensitive, and `student_name` is different from `Student_Name`.

**Correct Answer:** D
**Explanation:** Python is case-sensitive. The variable was created as `student_name` (all lowercase), but the `print()` function tries to access `Student_Name` (with capital letters). The program will fail because `Student_Name` has not been defined.

### Activities
- Create a 'Chapter 1 Summary' Colab notebook. In it, add a single code cell that accomplishes the following: 1. Creates a string variable for the name of your favorite book. 2. Creates an integer variable for the year it was published. 3. Creates a float variable for its price. 4. Uses the `print()` function to display all three pieces of information with descriptive labels (e.g., `print("Title:", book_title)`).

### Discussion Questions
- Think about a simple daily task you do, like making coffee or toast. Can you describe the 'algorithm' for it in plain English? What would make it a 'program'?
- Why is it important for a programming language to have different data types? What problems might occur if we only had one type of data (e.g., everything was treated as text)?
- Looking at the 'Next Steps', how might combining calculations (like addition) and user input make our programs more useful and interactive? Can you brainstorm a simple example?

---

