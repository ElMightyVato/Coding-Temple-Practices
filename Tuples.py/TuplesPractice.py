"""
Exdercise 1: E-commerce Product Catalog Management

Your task is to develop a system for an online store's product catalog.
This system should enable the addition of new products, display the entire catalog, and allow searching for products by category.

**Instructions:**

1.Implement a function to add products to the catalog. Each product should be represented as a tuple containing the product's name, price, and category. 
2. Create a function to display all products int he catalog. 
3. Develop a search functionality for users to find products by their category.
4. Store all product tuples in a list. 
5. Use exception handling to manage errors, especially for invalid inputs.
6. Implement a text-based user interface using a loop and conditional statements, allowing users to add products, view teh catalog, search by category, or exit the program.

**Hints:**

- Utilize a while loop to keep the program running, presenting a menu of actions until the user decides to exit. 
- Use the 'input()' function for gathering user inputs for adding products.
= Implement a for loop for iterating over the product tuples in the catalog display.
- For searching by category, iterate over the catalog and use an if statement to filter products.
"""

# def add_product(catalog):
#     try:
#         name: input("Enter product name: ")
#         price = float(input("Enter product price: ")) # if they enter a string it will run our value error
#         category = input("enter product category: ")
#         catalog.append((name, price, category)) #Here we append this tuple to our catalog list
#     except ValueError:
#         print("Invalid input. Price must be a number.")
    
# def display_catalog(catalog):
#     for product in catalog:
#         print(f"Name: {product[0]}, Price: {product[1]}, Category: {product[2]}") #name will be at index  0 price will be index location 1 and finally category will be
#         # index location 2

# def search_category(catalog):
#     category = input("Enter category to search: ")
#     found = [product for product in catalog if product[2].lower() == category.lower()] # here we are converting our category to .lower so that no matter how they type it, it will
#     # be converted to lower so CloThes.lower() --> clothes == clothes
#     if found:
#         for product in found:
#             print(f"Name: {product[0]}, Price: {product[1]}")
#     else:
#         print("No products found in this category.")

# def main():
#     catalog = [] # our empty list to store catalog
#     while True:
#         print("\n1. Add a product")
#         print("2. View catalog")
#         print("3. Search by category")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             add_product(catalog)
#         elif choice == '2':
#             display_catalog(catalog)
#         elif choice == '3':
#             search_category(catalog)
#         elif choice == '4':
#             print("exiting the program.")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __main__ == "__main__":
#     main()

"""
Exercise 2: Library catalog access system

You are tasked with creating a system for a library that allows users to view book details, search for books by title and list all books in a specific genre. 
Each book in the catalog is represented as a tuple containg the book's title, author, and genre.

**Instructions:**

1. Create a tuple to store multiple books, with each book represented as a sub-tuple.
2. Implement a function to display details of all books in the catalog.
3. Create a function to search for a book by its title and display its details
4. Implement a function to list all books in a specific genre.
5. Ensure the program handles cases where a book or genre is not found.
6. Use a loop and conditional statements to allow users to select different functionalities (e.g., view all books, search by title, list by gengre, exit).

**Hints:**

- Consider using a for loop and if statements within your search and list functions to iterate over the tuple and find matches.
- The 'in' keyword can be helpful for string comparisons when searching for titles or genres.
- Use the 'input()' function for user inputs and 'print()' for displaying information. 
"""

# def display_catalog(catalog):
#     for book in catalog:
#         print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")

# def search_by_title(catalog):
#     title = input("Enter book title to search: ").lower() # we need a variable that has an input that lets us do the searching and convert it to .lower
#     found = False
#     for book in catalog:
#         if book[0].lower() == title: # if our book at index 0 .lower is equal to the title we type
#             print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")
#             found == True
#             break
#     if not found: 
#         print("Book not found.")

# def list_by_genre(catalog):
#     genre = input("Enter genre to list books: ").lower()
#     found = False 
#     for book in catalog: 
#         if book[2].lower() == genre: 
#             print(f"Title: {book[0]}, Author: {book[1]}")
#             found = True
#         if not found: 
#             print("No books found in this genre.")

