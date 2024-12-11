"""
Exercise 1: E-commerce Product Catalog Management

Develop a Python program to manage a product catalog for an e-commerce platform.
The program should facilitate adding new product categories, adding products to existing categories, displaying all
available categories, and searching for products within the catalog.

**Instructions:**

1. Initialize a dictionary to represent the product catalog
2. Implement functions for:
    - Adding a new product category
    - Adding a product to an existing category
    - Displaying all categories and their respective products.
    - Searching for a product across all categories (case-insensitive).
3. Use exception handling to address potential errors, such as adding products to non-existent categories.
4. Implement case-insensitive search functionality for product queries.

**Hints:**

- Start with a pre-populated dictionary for ease of testing.
- Utilize string methods like 'lower()' for case-insensitive comparisons.
- In the search function, interate through all categories to find the product.
- Implement 'try' and 'except' blocks to gracefully handle situations where a specified category does not exist in the catalog.

"""

# def add_category(catalog, category): #catalog is our dictionary and category is our keys
#     if category not in catalog: # so if the key we entered is not in our dictionary we add it to the dictionary
#         catalog[category] = []
#         print(f"Category '{category}' added.")
#     else: # If it is in the dictionary it will not allow us to add it and print out the following text below
#         print(f"Category '{category}' already exists.")

# def add_product(catalog, category, product): # the catalog is our dictionary the category are the keys and the product
#     # is our values
#     try:
#         if product not in catalog[category]: #so if the product we want to add which is the value doesn't exist it will
#             # add it to the category
#             catalog[category].append(product)
#             print(f"Product '{product}' added to '{category}'.")
#         else:
#             print(f"Product '{product}' already exists in '{category}'.")
#     except KeyError:
#         print(f"category '{category}' does not exist.")

# def display_categories(catalog):
#     for category, products in catalog.items(): # category would be our key and products is the list within it
#         print(f"{category}: {', '.join(products)}")

# def search_product(catalog, product):
#     found = False
#     for category, products in catalog.items(): # here we are looping through the keys and then values and doing dictionary
#         # items to locate the product
#         if product.lower() in [p.lower() for p in products]: # here no matter what we type for product it will convert it 
#             # to lower so if we did laptop it'll convert Laptop to laptop
#             print(f"Product '{product}' found in '{category}'.")
#             found = True
#             break
#     if not found:
#         print(f"Product '{product}' not found.")

# catalog = {                         # This is our dictionary which contains the keys of electronics and books
#     "Electronics": ["Laptop", "Smartphone"],
#     "Books": ["Fiction", "Non-Fiction"]
# }

# add_category(catalog, "Clothing") # Here we are calling the function and pass in our catalog dictionary
# # and then we inputting Clothing as a (catagory) key we want to add

# add_product(catalog, "Electronics", "Camera")
# display_categories(catalog)
# search_product(catalog, "laptop")
# print(catalog)

"""
Exercise 2: Social Media Content Organizer

Develop a python program to manage and organize social media content. 
The Program should categorize posts into different social media platforms (e.g., Facebook, Instagram),
and further categories these posts into types (e.g., Text, Image, Video).

**Instructions:**

1. Create a nested dictionary where the first level represents social media platforms and the second level categorizes the types of
posts. 
2. Implement functions to:
    -add a new social media platform to the dictionary
    -add a new post type to a specific platform
    -add a post to a specific type within a platform
    -display all platforms, post types, and posts
3. Ensure that the program can handle adding new platforms and post types dynamically.

**Hints:**

-Initialize your dictionary with at least two platforms and a few post types.
-Use nested loops to iterate through the platforms and their posts types when displaying content
-Implement checks to handle the addition of already existing platforms or post types.
"""

# def add_platform(content_dict, platform): #
#     if platform not in content_dict:
#         content_dict[platform] = {}
#         print(f"Platform '{platform}' added.")
#     else:
#         print(f"Platform '{platform}' already exists.")

# def add_post_type(content_dict, platform, post_type): # The platform is looking for facebook insta etc. and the post type will be what kind of post
#     if platform in content_dict: # First we check if the platform we're inputting is in the platform if it is the following code runs
#         if post_type not in content_dict[platform]: # Now here we check if our post type is not already in the platform we selected
#             content_dict[platform][post_type] = [] # if it's not in there we add it in as an empty list
#             print(f"Post type '{post_type}' added to '{platform}'.")
#         else:
#             print(f"Post type '{post_type}' already exists in '{platform}'.") # if it is it won't create it
#     else:
#         print(f"Platform '{platform}' does not exist.")

