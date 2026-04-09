# Assessment: Slides Generation - Chapter 9: Data Structures II: Dictionaries

## Section 1: Chapter 9: Data Structures II: Dictionaries

### Learning Objectives
- Articulate the primary limitation of lists for non-sequential data retrieval.
- Define a dictionary as an unordered collection of key-value pairs.
- Explain why a dictionary provides a more efficient and readable lookup method than iterating through a list for specific data-modeling scenarios.
- Identify the core topics to be covered in the chapter, including dictionary operations, iteration, and applications.

### Assessment Questions

**Question 1:** Based on the slide, what is the primary inefficiency of using a list of lists (e.g., `[['Alice', 95], ...]`) to store and retrieve student grades by name?

  A) Lists cannot store both strings and numbers at the same time.
  B) You must iterate through the list to find a specific name, which is slow for large datasets.
  C) Lists are ordered, which makes it difficult to add new students.
  D) A list uses more memory than a dictionary for the same amount of data.

**Correct Answer:** B
**Explanation:** The key problem highlighted is performance. To find an element by its content (like a name) rather than its index, you have to perform a search operation, which can be very slow as the list grows.

**Question 2:** What fundamental concept allows a dictionary to provide 'instant lookup' of a value?

  A) It stores values in a sorted, alphabetical order.
  B) It uses a numeric index just like a list.
  C) It maps a unique key directly to its associated value.
  D) It pre-calculates the location of every possible value.

**Correct Answer:** C
**Explanation:** The power of a dictionary comes from its key-value pair structure. The key acts as a unique identifier that allows Python to directly and efficiently locate the corresponding value without searching.

**Question 3:** In the dictionary `grades_dict = {'Alice': 95, 'Bob': 87}`, what is the 'key' and what is the 'value' in the first pair?

  A) Key: 0, Value: 'Alice'
  B) Key: 95, Value: 'Alice'
  C) Key: 'Alice', Value: 95
  D) Key: 'grades_dict', Value: {'Alice': 95}

**Correct Answer:** C
**Explanation:** In a dictionary, each item consists of a key and a value. The key comes before the colon (':'), and the value comes after. In this case, 'Alice' is the key used to look up the value 95.

**Question 4:** You need to store the capital city for each country in the world. Which data structure would be most appropriate and why?

  A) A list, because the order of countries is important.
  B) A dictionary, using the country name as the key and the capital city as the value.
  C) A list of lists, as it is the simplest way to pair two pieces of information.
  D) A dictionary, using a numeric index (0, 1, 2...) as the key for each country.

**Correct Answer:** B
**Explanation:** This is a perfect use case for a dictionary. You want to look up a capital (value) by its country name (key). Using a dictionary provides a direct, readable, and efficient way to model this relationship.

### Activities
- Think-Pair-Share: Think about an app on your phone (e.g., Contacts, Spotify, a game). Where might it be using a dictionary-like structure? For example, in your Contacts app, your friend's name (the key) maps to their phone number (the value). Share your example with a partner.
- Whiteboard Challenge: As a class, let's model a simple product inventory. We have 'apples' (cost: 0.50), 'milk' (cost: 3.00), and 'bread' (cost: 2.50). How would we represent this data in a Python dictionary? Write the code on the board.

### Discussion Questions
- The slide mentions dictionaries are 'unordered'. What do you think that means, and why might that be an important distinction from lists?
- Besides student grades and product inventories, what are two other real-world examples where a key-value relationship is a natural way to model the data?
- Looking at the two code snippets (list search vs. dictionary lookup), which one is easier to read and understand at a glance? Why does code readability matter?

---

## Section 2: What is a Dictionary? The Key-Value Pair

### Learning Objectives
- Define a dictionary as an unordered collection of key-value pairs.
- Distinguish between a dictionary (accessed by key) and a list (accessed by index).
- Explain the rule that dictionary keys must be unique.
- Identify keys and values in real-world analogies like phonebooks or user profiles.

### Assessment Questions

**Question 1:** Which of the following statements is a fundamental rule for dictionary keys?

  A) Keys must be integers.
  B) Keys must be unique.
  C) Keys and values must be the same data type.
  D) Keys can be duplicated within the same dictionary.

**Correct Answer:** B
**Explanation:** The defining rule for keys in a dictionary is that each key must be unique to ensure a one-to-one mapping to its value. Attempting to add a duplicate key will update the existing entry's value.

