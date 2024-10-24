"""
Exercise 1: E-commerce Product catalog

Build a python program to manage an e-commerce product catalog efficiently.
The program should facilitate adding new product categories, addig products, displaying all available categories, and 
conducting product searches within the catalog.

**Instructions**

1. Initialize a dictionary to represent your prodcut catalog.
2. Implement functions to:
    - Add a new product category
    - Add a product to an exisiting category
    - Display all product categories with their respective products
    - search for a product across all categories
3. Include error handling for situations such as adding a product to an unlisted category
4. Ensure that the prodcut search is case-insensitive
5. Design the program to handle multiple additions and searches

**hints**

- Start by pre-populating your catalog dictionary with some categories and products.
- Utilize the 'lower()' or 'upper()' methods on strings for case-insensitive comparison.
- In your search function, check for hte product's prescense in every category.
- Leverage 'try' and 'except' blocks to gracefully handle any KeyError instances.

"""

# def add_category(catalog, category):
#     if category not in catalog:
#         catalog[category] = []
#         print(f"Category '{category}' added.")
#     else:
#         print(f"Category '{category}' already exists.")

# def add_product(catalog, category, product):
#     try:
#         if product not in catalog[category]:
#             catalog[category].append(product)
#             print(f"Product '{product}' aded to '{category}'.")
#         else:
#             print(f"Product '{product}' already exists in '{category}'.")
#     except KeyError:
#         print(f"Category '{category}' does not exist.")

# def display_categories(catalog):
#     for category, products in catalog.items():
#         print(f"{category}: {', '.join{products}}")

# def search_product(catalog, product):
#     found = False
#     for category, products in catalog.items():
#         if product.lower() in [p.lower() for p in products]:
#             found = True
#             print(f"Product '{product}' was found.")
#             break
#     if not found: 
#         print(f"Product '{product}' not found.")

# catalog = {
#     "Electronics": ["Laptop", "Smartphone"],
#     "Books": ["Fiction", "Non-Fiction"]
# }

# add_catagory(catalog, "Clothing")
# add_product(catalog, "Electronics", "Camera")
# display_categories(catalog)
# search_product(catalog, "laptop")

"""
Exercise 2: The Simple Order Validator

An online bookstore is processing orders for a popular novel.
They need a simple system to ensure that customers enter a valid quantity when placing their orders.

**Instructions**:

1. Prompt the user to enter the quantity of books they wish to order.
2. Validate the input to ensure it is a positive integer
3. If the input is valid, confrim the order by printing a message.
4. If the input is invalid (not an integer or a negative number), display an error message and prompt the user again.
5. Use a try/except block to catch non-numberic inputs

**HInts**:

- Use a while loop to keep asking for input until a valid quantity is entered
- Utilize the 'int()' function to convert the input to an integer and catch 'ValueError' for non-numeric inputs
"""

# def validate_order():
#     while True:
#         try:
#             quantity = int(input("Enter the quantity of books you want to order: "))
#             if quantity > 0:
#                 print(f"Thank you! You have ordered {quantity} books")
#                 break
#             else:
#                 print("Invalid quantity. Please enter a positive integer.")
#         except ValueError:
#             print("Invalid input. PLease enter a number.")

# validate_order()

"""
Exercise 3: The Safe Calculator

In a terminal-based calculator app, it's crucial to ensure that the user inputs are valid numbers before any arithmetic
operation is performed.
Your task is to enhance the app's robustness by implementing input validation that prevents the program from crashing
when a user enters non-numberic data.

**Instructions**:

1. Write a function 'safe_addition' that prompts the user for two numbers and returns their sum. It should handle any
'ValueError' exceptions that arise from the non-numberic input.
2. Use a loop to allow the user to try entering the numbers again if they make an input error.
3. Print the result of the addition if hte inputs are valid numbers
4. Provide the user with the option to perform another addition or exit the program.

**Hints**:

- Use the 'try' block to attempt to convert the user input to floats.
- Use the except block to catch 'ValueError' and prompt the user to enter the numbers again.

"""

# def safe_addition():
#     while True:
#         try:
#             num1 = float(input("Enter the first number: "))
#             num2 = float(input("enter the second number: "))
#             return num1 + num2
#         except ValueError:
#             print("Please eneter only numbers. Try again.")

