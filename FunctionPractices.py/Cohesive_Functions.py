"""
Exercise 1: The smart home morning routine:

You are programming a smart home system to perform a series of actions as part of a morning routine.
The system should greet you, inform you of the weather, remind you of your first calendar event, and tell you if you have unread emails.

***Insturctions***:

1. Define a function called 'morning_routine()' that takes no arguments.
2. Inside the function, print "Good Morning!" to simulate a greeting.
3. Create a list of weather conditions for the week.
4. Use a loop to iterate over the weather list and use an 'if' statement to check if hte current day's weather is "rainy". If it is,
print a reminder to take an umbrella.
5. Create a list of calendar events for the week.
6. Use a loop to find today's event and print it as a reminder
7. Create a variable to store the number of unread emails.
8. Use an 'if' Statement to check if there are any unread emails.
9. Call the 'morning_routine()' function to execute the morning routine.

**Hint**:
You can use the 'datetime' module to get the current day of hte week if you want to match the weeather and events to the actual day"""
# import datetime

# def morning_routine():
#     print("good morning!")

#     weather_conditions = ["Sunny", "Rainy", "Rainy", "Rainy", "Sunny", "Cloudy", "Windy"]

#     today_weather = weather_conditions[datetime.datetime.today().weekday()]
#     # print(datetime.datetime.today().weekday()) # Here we are looking at what day it is

#     # print(today_weather) # since the day today is wednesday it makes the index 2
#     if today_weather == "Rainy":
#         print("Don't forget your umbrella, it's rainy today.")


#     calender_events = ["Gym", "Meeting with bob", "Dentist appointment", "Lunch with sarah", "Grocery shopping"]
#     today_event = calender_events[datetime.datetime.today().weekday()]

#     print(f"Today's event: {today_event}")

#     unread_emails = 5
#     if unread_emails > 0:
#         print(f"You have {unread_emails} unread emails.")

# morning_routine()

"""
Exercise 2: The versatile coffee machine 

You have a coffee machine that can make various types of coffee. You want to prgram it to prepare your coffee based on your selection.

***Instructions***:

1. Define a function called 'make_coffee()' that takes on parametere 'coffee)type with a default value of "espresso"
2. Inside the function, print the message indicating the type of coffee being made.
3. Create a list of coffee types that the machine can make. 
4. Use a loop to iterate over the list of coffee types.
5. Inside the loop, use an 'if' statement to check if hte coffee type is "cappuccino". If it is, print a special message indicating
that it's a favorite.
6. Call the 'make_coffee()' function with different arguments to simulate making different types of coffee.
7. Ensure that calling 'make_coffee()' without arguments defaults to making an espresso.
"""
# def make_coffee(coffee_type = "Espresso"):
#     print(f"Making a cup of {coffee_type} coffee!") #Here we have created our function that will print this message

# coffee_type = ["Dark", "French Vanilla", "Cappuccino", "Espresso"] # Here is the list we created for types of coffee
    
# for coffee in coffee_type: # Here we are creating our for loop to go over each type of coffee
#     make_coffee(coffee) #Now we're using the function we created but inputting our coffee for loop variable so it will cycle through each type of coffee
#     if type == "Cappuccino": #during our loop if we hit cappuccino it will print the following below
#             print("Yum, a cappuccino my FAVORITE!")

# make_coffee() # Remember this will default to espresso since that's what we have in our function as the dafault value

"""
Exercise 3: The Dynamic Playlist DJ

You are devoloping a feature for a music app that allows users to create a custom playlist and play the songs in sequence.

***Instructions***:

1. Define a fucntion called 'play_songs()' that takes one parameter 'song_list'.
2. Inside the function, use a loop to iterate over 'song_list'
3. For each song in the list, print a message indicating that the song is now playing.
4. Beforfe calling the function, prompt the user to enter the number of songs they want to add to the playlist.
5. Use a loop and 'input() to accept song names form the user
6. Call the 'play_songs() function with the user-created list of songs as an argument.
"""

# def play_songs(song_list): #here we created a function with song_list and a loop going over every song
#     for song in song_list:
#         print(f"Now playing {song}")

# num_songs = int(input("How many songs would you like to add? ")) # here we ask the user how many songs they would like to add