**Question 2:** How does data access in a dictionary differ from a list?

  A) A dictionary is an ordered collection, while a list is unordered.
  B) A dictionary uses unique keys for access, while a list uses ordered numerical indices.
  C) A dictionary can store different data types, while a list cannot.
  D) Accessing data in a dictionary is always slower than in a list.

**Correct Answer:** B
**Explanation:** The core difference lies in their access method. Lists are sequences accessed by an integer index (0, 1, 2...), whereas dictionaries are mappings accessed by a user-defined, unique key.

**Question 3:** In a dictionary representing a user profile with `{'username': 'alex_c', 'user_id': 101, 'is_active': True}`, what is the value associated with the key `'user_id'`?

  A) 'user_id'
  B) 101
  C) 'alex_c'
  D) True

**Correct Answer:** B
**Explanation:** The dictionary is made of key-value pairs. For the pair `'user_id': 101`, the key is the string `'user_id'` and its corresponding value is the integer `101`.

**Question 4:** If you attempt to add a new key-value pair to a dictionary but the key already exists, what will happen?

  A) The dictionary will raise an error.
  B) The new key-value pair will be added, resulting in duplicate keys.
  C) The value associated with the existing key will be updated to the new value.
  D) The new key-value pair will be ignored.

**Correct Answer:** C
**Explanation:** Dictionaries do not allow duplicate keys. If you assign a value to a key that is already in the dictionary, you are simply overwriting or updating the old value with the new one.

### Activities
- On paper or in a text editor, design a dictionary to represent a single item in an online store. Include keys like `'product_id'`, `'name'`, `'price'`, and `'in_stock'`. Fill in example values for a fictional product.
- Review the following set of key-value pairs intended for a single dictionary: `('name', 'Alice')`, `('id', 123)`, `('department', 'Sales')`, `('name', 'Bob')`. Identify the conceptual error based on the rules of dictionaries and explain why it's a problem.

### Discussion Questions
- Why is it essential for dictionary keys to be unique? What kind of confusion or errors would occur in a student record system if Student IDs (the keys) were not unique?
- Brainstorm other real-world examples of key-value pairs not mentioned on the slide. For each example, identify the key and the value.
- Can you think of a situation where using a list would be more appropriate than a dictionary? Conversely, when is a dictionary clearly the better choice?

---

## Section 3: Syntax: Creating a Dictionary

### Learning Objectives
- Identify the correct syntax for initializing a dictionary.
- Recognize the use of curly braces `{}`, colons `:`, and commas `,` in dictionary creation.
- Differentiate between valid and invalid dictionary keys based on the principle of immutability.
- Understand that dictionary values can be of any data type, including other collections like lists.

### Assessment Questions

**Question 1:** Which of the following lines of code correctly creates a Python dictionary?

  A) `my_dict = ['name': 'Alice', 'age': 30]`
  B) `my_dict = ('name', 'Alice', 'age', 30)`
  C) `my_dict = {'name': 'Alice', 'age': 30}`
  D) `my_dict = {'name' = 'Alice', 'age' = 30}`

**Correct Answer:** C
**Explanation:** Dictionaries are created using curly braces `{}`, with key-value pairs separated by a colon `:` and each pair separated by a comma `,`.

**Question 2:** Which of the following data types is NOT a valid key for a Python dictionary?

  A) A string (e.g., 'city')
  B) An integer (e.g., 404)
  C) A tuple (e.g., (10, 20))
  D) A list (e.g., ['first_name', 'last_name'])

**Correct Answer:** D
**Explanation:** Dictionary keys must be of an immutable type. Lists are mutable (their contents can be changed), so they cannot be used as keys. Strings, integers, and tuples are all immutable.

**Question 3:** In the `user_profile` example, what is the data type of the value associated with the key `'topics'`?

  A) String
  B) List
  C) Dictionary
  D) Boolean

**Correct Answer:** B
**Explanation:** The value `['python', 'data', 'design']` is enclosed in square brackets, which defines a list in Python. This demonstrates that dictionary values can be complex data structures.

**Question 4:** How do you create an empty dictionary named `data`?

  A) `data = []`
  B) `data = ()`
  C) `data = empty_dict()`
  D) `data = {}`

**Correct Answer:** D
**Explanation:** An empty dictionary is created using a pair of empty curly braces `{}`. `[]` creates an empty list, and `()` creates an empty tuple.