# while True:
#     result = safe_addition()
#     print(f"The sum is: {result}")

#     continue_input = input("would you like to perform another addition? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break

"""
Exercise 4: The Resilient Divider 

In a data analysis context, dividing by zero can often occur and lead to program crashes.
YOur task is to create a function that performs division but returns a specific message instead of crashing when a 
division by zero is attempted.

**Instructions**:

1. Write a function safe_divide that takes two parameters, 'a' and 'b', and returns the result of 'a/b'
2. Implement error handling to catch zerodivisionerror exceptions within the function
3. IF division by zero occurs, the function should return a message indicating that division by zero is not allowed.
4. Test the function with user input and print the result or error message.

**hints**:

- User the try block to attempt the division
- Use the except block to catch zerodivisionerrror and return the appropriate message.

"""

# def safe_divide(a,b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Division by zero is not allowed."

# while True:
#     try:
#         numerator = float(input("Enter the numerator: "))
#         denominator = float(input("ENter the denominator: "))
#         result = safe_divide(numerator, denominator)
#         print(f"The result of the division is: {result}")
#     except ValueError:
#         print("Please enter only nubers.")

#     continue_input = input("Would you like to perform another division? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break

"""
Exercise 5: The login gatekeeper

In a software application, it's crucial to ensure that user credentials meet certain security standards.
Your task is to create a function that checks whether a username meets the required criteria and raises a custom
exception if it does not.

**Instructions**:

1. Define a custom exception class named UsernameError that inherits from the base exception class
2. Write a function check_username that takes a single parameter, 'username', and checks if it meets the criteria 
(e.g., at least 6 characters long).
3. If the username does not meet the crieteria, raise a usernameerror with an appropriate error message
4. PRompt the user to input a username and use a try-except block to catch the usernameerrror and display the error message.

**hints**:

- Use the raise keyword to raise the custom exception with a message when the username is too short
- In the except block catch the usernameerrror and print the message to inform the user
"""

# class UsernameError(Excepton):
#     def __init__(self, message):
#         self.message = message

# def check_username(username):
#     if len(username) < 6:
#         raise UsernameError("Username must be at least 6 characters long")

# while True:
#     username_input = input("PLease enter your username: ")
#     try:
#         check_username(username_input)
#         print("Username is valid!")
#         break
#     except UsernameError as e:
#         print(f"Error: {e.message}")

#     try_again_input = input("Would you like to try a different username? (yes/no) ").lower()
#     if try_again_input != 'yes':
#         break

"""
Exercise 6: The Data Sanitizer

In data processing applications, it's common to encounter a mix of valid and invalid data entries.
Your task is to write a program that attempts to convert a list of string values to integers, gracefully handling
any values that cannot be converted.

**Instructions**:

1. Create a list of strings where some represent integer values and others are non-numeric.
2. Iterate over the list and attempt to convert each string to an integer.
3. IF a string cannot be converted to an integer, catch the 'ValueError' and print a warning message.
4. Store the successfully converted integers in a new list called 'parsed_data'.

**Hints**:

- Use a try-except block within your loop to atch the conversion errors.
- Print a warning message in the except block for each non-convertible string

"""

# data_entries = ["100", "200", "three", "400", "5ive"]
# parsed_data = []

# for entry in data_entries:
#     try:
#         parsed_data.append(int(entry))
#     except ValueError:
#         print(f"Warning: {entry} is not a valid integer and will be skipped.")

# print(f"Parsed data: {parsed_data}")

"""
Exercise 7: The server's graceful exit

In server applications, unexpected exceptions can occur, and it's crucial to handle these gracefully to prevent data loss
and ensure necessary cleanup is performed.
Your task is to simulate a server's main operation loop and implement a mechanism that guarantees a graceful shutdown,
even if an error occurs.

**Instructions**:

1. Simulate a server's main loop with a placeholder comment.
2. Use a try-except-finally block to handle any potential exceptions during the server's runtime
3. In the except block catch a general exception and print an error message.
4. In the finally block perform cleanup operations and print a shutdown message.

**HInts**:

- The finally block is executed after try and except blocks regardless of whether an exception was raised or not
- Use the finally block to include any code that you want to execute regardless of exceptions, such as closing files or
releaseing resources.
"""

