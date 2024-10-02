# marshmallows = 0
# while marshmallows < 5:
#     marshmallows += 1
#     print("added a marshmallow! Now there are " + str(marshmallows) + " marshmallows!")

# marshmallows = 0 
# while marshmallows < 5: 
#     print("planning to add a marshmallow! Currently, there are " + str(marshmallows) + " marshmallows.")
#     marshmallows += 1

# temperature = 100
# while temperature < 0:
#     temperature -= 1
#     print(f"the temperature is now:", {temperature})
# print("The Temperature was never below 0 to begin with.")

# while True:
#     user_input = input("say 'stop' to end the refill: ")
#     if user_input.lower() == 'stop':
#         break
#     else:
#         print("here's more coffee!")

# steps = 10

# while steps > 0:
#     print("descending the stairs, " + str(steps) + " Steps reaming.")
#     steps -= 1
# print("we've reached the ground floor!")
"""
# exercise 1: The Countdown Timer 

# You are programming a countdown timer for a game that starts 
# from a specified number and counts down to zero. You need to display each number as the timer counts down.

# Here are the tasks you need to perform:

# 1. Initialize a variable with the starting number of the countdown.
# 2. Use a while loop to keep the countodwn going as long as the timer is greater than zero.
# 3. Inside the loop, decrease the timer by one and then print the current value of the timer. 
# 4. Once the countdown reaches zero, print a message indicating that the time is up. 
"""
# timer = 10

# while timer > 0:
#     print("Game is starting in ", timer , " seconds!")
#     timer -= 1
# print("Begin the game!")

"""Exercise 2: The Patient Queue 

You are developing a system for a clinic's reception desk that tracks the number of patients waiting and
calls them one by one until no one is left in the queue.

Here are the tasks you need to perform:

1. Initialize a variable with the total number of patients in the queue.quit
2. Use a 'while' loop to simulate calling each patient until the queue is empty.
3. Inside the loop, decrement the number of patients as each one is called.
4. Print a message each time a patient is called and when the queue is empty.

**Hint**:
make sure to decrease the number of patients in the queue to reflect that a patient has been called. """

# patients = 5

# while patients > 0:
#     print(f"Patient number {patients} please come in.")
#     patients -= 1 # patients = patients - 1
#     # will keep repeating until patients reaches 0

# print("That's all the patients!")

"""
Exercise 3: The Battery Charger with Efficiency check

You are programming a smart battery charger that not only charges a battery but also performs efficiency checks at 
certain milestones.
The battery starts at 0% and charges in increments. If the battery reaches 50% effiency, it charges faster. If it reaches
80% it slows down to preven overcharging.

Here are the tasks you need to perform:

1. Initialize a variable to represent the battery charge level.
2. Use a 'while' loop to charge the battery in increments.
3. Inside the loop, use 'if' statements to check the charge level.
4. If the charge level is 50%, increase the charging increments.
5. If the charge level reaches 80%, decrease the charging increments to prevent damage.
6. Print the battery level at each increment and a message when the battery is fully charged.

**Hint**:
You will need to adjust the increment value within the 'while' loop based on the charge level.

"""
#my solution

# battery = 0

# while battery < 100:
#     if battery < 50:
#         print(f"Beggining charge current battery: {battery}%.")
#         battery += 10
#     elif battery < 80:
#         print(f"Battery is now over 50% increasing charge to 15% current battery: {battery}")
#         battery += 15
#     else:
#         print(f"Battery is almost charged! Decreasing charge levels to 10% so it doesn't overheat current battery: {battery}%")
#         battery += 10
# print("Fully charged!")

# # Professors solution

# battery = 0
# increment = 10

# while battery < 100:
#     battery += increment
#     print(f"Battery is now at {battery}%")

#     if battery == 50:
#         print("efficiency check: Increasing charge rate.")
#         increment = 15
#     elif battery == 80:
#         print("efficiency check: Reducing charge rate to prevent overheating.")
#         increment = 5

# print("The battery is now fully charged.")

"""
Exercise 4: The Smart Coffee Machine

You are programming a smart coffee machine that dispenses different types of coffee until the reservoir is empty.
The machine has alist of coffee types it can dispense, and it should offer each type in order until it runs out of water.
Once a coffee type is offered, it should be removed from the list.

Here are the tasks you need to perform:

1.Initialize a variable to represent the coffee reservoir level.
2. Create a list of coffee types that the machine can dispense.
3. Use a 'while' loop to dispense coffee until the reseroir is empty.
4. Inside the loop, use an 'if' statement to check if there are still coffee types available.
5. Dispense each type of coffee and then remove it from the list.
6. Print the type of coffee dispensed and the remaining coffee types in the list.
7. Print a message when the coffee reservoir is empty.

**Hint**:
You will need to use list methods to remove coffee types once they are dispensed.

"""    

# coffee_reservoir = 10 # Amount of water in my coffee machine

# coffee_types =["Espresso", "Cappuccino", "Latte", "Americano", "Mocha"] # List of coffee types

# while coffee_reservoir > 0: # As long as water is over 0 this will run
#     if coffee_types: # Here we are checking if there is something in our coffee_types list
#         current_coffee = coffee_types.pop(0) #pop is removing the item from the list and we are also using current_coffee
#         # for the one item in our next print statement
#         print(f"Dispensing {current_coffee}.")

#         coffee_reservoir -= 1 # Each time we select a coffee type we reduce our reservoir variable by 1
#         print(f"Coffee types left: {coffee_types}")
#     else:
#         print("no more coffeee types available.")
#         break # if we don't have a break this will keep printing constantly.
# print("The coffee reservoir is empty")

"""
Exercise 5: The Intelligent Elevator System

You are designing an intelligent elevator system. The elevator has a list of floors where passengers have requested stops.
Write a 'while' loop that starts from the top floor and stops at each requested floor until it reaches the ground floor.

Here are the tasks you need to perform:

1. Initialize a variable for the starting floor.
2. Create a list of floors where passengers have requested stops.
3. Use a 'while' loop to move the elevator down floor by bloor.
4. Inside the loop, use the membership operator to check if hte current floor is in the list of requested stops.
5. If the current floor is a requested stop, print a message and remove that floor from the list.
6. Continue moving down until the ground floor is reached. 
7. Print a message each time the elevator moves down a floor and when it reaches the ground floor.

**hint**:
You will need to use list methods to remove floors from the list once they are visited.
"""

# current_floor = 5

# requested_stops = [1,3,4]

# while current_floor > 0:
#     if current_floor in requested_stops:
#         print(f"Stopping at floor {current_floor}")
#         requested_stops.remove(current_floor)
#     current_floor -= 1 #we want this out of the if statement so it can run well
#     print(f"Descending to floor {current_floor}.")

"""
Create a list of colors representing the traffic light sequence.
Initialize a counter for the green light
Use an infinite while loop to cycle through the traffic light colors.
Inside the loop, use the count method to track the number of times 'green' appears
Break the loop when the green light has appeared a specific number of times.
Print a message each time the oight changes and when the loop breaks for maintenance"""

# traffic_lights = ['red', 'yellow', 'green', 'yellow']
# green_count = 0

# while True:
#     for color in traffic_lights:
#         print(f"The traffic light is now {color}.")
#         if color == 'green':
#             green_count += 1
#             if green_count == 3:
#                 print("maintenance time! The cycle will stop.")
#                 break

#     if green_count == 3:
#         break