### Activities
- Live Coding: Create a Python dictionary named `student` to store the following information: `name` as a string, `student_id` as an integer, and `courses_enrolled` as a list of strings (e.g., ['Math', 'History']).
- Code Correction: The following code has two syntax errors. Identify and fix them to create a valid dictionary.
`book_info = { 'title' = 'Python Basics', ['year']: 2023 }`

### Discussion Questions
- Why do you think Python requires dictionary keys to be immutable? What problems might occur if you could change a key after it was created?
- Can you think of a real-world example (other than a user profile) where a dictionary would be a more useful data structure than a list? Why?
- In the `user_profile` example, the value for 'topics' is a list. Could it have been a tuple instead? What would be the practical difference in that case?

---

## Section 4: Accessing Values

### Learning Objectives
- Demonstrate how to retrieve a value from a dictionary using its key and square bracket notation.
- Predict and explain what a `KeyError` is and when it occurs.
- Differentiate between dictionary key-based lookup and list index-based access.
- Apply chaining of accessors to retrieve items from nested structures (e.g., an item in a list that is a dictionary value).

### Assessment Questions

**Question 1:** Given the dictionary `user_profile = {'username': 'alex_c', 'user_id': 101}`, what is the result of `print(user_profile['user_id'])`?

  A) `username`
  B) `101`
  C) `KeyError`
  D) `alex_c`

**Correct Answer:** B
**Explanation:** Accessing a value in a dictionary is done by placing the key inside square brackets `[]`. The key `'user_id'` corresponds to the value `101`.

**Question 2:** What happens if you try to access a key that does not exist in a dictionary, such as `user_profile['email']`?

  A) The program returns `None`.
  B) The program returns an empty string `''`.
  C) The program crashes with a `KeyError`.
  D) The program crashes with an `IndexError`.

**Correct Answer:** C
**Explanation:** Attempting to access a non-existent key with square bracket notation will raise a `KeyError`. This is a runtime error indicating the key was not found.

**Question 3:** Given `user_profile = {'topics': ['python', 'data', 'design']}`, how would you access the first topic, 'python'?

  A) `user_profile['topics', 0]`
  B) `user_profile[0]['topics']`
  C) `user_profile('topics')[0]`
  D) `user_profile['topics'][0]`

**Correct Answer:** D
**Explanation:** First, `user_profile['topics']` accesses the list `['python', 'data', 'design']`. Then, `[0]` is used to index into that list to retrieve the first element.

**Question 4:** Which of the following lines of code will fail with a `KeyError`? Assume `config = {'theme': 'dark', 'version': 1.2}`.

  A) `print(config['theme'])`
  B) `print(config['version'])`
  C) `print(config['Theme'])`
  D) `value = config['theme']`

**Correct Answer:** C
**Explanation:** Dictionary keys are case-sensitive. Since the key is `'theme'` (lowercase), trying to access `'Theme'` (uppercase) will result in a `KeyError` because that specific key does not exist.

### Activities
- {'type': 'code_completion', 'description': 'Code Snippet Analysis: Given the `user_profile` dictionary from the slide, write the single line of Python code required to access the list of topics and store it in a variable called `my_topics`.', 'solution': "my_topics = user_profile['topics']"}
- {'type': 'debugging', 'description': "Fix the Code: The following code is intended to print the user's active status but it fails. Identify the error and correct the second line.", 'code': "user_status = {'is_active': True, 'last_login': '2023-10-27'}\nprint(user_status[is_active])", 'solution': "print(user_status['is_active'])", 'explanation': "The key is the string literal `'is_active'`, not a variable named `is_active`. Keys must be referenced exactly as they are defined, including quotes for strings."}
- {'type': 'predict_output', 'description': "Predict the Error: What specific error will the following code produce? `settings = {'font_size': 12}; print(settings['font size'])`", 'solution': 'KeyError', 'explanation': "The code will produce a `KeyError`. The defined key is `'font_size'` without a space, but the code attempts to access `'font size'` with a space. These are treated as two different keys."}

### Discussion Questions
- Why is raising a `KeyError` often more useful for a programmer than silently returning `None` when a key isn't found? What are the advantages of this 'fail-fast' approach?
- In what real-world data scenarios would using a dictionary with descriptive string keys be more advantageous than using a list with integer indices?
- If a dictionary key happens to be an integer, like in `data = {101: 'alex_c'}`, is `data[101]` an index or a key? How is this fundamentally different from how a list works?