# try:
#     print("Server is running...")
#     # simulate an error
#     raise Exception("Unexpected error!")
# except Exception as e: 
#     print(f"An error occured {e}")
# finally:
#     print("Performing cleanup operations...")
#     print("Shutting down server gracefully")

"""
Exercise 8: User input validation with failback

In user-driven applications, it's common to require input that matches specific criteria
Your task is to write a program that prompts the user for their favorite fruit from a predefined list.
If the input is not in the list the program should handle the situation grcefully and ask for input again.

**Instructions**:

1. Create a list of fruits that are allowed inputs.
2. Prompt the user to enter their favorite fruit
3. Use a try-except-else block to validate the input
4. If the input is not in the list, raise a ValueError and handle it by asking for input again
5. If the input is valid, print a confirmation message.

**HInts**:

- The else block can be used to execute code when the try block doesn't raise an exception
- Use a loop to keep asking for input until a valid fruit is entered
"""

# allowed_fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# while True:
#     try:
#         favorite_fruit = input("Enter your favorite fruit: ").lower()
#         if favorite_fruit not in allowed_fruits:
#             raise ValueError("Fruit not in the list.")
#     except ValueError as ve:
#         print(ve)
#         print("Please choose a fruit from the list.")
#     else:
#         print(f"Great choice! Your favorite fruit is {favorite_fruit}.")
#         break

"""
Exercise 9: Multi-Scenario Input Handling

In a software application that processes user data, it's essential to anticipate and handle different kinds of erroneous
input.
Your task is to write a program that asks users for their age and ensures that the input is both a number and within a
reasonable range.

**Instructions**:

1. Prompt the user to enter their age
2. Use a try-except block to handle the following scenarios:
    - The input is not a number (ValueError)
    - The number is not within the range of 0 to 120 (ValueError)
3. If an excetion is raised provide a specific error message for hte type of exception and ask for the input again
4. IF the input is valid print a confirmation message

**HInts**:

- Use int() to convert the input string to an integer and catch any ValueError exceptions
- Check the age range within the try block and rasie a ValueError with a custom message if the age is out of range.
"""

# while True:
#     try:
#         user_age = input("Enter your age: ")
#         age = int(user_age)
#         if age < 0 or age > 120:
#             raise ValueError("Age must be between 0 and 120")
#     except ValueError as ve:
#         if "invalid literal" in str(ve): # this is checking age and if it's a string will run this part of the code
#             print("That's not a number. Please enter your age using digits.")
#         else: 
#             print(ve) # Other wise if our age is below 0 or over 120 this code will run
#     else:
#         print(f"Thank you. Your age is recorded as {age}.")
#         break

"""
Exercise 10: Robust Calculator Input Handling

You are developing a calculator app that can perform basic arithemtic operations.
The app should robustly handle user input, ensuring that only numerical values are accepted and operations are performed
correctly.

**Instructions**:

1. Ask the user to enter two numbers
2. Ask the user to choose an operation (addition, subtraction, multiplication, or division)
3. Perform the operation and display the result
4. Use a try-except block to handle ValueError and TypeError exceptions
5. No matter what happens thank the user for using hte calculator in a finally block

**Hints**:

- Use float() to convert the input strings to numbers
- Use an if-elif-else structure to perfomr the choosen operation
- In the except blocks handle ValueError for non-numberic input and TypeError for incorrect operations like division by zero
- Use the finally block to print a thank you message
"""

# def get_number(prompt):
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print("That's not a valid number. Please try again.")

# def get_operation():
#     operations = ['+', '-', '*', '/']
#     while True:
#         op = input("Choose an operation (+, -, *, /): ")
#         if op in operations:
#             return op
#         print("Invalid operation. Please choose +, -, *, /.")

# num1 = get_number("Enter the first number: ")
# num2= get_number("Enter the second number: ")
# operation = get_operation()

# try:
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == '/':
#         result = num1 / num2
#     print(f"The result is: {result}")
# except TypeError:
#     print("An unexpected type error occured")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# finally:
#     print("Thank you for using the calculator!")