# user_playlist = [] # Have to create an empty list to store the songs the user wants to add

# for i in range(num_songs): # Here we are iterating i which is the indexes and using range which is the maximum they can go
#     #which is coming from our input in num_songs
#     song_name = input(f"Enter song {i+1} ") # Here we are asking then to enter a song and then giving it the index plus
#     # 1 since indexes always start at 0
#     user_playlist.append(song_name)

# play_songs(user_playlist)

"""
Exercise 4: The group expense tracker

You are creating a program to track expenses for a group of friends on a trip. The program will calculate the total
expenses and identify the highest spender

***Instructions***:

1. Define a function called 'track_espenses()' that takes a variable number of nubmerical arguments representing individual expenses.
2. Inside the function, calcualte the sum of the expenses and print the total.
3. Also, determine the highest expense and print the person associated with it.
4. Outside the function, use a while loop to prompt each user to enter their expense until they enter 'done'
5. Use 'input()' to accept the expense amount from each user and store these in a list
6. After collecting all expenses, call the 'track_expenses()' function with the list of expenses as arguments using the splat opperator (*)
"""

# def track_expenses(*expenses):
#     total_expenses = sum(expenses)
#     print(f"The total expenses are: {total_expenses}")

#     highest_expense = max(expenses) #max is getting the highest expense
#     spender = expenses.index(highest_expense)+1
#     print(f"Person {spender} is the highest spender with an expense of: {highest_expense}")

# group_expenses = [] # here we create a list

# while True:
#     expense_input = input("ENter an expense amount or 'done' to fnish: ") #we do a while loop so it loops indefinetly until we tell it to stop

#     if expense_input.lower() == 'done':
#             break
#     else:
#         expense = float(expense_input)
#         group_expenses.append(expense)


# track_expenses(*group_expenses)

"""
Exercise 5: The Product Inventory Manager

You are developing a featuer for an e-commerce app that allows the store anager to view and update the inventory of products.

**Instructions**:

1. Define a list called 'products' that contains the intial inventory of product names.
2. Create a function called 'manage_inventory()' that will display the current inventory, allow the manager to add new
products, and remove products that are out of stock.
3. Inside the function, use a loop to display options for the manager: view inventory, add product, remove product, and exit.
4. Use list slicing and the 'len()' function to display the first 5 products in the inventory when viewing
5. Allow the manager to add a product by entering its name, which will be appended to the products list
6. Allow the manager to remove a product by entering its name. Ensure the product exists in the list before attempting to remove it.
7. Use the 'input()' function to collect the manager's choices and product names.
"""

# products = ['T-shirt', 'Jeans', 'Sneakers', 'Hat', 'Sunglasses', 'Jacket', 'Watch']

# def manage_inventory():
#     while True: # will run indefiently because of while true
#         print("\nInventory Management System")
#         print("1. View Inventory")
#         print("2. Add Product")
#         print("3. Remove Product")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             print("\\Current Inventory:")
#             for prodcut in products[:5]:
#                 print(products)
#             if len(products) > 5:
#                 print("...and more")
#         elif choice == "2":
#             new_product = input("Enter the name of the new product: ")
#             products.append(new_product) # Using the appened we are adding what they input into our list
#             print(f"{new_product} has been added to the inventory")
#         elif choice == "3":
#             product_to_remove = input("Enter the name of the product you wish to remove: ")
#             if product_to_remove in products:
#                 products.remove(product_to_remove)
#                 print(f"{product_to_remove} has been removed from the inventory")
#             else:
#                 print("This product does not exist!")
#         elif choice == "4":
#             print("Exiting inventory management system.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# manage_inventory()

"""
Exercise 6: The payment splitter

In a group of friends, expenses are often shared. Your task is to create a function that calculates how much each person
must pay or be reinbursed after a shared expense

**Instructions**:

1. Define a function called 'split_payment' that takes a list of expenses and the number of friends as arguments.
2. The function should calculate the total expenses and the individual share.
3. Return both the total and the individaul share from the function.
4. Outside the function, use a loop to allow the user to input the cost of each expense and add it to a list
5. After all expenses are entered, call the 'split_payment' function with the list of expenses and the number of friends.
6. Display the total expenses and how much each person must pay or be reimbursed.
"""