---

## Section 5: Adding and Updating Items

### Learning Objectives
- Utilize square bracket assignment (`dictionary[key] = value`) to add a new key-value pair to a dictionary.
- Employ the same square bracket assignment syntax to modify the value of a pre-existing key.
- Distinguish between assignment to a non-existent key (which creates it) and accessing a non-existent key (which raises a KeyError).
- Predict the final state of a dictionary after a series of add and update operations.

### Assessment Questions

**Question 1:** If `user_profile = {'username': 'alex_c', 'is_active': True}`, what does the code `user_profile['is_active'] = False` do?

  A) It adds a new key `'is_active'` with the value `False`.
  B) It updates the value of the existing key `'is_active'` to `False`.
  C) It raises a `KeyError` because the key already exists.
  D) It creates an entirely new dictionary.

**Correct Answer:** B
**Explanation:** The square bracket assignment syntax is used for both adding and updating. Since the key 'is_active' already exists, its corresponding value is updated from `True` to `False`.

**Question 2:** You have a dictionary `student = {'name': 'Eva', 'id': 205}`. Which line of code correctly adds her major as 'Physics'?

  A) `student.add('major', 'Physics')`
  B) `student['major'] = 'Physics'`
  C) `add to student: 'major': 'Physics'`
  D) The dictionary must be recreated to add new items.

**Correct Answer:** B
**Explanation:** To add a new key-value pair, you use the assignment operator with the new key in square brackets. Since 'major' does not exist, this operation creates it.

**Question 3:** What is the final state of `data` after the following code is executed? 
`data = {'a': 1, 'b': 2}`
`data['c'] = 3`
`data['a'] = 100`

  A) `{'a': 1, 'b': 2, 'c': 3}`
  B) `{'a': 100, 'b': 2, 'c': 3}`
  C) `{'a': 1, 'b': 2, 'a': 100}`
  D) The code will raise an error because 'a' is assigned twice.

**Correct Answer:** B
**Explanation:** The line `data['c'] = 3` adds a new key-value pair. The line `data['a'] = 100` finds the existing key 'a' and updates its value from 1 to 100. Keys in a dictionary must be unique.

**Question 4:** Which statement best describes the behavior of `my_dict[key] = value` in Python?

  A) It only adds new key-value pairs and will error if the key exists.
  B) It only updates existing values and will error if the key does not exist.
  C) It checks if the key exists. If it does, it updates the value; otherwise, it adds a new key-value pair.
  D) It always deletes the old dictionary and creates a new one with the modification.

**Correct Answer:** C
**Explanation:** This "upsert" (update/insert) behavior is a core feature of dictionary assignment. The same syntax intelligently handles both adding new items and modifying existing ones.

### Activities
- **Build a Profile:** Start with an empty dictionary: `my_profile = {}`. Write separate lines of code to add your name, your favorite programming language, and your city. Print the final dictionary to check your work.
- **Inventory Management:** Given the dictionary `inventory = {'apples': 100, 'oranges': 50}`. Write Python code to: 1. Update the count of 'apples' to 95. 2. Add a new fruit, 'bananas', with a count of 200. Print the `inventory` dictionary after your changes.
- **Spot the Typo:** Predict the output of the following code and explain why it happens: `settings = {'font': 'Arial', 'size': 12}; settings['sise'] = 14; print(settings)`. This demonstrates a common pitfall.

### Discussion Questions
- Why do you think Python's designers chose to use the same syntax for both adding and updating dictionary items? What are the pros and cons of this approach?
- Imagine you are building a system to count the frequency of words in a document. How would the 'add or update' behavior of dictionaries be essential for this task?
- What is a potential bug that could be introduced by this 'upsert' behavior? (Hint: think about what happens if you misspell a key name when you intend to *update* a value).

---

## Section 6: Removing Items

### Learning Objectives
- Correctly use the `del` keyword to remove a specified key-value pair.
- Predict the state of a dictionary after a `del` operation.
- Identify and anticipate a `KeyError` when attempting to delete a non-existent key.
- Distinguish between the `del` keyword and the `.pop()` method and understand their respective use cases.

### Assessment Questions

**Question 1:** Which keyword is used to remove a specific key-value pair from a dictionary?

  A) `remove`
  B) `pop`
  C) `del`
  D) `erase`

