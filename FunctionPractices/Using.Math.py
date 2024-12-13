""" 
In the digital age, usernames are crucial for identity on various platforms.
Your task is to write a program that checks if a username is neither too 
short nor too long, adhering to specific length criteria.

**Instructions**:

1. Prompt the user to enter a username.
2. Check if the username is between 5 and 15 characters long.
3. If the username meets the criteria, print a confirmation message.
4. If it does not meet the criteria, print a message indicating the username length requirements.
5. Provide the user with the option to try a different username or exit the program.

"""

# while True:
#     username = input("Please enter your desired username: ")

#     if 5 <= len(username) <= 15:
#         print(f"{username} accepted!")
#     else:
#         print("Please have username be between 5 and 15 characters")
#     Continue_input = input("Do you want to try another username? (yes/no) ").lower()
#     if Continue_input != 'yes':
#         break

"""
Exercise 2: The Precise Price Tagger

In retail applications, both online and in-store, displaying prices in a clear and precise manner is essential for customer satisfaction.
Your task is to write a program that takes a price as input and rounds it to two decimal places, making it more user-friendly.

**Instructions**:

1.Prompt the user to enter a price.
2.Use the 'round()' function to round the price to two decimal places.
3.Display the rounded price in a format that is easy for customers to understand.
4. Provide the user with the option to enter a new price or exit the program.

"""

# while True: # Remember to start loops we use whiles
#     price = float(input("Please enter the price for the item: ")) #since we are using math remember to convert your input since it will always return string
#     rounded_price = round(price, 2) # Here we are rounding after stating what we would like to round
#     print(f"Rounded price: ${rounded_price}") # We use the variable we created to print the rounded price

#     new_price = input("Would you like to enter in a new price? (yes,no) ").lower() #we use the .lower() in case they type yes and no in all caps
#     if new_price == 'no': # if the answer is no my program will stop
#         break

"""
**Problem Statement**:
You are creating a feature for a travel app that allows users to view the temperature in both celsius
and fahrenheit, so they can easily understand the weather forcast no matter where they travel.

**Instructions**:

1.Create a list of temperatures in Celsius that you want to convert.
2.Loop through the list, and for each temperature in Celsius, convert it to Fahrenheit.
3.Print out both the Celsius and Fahrenheit temperatures using f-strings for formatted output.

"""

# temps = [23,34,67,41,40]


# for fahrenheit_temps in temps: #Looping through every item in the list one by one
#     new_temp = (fahrenheit_temps * 9/5) + 32 #We are using the new variable we're looping through for this equation
#     print(f"{fahrenheit_temps}C is equivalent to {new_temp}F") # Remember to call the print within the loop not outside

"""
Goldilocks wants to find the warmest and coolest rooms in her house based on the current temperature readings.
She has a list of temperatures for each room and needs a quick way to determine which rooms are the warmest and coolest.

**Instructions**:

1.Create a list of temperatures and rooms for each room in the house.
2.Determine the warmest and coolest temperatures using the 'max()' and 'min()' functions
3.Identify the rooms with these4 temperatures and print out the results using string formatting.

"""

# room_temperatures = [22,24,19,21]
# room_names =["Living Room", "Kitchen", "Bedroom", "Bathroom"]

# warmest_temp = max(room_temperatures) # Here we are grabbing the max temp for the warmest room
# coolest_temp = min(room_temperatures) # We are doing the opposite and grabbing the smallest number

# warmest_room_index = room_temperatures.index(warmest_temp) # Here we create a new variable that will have an index 
# # reference number by using the number we grab from room_temps so warmest room is 1 since 24 is the highest number
# coolest_room_index = room_temperatures.index(coolest_temp)

# print(warmest_room_index, coolest_room_index)
# print(room_names[warmest_room_index]) #we are able to call upon the room name since warmest_room_index gives us an index number 1
# # therefore we can just call upon  it by doing room_names[index number]

# warmest_room = room_names[warmest_room_index] #Using the example above to use in our quick name variables
# coolest_room = room_names[coolest_room_index]

# print(f"The {warmest_room} is the warmest with {warmest_temp}")
# print(f"The {coolest_room} is the coolest with {coolest_temp}")