# def add_post(content_dict, platform, post_type, post):
#     if platform in content_dict and post_type in content_dict[platform]: # Here we are checking if the platform and post type exists
#         content_dict[platform][post_type].append(post) # if it exists we grab our dictionary, then select the platform and finally the post type
#         print(f"Post added to '{platform}' under '{post_type}'.")
#     else:
#         print(f"Either platform '{platform}' or post type '{post_type}' does not exist.") # If it does not exist we let the user know it's either the platform ot post type

# def display_content(content_dict):
#     for platform, post_types in content_dict.items(): # we are looping through this using .items so first we are grabbing the plat form and then the dictionary
#         print(f"Platform: {platform}")
#         for post_type, posts in post_types.items(): # Now we are looping through the post type and posts
#             print(f" Post Type: {post_type}")
#             for post in posts: # Now we loop through this list in posts and print each one individually
#                 print(f"   - {post}")

# social_media_content = {
#     "Facebook": {
#         "Text": ["Hello World", "Python is fun!"],
#         "Image": ["Beach photo", "Birthday party"]
#     }
# }

# add_platform(social_media_content, "Instagram")
# add_post_type(social_media_content, "Instagram", "Image")
# add_post(social_media_content, "Instagram", "Image", "sunset view")
# display_content(social_media_content)

"""
Exercise 3: Restuarant Menu and Order Management

Create a python program to manage a restuarant's menu and customer orders. 
The program should allow for menu management (adding/removing items and categories) and handling customer orders by seleecting items from the menu

**Instructions**

1. Define a dictionary to represent the restaurant's menu, with categories as keys and lists of menu items as values.
2. Implement functions for:
    - Adding and removing menu categories
    - Adding and removing items within a category.
    - Taking a customer's order by selecting items from the menu.
    - Displaying the complete menu and individual customer ordedrs.
3. Include error handling for cases like attempting to order an item not on the menu.

**Hints:**

- Start with a pre-defined menu
- Use 'try' and 'except' for handling invalid order requests.
- Consider using a list to store individual customer orders.
"""

# def add_category(menu, category): 
#     if category not in menu: # we check to see if the category is not in the menu
#         menu[category]= [] # if it's not in the menu it will create it along with an empty list
#         print(f"Category '{category}' added.")
#     else:
#         print(f"Category '{category}' already exists.")

# def add_item(menu, category, item):
#     if category in menu: # we check if the category we input is in our menu so if beverage in restuarant_menu
#         if item not in menu[category]:  # Now we check to see if the item is in our category 
#             menu[category].append(item)
#             print(f"Item '{item}' added to '{category}'.")
#         else:
#             print(f"Item '{item}' already exists in '{category}'.")
#     else:
#         print(f"Category '{category}' does not exist.")
 
#  def take_order(menu, order): 
#     try: # creates an order items variable and sets it equal to a list grabbing the menu at the category at the item index
#         order_items = [menu[category][item_index] for category, item_index in order]
#         return order_items
#     except (KeyError, IndexError):
#         print("Invalid order. Please check menu and order again.")
#         return None
    
# def display_menu(menu):
#     for category, items in menu.items(): #here we are looping through our menu using .items
#         print(f"{category}: {', '.join{items}}")
    
# customer_order = [("Main Course", 1), ("Desserts", 0)] #Variable we just created so in it we have what the customer wants to order
# # so main course would be salmon and desserts would be cake


# restaurant_menu = {
#     "starters": ["Soup", "Salad"],
#     "Main Course": ["Steak", "Salmon", "Pasta"],
#     "Desserts": ["Cake", "Ice Cream"]
# }

# order_items = take_order(restaurant_menu, customer_order) # here we pass in the restuarnt menu and the customer order going back to our function so our try 1.
# if order_items:
#     print("Customer order:", order_items)