**Correct Answer:** C
**Explanation:** The `del` keyword followed by the dictionary and the key in square brackets (e.g., `del my_dict['key']`) is the standard way to permanently remove a key-value pair.

**Question 2:** What happens if you try to use `del` to remove a key that does not exist in a dictionary?

  A) The dictionary remains unchanged and no error occurs.
  B) A `ValueError` is raised.
  C) A `KeyError` is raised.
  D) The program creates the key with a `None` value.

**Correct Answer:** C
**Explanation:** Attempting to delete a non-existent key with the `del` keyword will result in a `KeyError`, which can crash the program if not handled properly.

**Question 3:** Consider the following code:
`user_profile = {'username': 'alex_c', 'email': 'alex@example.com'}`
`del user_profile['username']`
What is the value of `user_profile` after this code is executed?

  A) `{'username': 'alex_c', 'email': 'alex@example.com'}`
  B) `{'email': 'alex@example.com'}`
  C) `{'username': None, 'email': 'alex@example.com'}`
  D) `None`

**Correct Answer:** B
**Explanation:** The `del` keyword removes the specified key-value pair ('username': 'alex_c') directly from the dictionary, leaving only the remaining pairs.

**Question 4:** What is the primary difference between using the `del` keyword and the `.pop()` method to remove an item from a dictionary?

  A) `del` can remove multiple keys at once, while `.pop()` can only remove one.
  B) `.pop()` removes an item and returns its value, while `del` just removes the item.
  C) `del` is safer and will not raise an error for a missing key, unlike `.pop()`.
  D) There is no functional difference; they are interchangeable.

**Correct Answer:** B
**Explanation:** The key distinction is that `.pop()` is a method that both removes the key-value pair and returns the corresponding value, which can then be stored in a variable. `del` is a statement that only performs the deletion and returns nothing.

### Activities
- **Code Writing:** Given the dictionary `car = {'make': 'Ford', 'model': 'Mustang', 'year': 2022}`, write the single line of code that would remove the 'year' key-value pair.
- **Debugging:** The following code snippet is intended to remove the 'age' key from a dictionary, but it causes an error. Identify the error, explain why it happens, and rewrite the code to safely remove the key only if it exists. 
`student = {'name': 'Jordan', 'major': 'Physics'}`
`del student['age']`
- **Concept Application:** Given the dictionary `settings = {'theme': 'dark', 'font_size': 14, 'show_notifications': True}`, write a script that removes the 'font_size' key and stores its value (14) in a variable named `previous_font_size` using the most appropriate method.

### Discussion Questions
- When would you choose to use the `.pop()` method over the `del` keyword in a real-world application? Can you provide a specific scenario?
- What are some strategies to prevent your program from crashing with a `KeyError` when you need to delete items that may or may not exist in a dictionary?
- The `del` keyword modifies a dictionary 'in-place'. What does 'in-place modification' mean, and why is it an important concept to understand when working with data structures?

---

## Section 7: Iterating Through a Dictionary

### Learning Objectives
- Iterate through the keys of a dictionary using a standard `for` loop.
- Use the `.items()` method to efficiently iterate through both keys and values together.
- Use the `.values()` method to iterate through only the values of a dictionary.
- Apply dictionary iteration to perform calculations and filter data based on keys or values.

### Assessment Questions

**Question 1:** To loop through both the keys and values of a dictionary `d` simultaneously, which syntax is most appropriate?

  A) `for item in d:`
  B) `for key, value in d.items():`
  C) `for value in d.values():`
  D) `for i in range(len(d)):`

**Correct Answer:** B
**Explanation:** The `.items()` method returns a view object that displays a list of a dictionary's key-value tuple pairs. This allows you to conveniently unpack both the key and value in each iteration of a for loop.

**Question 2:** What is the output of the following code snippet?

```python
config = {'host': 'localhost', 'port': 8080}
for setting in config:
    print(setting)
```

  A) `localhost`, `8080`
  B) `('host', 'localhost')`, `('port', 8080)`
  C) `host`, `port`
  D) An error will occur.

**Correct Answer:** C
**Explanation:** By default, iterating over a dictionary in a `for` loop provides access to its keys. The loop variable `setting` will be assigned the keys 'host' and 'port' in sequence.

**Question 3:** If you only need to process the values in a dictionary and do not need the keys, which method is the most direct and efficient?

  A) `my_dict.keys()`
  B) `my_dict.items()`
  C) `my_dict.values()`
  D) `for key in my_dict: print(my_dict[key])`