# def main():
#     catalog = (
#         ("To kill a Mockingbird", "Harper Lee", "Classic"),
#         ("1984", "George Orwell", "Dystopian"),
#         ("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
#         ("Brave New World", "Aldous Huxley", "Dystopian")
#     )

#     while True:
#         print("\n1. View all books")
#         print("2. Search by title")
#         print("3. List by genre")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             display_catalog(catalog)
#         elif choice == '2':
#             search_by_title(catalog)
#         elif choice == '3':
#             list_by_genre(catalog)
#         elif choice == '4':
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice, plase try again.")

# if __name__ == "__main__":
#     main()

"""
Exercise 3: Employee Task Tracker

**Problem Statement:**
You are developing a system to track tasks assigned to employees in a department. Each task is assigned to an employee and has a deadline. 
The system should allow managers to veiew all tasks, add new tasks, and mark tasks as completed.

**Instructions:**

1. Store tasks in a list, where each task is a tuple containing the employee's name, task descrioption, and deadline.
2. Implement a function to add new tasks to the system.
3. Create a function to display all tasks, unpacking the tuple to show each task's details. 
4. Develop a function to mark a task as completed, which removes it from the list.
5. Handle user input for different functionalities (e.g., add a task, view tasks, complete a task, exit).
6. Use loops and conditional statements for hte programs's flow and decision-making.

**Hints:**

- Use tuple unpacking to display each component of a task when listing tasks. 
- When adding or completing tasks, ensure that the user's input is handled effectively.
- Loop through the list of tasks to display or update the task list as needed.
"""

# def add_task(tasks):
#     name = input("Enter employee's name: ")
#     description = input("Enter task description: ")
#     deadline = input("Enter deadline (dd/mm/yyyy): ")
#     tasks.append((name, description, deadline)) # once they enter the input we will append it into a tuple

# def display_tasks(tasks):
#     for task in tasks: 
#         name, description, deadline = task
#         print(f"Employee: {name}, Tasks: {description}, Deadline: {deadline}")

# def complete_task(tasks):
#     task_to_remove = input("Enter the description of the completed task: ")
#     for i, task in enumerate(tasks): # here we are checking if task 1 is equal to the task we want to remove
#         if task[1] == task_to_remove:
#             del task[i] # if it does we will delete that from the current task list
#             print("Task completed and removed.")
#             break
#     else:
#         print("Task not found.")

# def main():
#     tasks = []
#     while True:
#         print("\n1. add a task")
#         print("2. View Tasks")
#         print("3. Complete a task")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             add_task(tasks)
#         elif choice == '2':
#             display_tasks(tasks)
#         elif choice == '3':
#             complete_task(tasks)
#         elif choice == '4':
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()

"""
Exercise 4: Weather Data Analysis

You are developing a system for a meterological department to process and display historical weather data.
The data includes daily weather records stored as tuples, each containing the date, average temperature, and precipitation level.

**Instructions:**

1. Store the weather data in a list, with each record represented as a tuple.
2. Implement a function to calculate and display the average temperature for hte entire dataset.
3. Create a function to find and displaay the day(s) with the highest precipitation level.
4. Develop a function to list all records for days with temperatrures above a user-specified threshold.
5. Ensure the program allows users to select different functionalities (e.e., calculate average temperatrure, find highest preciptiation, list hot days, exit).
6. Use loops and conditional statements to iterate over the tuple data and perform the required analyses.

**Hints:**

- When calculating averages or maximum values, consider initializing variables to store cumulative totals or maximum records.
- Use a for loop to iterate over the list of tuples, processing each record as needed.
- Utilize conditional statements within the loop to filter or compare data based on the criteria.
"""

# def calculate_average_temperature(weather_data):
#     total_temp = sum(record[1] for record in weather_data)
#     average_temp = total_temp / len(weather_data)
#     print(f"Average temperature: {average_temp:.2f}")

