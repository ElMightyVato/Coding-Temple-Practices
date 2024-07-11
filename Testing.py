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

flavors = ["vanilla", "chocolate", "blueberry", "mango", "salted carmel"]
for flavor in flavors:
    print("mmm... I just sampled " + flavor + "!")