**Correct Answer:** C
**Explanation:** The `.values()` method returns a view object containing only the values from the dictionary, making it the most direct way to iterate when keys are not needed.

**Question 4:** Which code snippet correctly prints only the keys associated with boolean `True` values in the `user_profile` dictionary?

`user_profile = {'username': 'alex_c', 'is_active': True, 'email_verified': True}`

  A) `for key, value in user_profile.items():
    if value == True:
        print(key)`
  B) `for key in user_profile:
    if key == True:
        print(key)`
  C) `for value in user_profile.values():
    if value == True:
        print(value)`
  D) `for key, value in user_profile:
    if value == True:
        print(key)`

**Correct Answer:** A
**Explanation:** This option correctly uses `.items()` to get both the key and value. The `if` statement then checks if the `value` is `True`, and if so, prints the corresponding `key`. The other options either iterate incorrectly or check the wrong variable.

### Activities
- Code Writing: Given the `user_profile` dictionary, write a `for` loop using `.items()` that prints each key and its corresponding value in the format 'Key -> Value' (e.g., 'username -> alex_c').
- Problem Solving: You are given a dictionary `inventory = {'apples': 50, 'bananas': 25, 'oranges': 30}`. Write a Python script that iterates through the dictionary to calculate and print the total number of fruits in the inventory.
- Code Refactoring: The following code works, but it is not the most 'Pythonic' way. Refactor it to use the `.items()` method for better readability and efficiency.

```python
user_profile = {'username': 'alex_c', 'is_active': True}
for key in user_profile.keys():
    value = user_profile[key]
    print(f'{key}: {value}')
```

### Discussion Questions
- In what real-world scenario would you prefer to iterate over only the values of a dictionary using `.values()` instead of the keys or key-value pairs?
- The `.items()` method is often described as more efficient than looping through keys and looking up the value with `my_dict[key]` inside the loop. Why do you think that is?
- Imagine you have a dictionary where the values are lists, like `{'students': ['Alice', 'Bob'], 'teachers': ['Mr. Smith']}`. How would you write a nested loop to print every person's name from this dictionary?

---

## Section 8: Checking for Keys

### Learning Objectives
- Explain what causes a `KeyError` and why it's important to prevent it.
- Use the `in` keyword to verify the existence of a key in a dictionary.
- Use the `not in` keyword to verify the absence of a key.
- Write robust conditional logic (`if/else`) to safely access dictionary data and handle cases where keys may be missing.

### Assessment Questions

**Question 1:** What is the primary purpose of using the `in` keyword with a dictionary in Python?

  A) To check if a specific value exists in the dictionary.
  B) To iterate through all the key-value pairs.
  C) To check if a specific key exists in the dictionary.
  D) To retrieve the value associated with a key.

**Correct Answer:** C
**Explanation:** The `in` keyword is used to test for membership within a dictionary's keys. It returns `True` if the key is present and `False` otherwise, which is essential for preventing `KeyError`.

**Question 2:** Given the dictionary `config = {'mode': 'test', 'version': 2.1}`, what will the expression `'port' not in config` evaluate to?

  A) `True`
  B) `False`
  C) `None`
  D) It will raise a `KeyError`.

**Correct Answer:** A
**Explanation:** The `not in` operator checks for the absence of a key. Since the key 'port' does not exist in the `config` dictionary, the expression correctly evaluates to `True`.

**Question 3:** Which code snippet will safely print a user's `email` if it exists, and a default message if it does not?

  A) `print(user_profile['email'])`
  B) `if user_profile['email']: print(user_profile['email'])`
  C) `if 'email' in user_profile: print(user_profile['email']) else: print('Email not found')`
  D) `for key in user_profile: if key == 'email': print(key)`

**Correct Answer:** C
**Explanation:** This option correctly uses the `in` keyword to first check for the key's existence. It then accesses the value only if the check passes, and handles the alternative case with an `else` block, thus avoiding any potential `KeyError`.

**Question 4:** What is a `KeyError` in the context of Python dictionaries?

  A) An error that occurs when you try to assign an invalid value to a key.
  B) An error that occurs when you try to access a key that does not exist in the dictionary.
  C) An error that occurs when a dictionary key is not a string.
  D) An error that occurs when the `in` keyword is used incorrectly.