"""
Exercise 4: Hotel Room Booking System

Develop a system to track and manage room bookings for a hotel.
The program should allow adding rooms, checking room availability, booking rooms, and displaying current bookings.

**Instructions:**

1. Use a dictionary to represent the hotel rooms, where keys are room numbers and values are boolean indicating availabilty.
2. Implement functions for:
    - Adding new rooms to the hotel
    - Checking if a room is avaialable
    - Booking a room
    - Displaying all rooms and their current status.
3. Incorporate a main loop that allows users to choose different actions (e.e., add room, book room, etc.).
4. Use exception handling for invalid inputs or actions, such as attempting to book an already occupied room.

**Hints:**

- Initialize your dictionary with a set of rooms
- Use a while loop for the main program execution, allowing continous operation until the user decides to exit. 
- When booking, check the room's availability before confirming the booking.

"""

# def add_room(hotel, room_number):
#     if room_number not in hotel:
#         hotel[room_number] = True # True indicates room is available 
#         print(f"Room {room_number} added.")
#     else:
#         print(f"Room {room_number} already exists.")

# def is_available(hotel, room_number):
#     return hotel.get(room_number, False) #.get helps get the room number and states if hte room is available

# def book_room(hotel, room_number):
#     if is_available(hotel, room_number): # if the room is avaialibe it will run the code below and set it to false since we're booking it
#         hotel[room_number] = False
#         print(f"Room {room_number} booked.")
#     else:
#         print(f"Room {room_number} is not available or does not exist.")

# def display_rooms(hotel):
#     for room, available in hotel.items():
#         status = "Available" if available else "Booked"
#         print(f"Room {room}: {status}")

# hotel_rooms = {"101": True, "102": False, "103": True} # our hotel rooms dictionary

# while True:
#     print("\nHotel Management System")
#     print("1: Add Room\n2: Book Room\n3: Check Room Availability\n4: Display Rooms\n5: Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         room = input("Enter room number to add: ")
#         add_room(hotel_rooms, room)
#     elif choice == "2":
#         room = input("Enter room number to book: ")
#         book_room(hotel_rooms, room)
#     elif choice == "3":
#         room = input("Enter room number to check availabitility: ")
#         available = is_available(hotel_rooms, room)
#     elif choice == "4":
#         display_rooms(hotel_rooms)
#     elif choice == "5":
#         print("Exiting system.")
#         break
#     else:
#         print("Invalid choice. Please try again.")

"""
Exercise 5: Customer Feedback Analysis for a product

Create a system to categorize and count customer feedback based on sentiment (positive, negative, neutral) for a specific product. 
The program should allow adding new feedback, displaying sentiment counts, and showing all feedback for a specific sentiment.

**Instructions:**

1. Use a dictionary to store customer feedback, categorized by sentiment.
2. Implement functions to:
    - Add new feedback with a specified sentiment.
    - Display the count of feedback for each sentiment.
    - Show all feedback messages for a specific sentiment.
3. Utilize built-in dictionary methods to efficiently manage and access the feedback data.
4. Ensure the program handles cases where no feedback is available for a given sentiment.

**Hints:**

- Initialize your dictionary with empty lists for each sentiment category.
- Consider using the 'get()' method for safely retrieving feedback for a sentiment.
- Use string methods for standaridizing feedback inputs (e.g., converting to lowercase for uniformity).
 """

def add_feedback(feedback_dict, sentiment, message): # this is going to target our feedback_dictionary and sentiment will be targeting our keys positive, negative, neutral
    # then it will add in what ever message in the brackets
    feedback_dict.setdefault(sentiment.lower(), []).append(message) #this checks if our sentiment.lower is withing our dictionary if it does exist it will append the message
    # if it doesn't it will instead create an empty list
    print(f"Feedback added to '{sentiment}' category.")

def display_feedback_count(feedback_dict): # here we are taking in our dictionary
    for sentiment, messages in feedback_dict.items(): #now we are looping through the sentiments and messages with .items
        print(f"{sentiment.title()}: {len(messages)} feedbacks(s)") #here we are showing them how many messages we have per sentiment so for positive if there are 5 messages it will
        # be positive: 5 feedbacks(s)""

def show_feedback_for_sentiment(feedback_dict, sentiment): # So here we are targeting our feedback dictionary 
    messages = feedback_dict.get(sentiment.lower(), []) # if the sentiment exists it will bring back the array if it doesn't exist it will provide an empty array
    if messages:
        print(f"Feedback for '{sentiment}':")
        for message in messages:
            print(f"- {message}")
    else:
        print(f"No feedback available for '{sentiment}'.")

customer_feedback = {"Positive": [], "Negative": [], "Neutral": []} # this is our customer feedback dictionary

add_feedback(customer_feedback, "overwhelminly positive", "Great Product!")















