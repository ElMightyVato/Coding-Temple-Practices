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

while True:
    username = input("Please enter your desired username: ")

    if 5 <= len(username) <= 15:
        print(f"{username} accepted!")
    else:
        print("Please have username be between 5 and 15 characters")
    Continue_input = input("Do you want to try another username? (yes/no) ").lower()
    if Continue_input != 'yes':
        break