**Correct Answer:** B
**Explanation:** A `KeyError` is raised specifically when you use square bracket notation `[]` to access a key that is not present in the dictionary, causing the program to halt.

### Activities
- {'type': 'problem_solving', 'title': 'Safe Login Check', 'description': "Write a Python `if/else` block that checks if the key 'last_login' exists in the `user_profile` dictionary. If it does, print its value. If not, print 'User has never logged in.' Assume `user_profile` is a pre-existing dictionary."}
- {'type': 'code_refactoring', 'title': 'Fix the Crashing Code', 'description': 'You are given the following code: `car = {\'make\': \'Toyota\', \'model\': \'Camry\'}\nprint(f"Year: {car[\'year\']}")`. This code will crash if the \'year\' key is missing. Refactor it using the `in` keyword to print the car\'s year if available, or \'Year not specified\' otherwise.'}
- {'type': 'problem_solving', 'title': 'Checking Stock Status', 'description': "Given a dictionary `product = {'name': 'Laptop', 'price': 1200}`, write a script that checks for the key `'in_stock'`. If the key `'in_stock'` exists and its value is `True`, print 'Product is available'. If the key exists but its value is `False`, print 'Product is out of stock'. If the key does not exist at all, print 'Stock status unknown'."}

### Discussion Questions
- Besides preventing a program from crashing, what are other benefits of checking for a key's existence before using it? (e.g., providing default values, better user experience).
- Can you think of a real-world scenario, like processing data from a web form or an API, where some dictionary keys might be optional and checking for their existence is crucial?
- The `in` keyword checks for keys. How would you approach checking if a specific *value* exists within a dictionary's values?

---

## Section 9: When to Use a Dictionary vs. a List

### Learning Objectives
- Differentiate the primary use cases for lists and dictionaries.
- Choose the appropriate data structure for a given problem based on its requirements (ordered collection vs. key-value mapping).
- Explain the difference between accessing data by a numerical index (list) and by a unique key (dictionary).

### Assessment Questions

**Question 1:** You need to store a collection of user preferences, such as 'theme', 'language', and 'notifications', where you'll look them up by name. Which data structure is more suitable?

  A) A list, because the order of settings might matter.
  B) A dictionary, because you are mapping a setting name (key) to its value.
  C) Either a list or a dictionary would work equally well.
  D) A tuple, because settings should not be changed.

**Correct Answer:** B
**Explanation:** This is a perfect use case for a dictionary. You need to associate a specific name (the key, e.g., 'theme') with a value (e.g., 'dark'). A dictionary allows for fast, direct lookup by the setting's name, which is more intuitive and readable than accessing by a numerical index.

**Question 2:** A programmer needs to store the exact sequence of turns in a chess game. Which data structure is the best choice for this task?

  A) A dictionary, with turn numbers as keys.
  B) A list, because the order of the turns is the most important requirement.
  C) A set, to ensure no duplicate moves are recorded.
  D) A single string, with moves separated by commas.

**Correct Answer:** B
**Explanation:** The critical requirement is to maintain an ordered sequence of items (the turns). Lists are specifically designed for ordered collections where elements are accessed by their numerical position (index), making them the ideal choice.

**Question 3:** What is the primary way to access an element in a list versus a dictionary?

  A) List: by its key; Dictionary: by its numerical index.
  B) List: by its numerical index; Dictionary: by its key.
  C) Both are accessed using a numerical index.
  D) Both are accessed using a unique key.

**Correct Answer:** B
**Explanation:** As shown in the slide's examples, lists use zero-based numerical indices (e.g., `recipe_steps[1]`) for access, while dictionaries use unique keys (e.g., `app_settings['theme']`) to look up their associated values.

**Question 4:** You are creating a data structure to hold information about a single book: its title, author, and ISBN. Which of the following is the most appropriate and readable implementation?

  A) `book = ['The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565']`
  B) `book = {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'isbn': '9780743273565'}`
  C) `book = ('The Great Gatsby', 'author', '9780743273565')`
  D) It is not possible to store this combination of data in a single variable.

**Correct Answer:** B
**Explanation:** A dictionary is the best choice because it explicitly labels each piece of information (title, author, isbn). This makes the code self-documenting and eliminates ambiguity about what each value represents, unlike a list where you must remember that index 0 is the title, index 1 is the author, etc.