"""
Exercise 5: The E-commerce Cart summary

In an e-commerce application, it's important to provide customers with a clear and concise summary of their shopping cart before they proceed to checkout.
Your task is to write a python script that uses string concatenation to create a summary of the items in a shopping cart, including
product names, prices, and stock availabilty.

**Instructions**:

1. Define Variables for a few products, their prices, and their stock availabilty.
2. Use string concatenation to build a summary of the cart.
3. Include product names, prices, and stock status (In stock or Out of Stock) in the summary.
4. Display the cart summary to the user.

"""

# #Products
# product_1 = "wireless Mouse"
# product_2 = "Gaming Keyboard"
# product_3 = "USB-C adapter"

# #Prices
# price_1 = "$25"
# price_2 = "$50"
# price_3 = "$10"

# #Availabiltiy 
# in_stock_1 = True
# in_stock_2 = False
# in_stock_3 = True

# cart_summary = "Your Cart Items:\n" #\n lets us continue our code and start a new line so it flows well
# cart_summary += "- " + product_1 + ": " + price_1 + (" (In stock)" if in_stock_1 else " (Out of Stock)") + "\n"
# cart_summary += "- " + product_2 + ": " + price_2 + (" (In stock)" if in_stock_2 else " (Out of Stock)") + "\n"
# cart_summary += "- " + product_3 + ": " + price_3 + (" (In stock)" if in_stock_3 else " (Out of Stock)") + "\n"

# print(cart_summary)

"""
**Problem Statement**:
You are creating an interactive story where the reader can choose their own adventure
At each stage of the story the reader is presented with a choice that determines the direction of the narrative
Your task is to write a python script that guides the reader through the first decision point of the story

**Instructions**:

1.Present the reader with a brief introduction to the story and a choice to make
2.Capture the reader's choice using the 'input()' function
3.Depending on the choice, display the outcome of their decision.
4. Use a list to store possible choices and outcomes.
"""

# print("You wake up in a mysterious forest. Two paths lie before you.")

# choices = ['left', 'right']
# outcomes = ["You encounter a friendlly elf who offers you a map.", "you stumble upon a sleeping dragon"]

# print(f"Do you go left or right? (type 'left' or right')")
# decision = input().lower() #The reason we don't input our question into our input is becasue we want it to appear on the next line

# if decision not in choices: #here we are checking if the decision we input is not in choices it won't run
#     print("Confused, you decide to wait for a clearer sign of which path to take.")
# elif decision == 'left':
#     outcome_index = choices.index('left')
#     print(outcomes[outcome_index]) #Remember this is grabbing the outcome at whatever index number left is at so 0
# else:
#     outcome_index = choices.index('right')
#     print(outcomes[outcome_index])

"""
Exercise 7: The Customized List Printer

You are tasked with creating a program that prints out a shopping list.
However, the user wants the list to be printed in a specific format, with custom seperators between items and a custom
ending to signify the end of the list.

**Instructions**:

1. Create a list of shopping items.
2. Ask the user for their preferred separator (e.g., comma, slash, dash).
3. Ask the user for their preferred ending phrase (e.g., "end of the list", "That's all!")
4. User a loop to print each item with the user's preferred separator and end the list with their choosen ending phrase.

"""

# items = ["Shoes", "Dress", "Guns", "Video Games", "Manga"]

# seperation = input("How would you like to seperate these items? (',', '/', '-': ")

# ending = input("How would you like to know you're done with the list? (End of the list, That's all!)")

# print("Your shopping list: ", end="\n\n") # Without the double n's there would be no space inbetween your shopping list and items being listed
# for item in items:
#     if item == shoping_list[-1]: # we are using this so it does not put a comma on the last item and will just print it
#         print(item)
#     print(item, end=seperation + " ") # With end we are just adding our input at the end of each item
# print("\n\n" + ending) 

"""
Exercise 8: The Dynamic Type Quiz Game

You are tasked with developing a quiz game that challenges players to answer questions that require answers in different data types.
The game should prompt the user for an answer, convert the answer to the required type, and verify its correctness

**Instructions**:

1. Create a separate list for questions, correct answers, and the required answer types.
2. Use a loop to iterate over the questions and present them to the user one by one.
3. For each question, prompt the user for their answer and convert it to the required type using the corresponding type conversion function.
4. Compare teh user's converted answer to the correct anser and provide immediate feedback
5. Keep a count of hte number of correct answers and display the user's score at the end of the game. 

"""