# def split_payment(expenses, number_of_friends):
#     total_expenses = sum(expenses)
#     individual_share = total_expenses / number_of_friends
#     return total_expenses, individual_share 

# expenses = []

# number_of_friends = int(input("ENter the number of friends: "))

# while True:
#     expense = input("enter an expense or 'done' to finish: ")
#     if expense.lower() == 'done':
#         break
#     expenses.append(float(expense))

# total, share = split_payment(expenses, number_of_friends)

# print(f"\nTotal expenses: ${total:.2f}.")
# print(f"Each person must pay: ${share:.2f}") #.2f is helping it round up to two decimal places

"""
Exercise 7: The Phonebook Manager

You need to manage contacts in a phonebook.
Your task is to create functions that can add a new contact and display all contacts, ensuring that you correctly handle 
variable scope.

**Instructions**:

1. Define a global list called 'phonebook' to store contacts as separate lists for names and numbers.
2. Define a function called 'add_contacts' that takes a name and number as arguments and adds them to the 'phonebook' list
3. Define a function called 'display_contacts' that prints all the contacts in the 'phonebook'.
4. Use a loop to allow the user to choose between adding a contact or displaying all contacts.
5. Ensure that the 'phonebook' list is not reinitialized within the functions preserving its global scope
"""

# phonebook_names = []
# phonebook_numbers = []

# def add_contacts(name, number):
#     global phonebook_names
#     global phonebook_numbers
#     phonebook_names.append(name)
#     phonebook_numbers.append(number)
 
# def display_contacts():
#     global phonebook_names
#     global phonebook_numbers
#     for i in range(len(phonebook_names)): #we want to look through both lists so we
#         #use i in range signifying index for range being the length of names in the list
#         print(f"Name: {phonebook_names[i]}, Number: {phonebook_numbers[i]}") #this will grab the string within
#         #phonebook names 

# while True:
#     action = input("Choose an action: [A]dd contact, [D]isplay contact, [Q]uit: ")
#     if action == 'A':
#         name = input("Enter the contact's name: ")
#         number = input("Enter the contact's phone number: ")
#         add_contact(name, number)
#     elif action == 'D':
#         display_contacts()
#     elif action == 'A':
#         break
#     else:
#         print("Invalid action. Please try again.")

"""
Exercise 8: The HR Assistant

You are taksed with managing employee records for a small company. Your job is to create functions that can add new
employee details, calculate average age and display all employee information using lists instead of dictionaries.

**Instructions**:

1. Define a global list called 'employees' to store employee details, where each employee is represented as a list with
elements '[name, age, department]
2. Define a function called 'add_employee' that takes name, age, and department as arguments and adds them as a list to 
the 'employees' list.
3. Define a function called 'calculate_average_age' that computes and returns the average age of all employees.
4. Define a function called 'display_employees' that prints all the employee details in a formatted manner.
5. Use a loop to allow the user to choose between adding an employee, calcualting the average age, or displaying all employees
6. Ensure that the 'employees' list is not reinitailized within the functions, maintining its global scope.
"""

employees = []

def add_employee(name, age, department):
    global employees
    employees.append([name, age, department])

def calculate_average_age():
    global employees
    total_age = sum(employee[1] for employee in employees) #we are looping through employees for every single one of these
    #and only grabbing the age
    return total_age / len(employees) if employees else 0

def display_employees():
    global employees
    for employee in employees:
        print(f"Name: {employee[0]}, Age: {employee[1]}, department: {employee[2]}") #employee 0 is equivilant to name
        # employee 1 is equal to age and finally employee 2 is department

while True:
    action = input("Choose an action: [A]dd employee, [C]alculate average, [D]isplay employees, [Q]uit: ").upper()
    if action == 'A':
        name = input("Enter the employee's name: ")
        age = int(input("Enter the employee's age: "))
        department = input("What department do they work in? ")
        add_employee(name, age, department)
    elif action == 'C':
        average_age = calculate_average_age()
        print(f"The average age of employees is: {average_age:.2f}")
    elif action == 'D':
        display_employees()
    elif action == 'Q':
        break
    else:
        print("Please choose a new option.")