### Activities
- {'title': 'Data Structure Selection', 'description': 'For each of the following scenarios, decide whether a list or a dictionary is the more appropriate data structure. Write a short justification for your choice. \n1. A list of students waiting in a line for the cafeteria. \n2. The glossary of terms at the end of a textbook. \n3. The daily temperature readings for a month, recorded in order. \n4. The contact information (phone, email, address) for a single person.'}
- {'title': 'Code Implementation', 'description': "Choose one scenario from the 'Data Structure Selection' activity and write a small Python code snippet to implement it. For example, create a dictionary for the contact information and demonstrate how to access the person's email address."}

### Discussion Questions
- What problems would you encounter if you used a list to store the `app_settings` from the slide's example? How would you retrieve the `username`?
- Can you think of a real-world scenario where you might need a list of dictionaries? For example, a list of contacts where each contact is a dictionary of their details.
- The slide mentions a 'mental model' for each data structure. Why is it helpful to have a mental model (like a numbered list vs. a phone book) when programming?

---

## Section 10: Chapter Summary

### Learning Objectives
- Recall the syntax for creating dictionaries and performing core operations (add, access, update, delete).
- Explain the fundamental structure of a dictionary as a collection of key-value pairs.
- Identify the properties of valid dictionary keys (uniqueness and immutability).
- Distinguish between appropriate use cases for dictionaries versus other data structures like lists.

### Assessment Questions

**Question 1:** Which of the following statements about Python dictionaries is FALSE?

  A) They store data as key-value pairs.
  B) New items are added using syntax like `my_dict['new_key'] = 'new_value'`.
  C) They are created using square brackets `[]`.
  D) The `del` keyword is used to remove items by key.

**Correct Answer:** C
**Explanation:** Dictionaries are created using curly braces `{}`, while lists are created using square brackets `[]`. This is a fundamental syntax difference.

**Question 2:** Consider the code: `player = {'score': 100, 'level': 5}`. What is the effect of the statement `player['score'] = 150`?

  A) It adds a new key 'score' with the value 150.
  B) It raises an error because the key 'score' already exists.
  C) It updates the existing value for the key 'score' to 150.
  D) It creates an entirely new dictionary named 'player'.

**Correct Answer:** C
**Explanation:** When you assign a value to a key that already exists in a dictionary, Python updates the value associated with that key. The syntax is the same for both adding a new pair and updating an existing one.

**Question 3:** Which of the following data types cannot be used as a dictionary key?

  A) A string (e.g., 'name')
  B) An integer (e.g., 404)
  C) A list (e.g., [1, 2])
  D) A tuple (e.g., (10, 20))

**Correct Answer:** C
**Explanation:** Dictionary keys must be of an immutable data type. Lists are mutable (their contents can be changed), so they cannot be used as keys. Strings, integers, and tuples are all immutable.

**Question 4:** You need to store user profile data where you must be able to look up a user's email by their unique username. Which data structure is most suitable for this task?

  A) A list of usernames and a separate list of emails.
  B) A dictionary where the username is the key and the email is the value.
  C) A list of tuples, with each tuple containing a username and an email.
  D) A set containing all the usernames and emails.

**Correct Answer:** B
**Explanation:** A dictionary is the perfect choice for this scenario. It allows for direct, efficient lookup of a value (email) using a unique identifier (username) as the key, which directly models the problem.

### Activities
- {'type': 'Think-Pair-Share', 'description': "With a partner, design a Python dictionary to represent a configuration for a simple game. It should store the player's name, difficulty level ('easy', 'medium', 'hard'), and sound volume (a number from 0 to 100). Be prepared to share your dictionary structure with the class."}
- {'type': 'Code Correction', 'description': "The following code is intended to create a dictionary for a book and then update its price, but it has two syntax errors. Find and fix them. `book = ['title': 'The Hobbit', 'author': 'J.R.R. Tolkien']; book(price) = 15.99`"}
- {'type': 'One-Minute Paper', 'description': 'On a piece of paper or in a document, write a short summary (1-3 sentences) of the most important concept you learned about dictionaries today and one question you still have.'}

### Discussion Questions
- Why is it essential for dictionary keys to be unique? What kind of problems would arise if a dictionary could have duplicate keys?
- We learned that dictionaries are ideal for modeling real-world objects. Can you think of another example (besides a user profile or a student record) that could be well-represented by a dictionary? What would be the keys and values?
- What is the difference in purpose between using `del student['major']` to remove an item, versus setting its value to `None` with `student['major'] = None`?

---

