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






