# def find_highest_precipitation(weather_data):
#     max_precipitation = max(weather_data, key=lambda record: record[2]) # first with the max funciton grabs the largest number now we're specifing a key and waht lambda does is
#     # an ananmoys function so it only targets the precipitation levels
#     print(f"Highest precipitation on: {max_precipitation[0]}, level: {max_precipitation[2]}")

# def list_hot_days(weather_data):
#     threshold = float(input("Enter temperature threshold: "))
#     hot_days = [record for record in weather_data if record[1] > threshold]
#     for day in hot_days:
#         print(f"Date: {day[0]}, Temperature: {day[1]}, Precipitation: {day[2]}")

# def main():
#     weather_data = [
#         ("01/01/2020", 50, 5),
#         ("02/01/2020", 60, 10),
#         ("03/01/2020", 80, 7)
#     ]

#     while True:
#         print("\n1. Calcualte Average Temperature")
#         print("2. Find Highest precipitation")
#         print("3. List hot days")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             calculate_average_temperature(weather_data)
#         elif choice == '2':
#             find_highest_precipitation(weather_data)
#         elif choice == '3':
#             list_hot_days(weather_data)
#         elif choice == '4':
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()

"""
Exercise 5: Flight Itinerary Planner

You are tasked with creating a system for an airline company that organizes flight itineraries.
Each itinerary consists of a series of flights, where each flight is represented as a tuple containing the flight number, departure, and arrival cities. 
Itineraries are also tuples, containing multiple flights and the traveler's name.

**Instructions:**

1. Store multiple itineraries in a list, with each itinerary represented as a nested tuple.
2. Implement a function to display all itineraries, including the details of each flight in the itinerary.
3. Create a function to find and display itineraries for a specific traveler.
4. Develop a function to list all itinerarires that include a specific city as a departure point.
5. Ensure the program allows users to choose between different functionalities (e.g., view all itineraries, search by traveler, list itineraries from a city, exit).
6. Use nested loops and conditional statements to navigate through the nested tuple data.

**Hints:**

- Use nested for loops to iterate over the itineraries and the flights within each itinerary.
- For searching functionalities, iterate through the itineraries and use conditional statements to check for matching criteria.
"""

# def display_itineraries(itineraries):
#     for itinerary in itineraries:
#         traveler, flights = itinerary[0], itinerary[1:]
#         print(f"\nTraveler: {traveler}")
#         for flight in flights:
#             print(f" Flight: {flight[0]}, From: {flight[1]}, To {flight[2]}")

# def find_itinerary_by_traveler(itineraries, traveler_name):
#     for itinerary in itineraries:
#         if itinerary[0].lower() == traveler_name.lower():
#             print(f"\nItinerary for {traveler_name}: ")
#             for flight in itinerary[1:]:
#                 print(f" Flight: {flight[0]}, From: {flight[1]}, To: {flight[2]}")
#             break
#     else:
#         print("No itinerary found for this traveler.")

# def list_itineraries_from_city(itineraries, city):
#     print(f"\nItineraries from {city}:")
#     for itinerary in itineraries:
#         for flight in itinerary[1:]:
#             if flight[1].lower() == city.lower():
#                 print(f"Traveler: {itinerary[0]}, Flight: {flight[0]}, To: {flight[2]}"))

# def main():
#     itineraries = [
#         ("Alice", ("FL123", "New York", "London"), ("FL456", "London", "Paris")),
#         ("Bob", ("FL789", "Tokyo", "San Francisico"), ("FL321", "San Francisico", "New York")),
#     ]

#     while True:
#         print("\n1. View all itineraries")
#         print("2. Search itinerary by traveler")
#         print("3. List itineraries from a city")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             display_itineraries(itineraries)
#         elif choice == '2':
#             traveler = input("Enter traveler's name: ")
#             find_itinerary_by_traveler(itineraries, traveler)
#         elif choice == '3':
#             city = input("Enter departure city: ")
#             list_itineraries_from_city(itineraries, city)
#         elif choice == '4':
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()