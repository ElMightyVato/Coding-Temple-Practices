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
# def create_welcome_message(name):
#     line_length = 30
#     centered_name = name.center(line_length, '*')
#     return f"Welcome {centered_name} welcome"

# while True:
#     user_name = input("Please enter your name for a personalized welcome message: ")
#     if user_name.isalpha():
#         welcome_message = create_welcome_message(user_name)
#         print(welcome_message)
#     else:
#         print("Invalid name please enter alphabetic characters only")

#     continue_input = input("Do you wish to continue? (yes/no) ").lower()
#     if continue_input != 'yes':
#         break

"""
Exercise 6: The stats breakdown

**Instructions**:

1. Write a function 'print_stats' that takes a string of stats and prints each one on a new line.
2. Each stat should be presented in the format: "catagory: [CATEGORY], Value: [VALUE]".
3. Implement a loop that prompts the user to enter their stats string.
4. Use the function to parse the user to enter their stats string
5. Ensure the program handles invalid formats by informing the user and asking for input again.

"""

# def print_stats(stats_string):
#     stat_list = stats_string.split(';')
#     # Goals:4; Fouls:1 >we are seperating them with the semi colon and then they'll become their own individual strings
#     for stat in stat_list:
#         category_value =stat.split(':')
#         if len(category_value) == 2:
#             category, value = category_value
#             print(f"Category: {category}, Value: {value}")
#         else:
#             print("Invalid format for stat")
#             break
# while True:
#     stats_input = input("Enter your stats seperated by semicolons (e.g., 'Goals:4;Assists:2;Fouls:1'): ")
#     print_stats(stats_input)

#     continue_input = input ("would you like to enter more stats? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break

"""
Exercise 7: The name tag switcheroo

You are developing a playful feature for a social networking app that allows users to swap the first and last characters of
their usernames.
The app takes a username as input and displays the modified version.

**Instructions**:

1. Write a funtion 'swap_characters' that takes a string and returns a new string with the first and last characters swapped.
2. Ensure the function handles usernames of any length, including single-character names.
3. Implement a loop that promps the user to enter their username.
4. Use the function to swap the characters and print the result in a fun and engaging way.
5. Provide the user with the option to try another username or exit the program.

"""

# def swap_characters(username):
#     if len(username) > 1:
#         # coding ==> godinc
#         return username[-1] + username[1:-1] + username[0] # here we are grabing the last letter then adding whats
#         # in the middle and finally grabbing whats up front and moving it to the back
#     return username

# while True:
#     username_input = input("Enter your username to see the magic swap: ")
#     swapped_username = swap_characters(username_input)

#     print(f" Ta-Da! Your magical username is: {swapped_username}")

#     cointune_input = input("want to try another username? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break

"""
Exercise 8: The meeting agenda reverser

Imagine you're developing a feature for a meeting management app that allows users to reverse the order of items in their
meeting agenda.
The app accepts a string representing the agenda items in order and outputs them in reverse order.

**Instructions**:

1. Write a function 'reverse_agenda' that takes a string of agenda items and returns a string with the items in reverse
order.
2. Implement a loop that prompts the user to enter their agenda items separated by commas.
3. Use the function to reverse the order of the agenda items and print the result.
4. Provide the user with the option to enter a new agenda or exit the program.

"""

# def reverse_agenda(agenda_string):
#     # will take our string and it will convert it into a list
#     agenda_items = agenda_string.split(', ')
#     # after the split it will now become ['example1', 'example2', 'example3]
#     # and it will come out like this ['example3', 'example2', 'example1']
#     reverse_agenda = agenda_items[::-1]
#     # example3, example2,
#     return ', '.join(reverse_agenda)

# while True:
#     user_agenda = input("Enter your meeting agenda items separated by commas: ")
#     reverse_order = reverse_agenda(user_agenda)

#     print(f"Reversed agenda order: {reverse_order}")

#     continue_input = input("Would you like to reverse another agenda? (yes/no) ")
#     if continue_input != 'yes':
#         break

"""
Exercise 9: The social media post formatter

In the world of social media, users often like to stylize their posts with unique character replacements.
You're tasked with developing a feature for a social media app that allows users to replace every instance of hte letter
'a' with '@' and 'e' with '3'

**Instructions**:

1. Write a function 'stylize_post' that takes a string and returns a stylized version of it according to the specified
replacements.
2. Impletement a loop that prompts the user to enter their post
3. Use the function to apply the stylization and print the result
4. Provide the user with the option to stylize a new post or exit the program.

"""

# def stylize_post(post_string):
#     stylized_chars= []
#     for char in post_string:
#         if char == 'a':
#             stylized_chars.append('@')
#         elif char == 'e':
#             stylized_chars.append('3')
#         else:
#             stylized_chars.append(char)
#     return ''.join(stylized_chars)

# while True:
#     user_post = input("Enter your social media post: ")
#     stylized_post = stylize_post(user_post)

#     print(f"Stylized post: {stylized_post}")

#     continue_input = ("Would you like to stylize another post? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break

"""
Exercise 10: The custom repetition message generator 

In many user interfaces, there's a need to display a message or a string repeatedly to grab attention or for aesthetic
purposes.
You are tasked with developing a feature for a user interface toolkit that allows users to repeat a string a specified
number of times, with each repetition separated by a dash ('-').

**Instructions**:

1. Write a function 'repeat_message' that takes a string and a number as arguments and returns the repeated string pattern
2. Implement a loop that prompts the user to enter their message and the number of repetitions.
3. Use the function to generate the repeated string pattern and print the result.
4. Provide the user with the option to create a new repeated string pattern or exit the program.

"""

def repeate_message(message, times):
    return '-'.join([message] * times)

while True:
    user_message = input("Enter the message you want to repeate: ")
    repeat_count = int(input("How many times would you like to repeat it? "))

    repeated_message = repeate_message(user_message, repeat_count)

    print(f"Repeated message: {repeated_message}")

    continue_input = input("Would you like to create another repeated message? (yes/no): ").lower()
    if continue_input != 'yes':
        break