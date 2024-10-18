"""
Exercise 1: The book index finder

You are developing a feature for an e-reader app that allows users to find the index of characters in a book or document
this feature helps users to quickly navigate through the text by character references

**Instructions**:

1. Write a function 'find_character_index' that takes a 'text' string and a 'character' as parameters and returns
the index of hte character in the text.
2. If the character is not found, the function should return a message stating that the character is not present
3. Implement a loop that prompts the user to enter a string (representing a paragraph or line from a book) and a 
character to search for.
4. Use the function to find the index of the character and print the result using an f-string
5. Ensure the program handles cases where the user may enter multiple characters instead of a single one.

"""

# def find_character_index(text, character):
#     if len(character) == 1: #want to make sure the character we're searching for is equal to 1
#         index = text.find(character) # here we have a variable called index were we look in text and try to find the 
#         #character index number
#         if index == -1:
#             return f"The character '{character}' is not present in the text."
#         else:
#             return f"The index of the '{character}' is: {index}" 
#     else:
#         return "Please enter only a single character."
    
# while True:
#     text_input = input("Enter a line of text from the book ")
#     char_input = input("Enter the character to find. ")

#     result = find_character_index(text_input, char_input) #here we use our inputs and plug it into our function so
#     # text_input becomes text and char_input becomes character
#     print(result)

#     continue_search = input("Do you want to search for another character? (yes/no): ").lower()
#     if continue_search != 'yes':
#         break

"""
Exercise 2: The echo text generator

you are tasked with developing a feature for a social media app that allows users to create a fun echo effect with their
text posts.
This feature repeats each character in the text to create an echo-like pattern, making the posts more engaging and 
visually appealing.

**Instructions**:

1. Write a function 'generate_echo_text' that makes a 'text' string as a parameter and returns a new string with each
character repeated twice.
2. Implement a loop that prompts the user to enter a string (representing a social media post or message).
3. Use the function to generate the echo text and print the result using an f-string
4. Ensure the program handles empty strings and informs the user accordingly

"""

# def generate_echo_text(text):
#     if text:
#         return ''.join([char * 2 for char in text]) # this will go through and multiple the character by 2
#     else:
#         return "The input text cannot be empty. Please enter some text."
    
# while True:
#     user_input = input("Enter your text to echo: ")

#     echo_text = generate_echo_text(user_input) # this runs our function using the user_input for text
#     print(f"Your echoed text is: {echo_text}")

#     continue_input = input("Do you wish to continue? (yes/no)").lower()
#     if continue_input != 'yes':
#         break

"""
Exercise 3: The game highlight reel

You are developing a feature for a sports app that allows users to input a series of game highlights and then displays
each event separately for easy reading and analysis.
This feature is particulalry useful for users who want to quickly create summaries of key moments in a match or game.

**Instructions**:

1. Write a function 'format_highlights' that takes a string of highlights separated by commas and returns a list of 
individual plays.
2. Implement a loop that prompts the user to enter the string of highlights.
3. Use the function to format the highlights and print each play on a new line using an f-string.
4. Ensure the program handles empty strings by informing the user and asking for input again.

"""

# def format_highlights(highlight_string):
#     if highlight_string.strip():
#         return [play.strip() for play in highlight_string.split(',')]
#     else:
#         return []

# while True:
#     user_input = input("Enter the game Highlights, separated by commas: ")
#     formated_highlights = format_highlights(user_input)

#     if formated_highlights:
#         print("Game Highlights: ")
#         for play in formated_highlights:
#             print(f"- {play}")
#     else:
#         print("No highlights entered. Please provide the highlights of hte game.")
    
#     continue_input = input("Do you want to enter more highlights? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break

"""
Exercise 4: The announcement speaker

You are creating a feature for a public address system app that allows users to input a message and then displays the
message in uppercase, which represents the announcemnt mode.

**Instructions**:

1. Write a function 'announce_message' that takes a string and returns the same string in upper case.
2. implement a loop that prompts the user to enter their message.
3. use the function to convert the message and print it using an f-string.
4. Ensure the program handles empty strings by informing the user and asking for input again.

"""
# def announce_message(message):
#     return message.upper()

# while True:
#     user_input = input("Enter your message for hte announcement: ")
#     if user_input.strip():
#         announcment = announce_message(user_input)
#         print(f"Announcement: {announcment}")
#     else: 
#         print("No message entered. Please provide a message for the announcement.")
    
#     continue_input = input("Do you want to make another announcement? (yes/no): ").lower()
#     if continue_input != "yes":
#         break

"""
Exercise 5: The personalized welcome mat

You are developing a feature for a hopitality ap that personalizes the welcome experience for guests.
The app takes the guest's name as input and prints a welcome message, with the name beautifully centered within a design
made of asterisks.

**Instructions**:

1. WRite a function 'create_welcome_message' that takes a string (the user's name) and returns a welcome message.
2. The welcome message should have the user's name centered within a line of asterisks.
3. Implement a loop that prompts the user to enter their name.
4. Use the function to generate the welcome message and print it using an f-string.
5. Ensure the program handles empty or invalid names by infomring the user and asking for input again.

"""
def create_welcome_message(name):
    line_length = 30
    centered_name = name.center(line_length, '*')
    return f"Welcome {centered_name} welcome"

while True:
    user_name = input("Please enter your name for a personalized welcome message: ")
    if user_name.isalpha():
        welcome_message = create_welcome_message(user_name)
        print(welcome_message)
    else:
        print("Invalid name please enter alphabetic characters only")

    continue_input = input("Do you wish to continue? (yes/no) ").lower()
    if continue_input != 'yes':
        break



