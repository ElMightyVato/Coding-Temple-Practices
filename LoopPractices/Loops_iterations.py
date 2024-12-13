# prompt the user to enter a username
#check if hte username is between 5 and 15 characters long
# if hte username meets the criteria, print a confrimation message
#if it does not meet the criteria, print a message indication the user name length requirments
#provide the user with the option to try a different usernae or exit the program
# while True:
#     username = input("Enter a user name ")
#     if len(username) >= 5 and len(username) <= 15:
#         print("Username accepted!")
#     else:
#         print("Username MUST be between 5 and 15 characters!")

#     continue_input = input("do you want to try another username? (yes/no) ")
#     if continue_input != "yes":
#         break

# flavors = ["vanilla", "chocolate", "blueberry", "mango", "salted carmel"]
# for flavor in flavors:
#     print("mmm... I just sampled " + flavor + "!")
# import re 

# email = "user@example.com"
# if re.search (r'[A-sa-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', email):
#     print("valid email address")
# else:
#     print("Invalid email address")

# num = 7
# if num % 2 == 0:
#     print("The number is even!")
# else: 
#     print("The number is odd!")

# print(7%2)

# light = input("What color is the traffic light? (red, yellow, green) ")

# if light == "red":
#     print("Stop don't go ahead")
# elif light == "yellow":
#     print("Slow down the light will be turning red soon")
# else:
#     print("You may go")

# booth_types = ["food", "games", "music", "crafts"]
# schedule_times = ["10:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]
# items_needed = ["Grill", "tickets", "instruments", "paint"]

# for i in range(len(booth_types)): #here we are using range to loop through each booth type and giving it
# # an index so it only loops through each type of item per index so food(0), 10:00 AM (0), grill (0)
#     booth = booth_types[i]
#     time = schedule_times[i]
#     item = items_needed[i]
#     print(f"{booth} booth - schedule: {time}, Item needed: {item}")

# students = 30 
# rows = 5

# students_per_row = students // rows

# for row in range(1, rows + 1): # this makes our row number start at 1 instead of 0 and increases until we reach 5
# # rows which we defined up above
#     for seat in range(1, students_per_row + 1): # here we are giving seat a number which is 6 since students_per_row
# # is equal to 6 and what it does is first it'll do rows then it'll do the seats up to 6 5(rows) times
#         seat_number = (row-1) * students_per_row + seat # here we are giving the seat number 
#         print(f"Row {row} - seat {seat}: Student {seat_number}")

# list of item item_prices
# use a for loop to iterate through the list of item_prices
# calculate the total cost by adding up the prices of all the items

# item_prices = [2.99, 5.49, 3.25, 13.99, 4.75] # here we created the list of prices that was asked of us

# total_cost = 0 # here we are inputing the total cost and making it 0 to add our prices

# for price in item_prices: #here we are creating a loop going through each price until the list is done
#     total_cost += price # he we are adding each price to the total cost which is 0 so 0 + 2.99 = 2.99 + 5.49 etc
# print(f"The total cost of the shopping cart is: ${total_cost}")

# table_size = int(input("Enter the size of the multiplication table: "))

# for row in range(1, table_size + 1):
#     for col in range(1, table_size +1):
#         product = row * col
#         print(f"{product} \t", end = "")
#     print()

# Create a list of items in hte inventory with their current quantities.
# Use a for loop to iterate over each item.
# Use an if statement to check if hte quantity of an item is below the reorder threshold
# Print out hte names of hte items that need to be reordered.

# inventory = [ 
#     ["apples", 5],
#     ["bananas", 2],
#     ["oranges", 0],
#     ["milk", 1],
#     ["eggs", 12]
# ]

# reorder_threshold = 3

# for items in inventory:
#     name, quantity = items # here we're tying name, and quanity to the list within our list so we know what part
#     #is the name and what's the quantity
#     if quantity < reorder_threshold:
#         print(f"These Items need to be reorderd: {name}")

# caves = [False, False, True, False, False]

# for index, cave in enumerate(caves):
#     # check if hte cave has the treasure
#     if cave:
#         print(f"Treasure found in cave {index + 1}!")
#         break
#     else:
#         print("The treasure was not in this cave")

# emails = ["user1@example.com", None, "user2@example.com", "user3@example.com", None]

# valid_emails = []

# for email in emails:
#     print(f"checking email: {email}")
#     if email is None:
#         print(f"email {email} is not valid")
#         continue
#     print("adding to valid_emails list...")
#     valid_emails.append(email)

# print(valid_emails)