# questions = [
#     "What is 10 plus 4?",
#     "Enter a decimal number between 1 and 2", 
#     "what is string representation of the number 20?", 
#      "Is python a programing language? (True/False)"
# ]

# correct_answers = [14, 1.5, "20", True]
# answer_types = [int, float, str, bool]

# score = 0 #Need this variable so we can add to it when our answers are correct

# for i in range(len(questions)): #we are iterating after every question but also giving it an index so what is 10 plus 4 is index 0
#     user_answer = input(questions[i] + " ") # here we are asking them each question and we're adding the space ourselves in this input
#     try: #This is to prevent a potential error
#         if answer_types[i] == bool: #only using this for bool to convert 
#             converted_answer = user_answer.lower() in ['true', 't', '1','yes','y'] #this is for when the user answers any of these with potential answers
#         else:
#             converted_answer = answer_types[i](user_answer) #here we are saying the answer type index is equal to the user answer we did with index as well so match 1:1
#         if converted_answer == correct_answers[i]:
#             print("Correct!")
#             score += 1
#         else: 
#             print("wrong answer.")
#     except ValueError:
#         print("Invalid input type.")
# print(f"Your final score is {score}/{len(questions)}")

"""
Exercise 9: The Type Inspection Challenge

You are creating a program that categorizes elements in a list based on their data type.
The program should iterate over a mixed-type list, identify the data type of each element, and sort the elements into separate lists according to their type.

**Instructions**:

1. Create a mixed-type list with various data types (e.g., integers, floats, strings, booleans).
2.Initialize separate lists to hold elements of each data type.
3. Use a loop to iterate over the mixed-type list
4. For each element, use 'isinstance()' or 'type()' to determine the element's type
5. append the element to the corresponding list based on it's type
6. Use shorthand 'if' statements to streamline the type-checking logic
7. Print out hte gategorized lists after processing the entire mixed-type list.

"""

# mixed_list = [10, 3.14, 'python', False, 42, 'code', 2.718, True]

# integers = []
# floats = []
# strings = []
# booleans = []

# for element in mixed_list:
#     if isinstance(element, int) and not isinstance(element, bool): #booleans is a subclass of integers so you have to do the do not 
#         integers.append(element)
#     elif isinstance(element, float):
#         floats.append(element)
#     elif isinstance(element, str):
#         strings.append(element)
#     elif isinstance(element, bool):
#         booleans.append(element)
#     else:
#         print(f"Unknown type: {type(element)}")

# print(f"Integers: {integers}")
# print(f"floats: {floats}")
# print(f"strings: {strings}")
# print(f"booleans: {booleans}")

"""
Exercise 10: The Math Function Marathon

You are working on a data analysis project that requires you to process a list of floating-point numbers.
Your task is to calculate the sum of all numbers, find the square root of each number, and then round them up or down to the 
nearest integer.
Additionally, you need to identify which numbers are above the average after rounding.

**Instructions**:

1.Create a list of floating-point numbers.
2.Calculate the sum of the numbers using the 'sum()' function and print the result.
3.Use a loop to iterate over each number in the list.
4.Inside the loop, calculate the square root of each number using the 'sqrt()' function from the 'math' module.
5. Round each square root to the nearest integer using the 'round()' function and then determine whether to round up or down using 'ceil()'
or 'floor()' from the 'math module
6.Use nested 'if' statements to compare each rounded number with the average of hte list and print whether it is above or below average. 
7. Ensure that the output is clear and informatitive.

"""

# import math

# numbers = [2.5, 3.6, 4.7, 5.8, 6.9]

# total_sum = sum(numbers)
# print(total_sum)

# average = total_sum/ len(numbers)

# for number in numbers:
#     sqrt_number = math.sqrt(number)
#     rounded_number = round(sqrt_number)
#     if rounded_number < sqrt_number:
#         rounded_number = math.ceil
#     else:
#         rounded_number = math.floor(sqrt_number)

#     if rounded_number > average:
#         print(f"{rounded_number} is above the average")
#     else:
#         print(f"{rounded_number} is below the average")















