"""
Exercise 1: E-commerce Product Categorization tool

In the e-commecre industry, managing a diverse range of products can be challenging, especially when dealing with large inventories.
Duplicate entries and unorganized categories can lead to inefficiencies.
Your task is to create a python script that processes a list of product-category pairs, eliminates any duplicates, and categorizes the products neatly.

**Instructions:**

1. Take user input for hte number of products to categorize
2. For each product, accept the product name and its category.
3. Store these inputs in a suitable data structure, ensuring no duplicate product-category pairs.
4. Categorize the products based on their categories and display the organized list.
5. Handle any input erros using try-except blocks.

**Hints:**

- COnsider using a set or a dictionary to store product-category pairs.
- You can use a 'set' to automatically handle duplicate entries.
- Use a loop to iterate through the number of products.
- Utilize string manipulation to process and display the data neatly.
- Implement try-except blocks for handling non-integer inputs for the number of products.
"""

# def categorize_products(num_products):
#     product_categories = set()

#     for _ in range(num_products):
#         try: 
#             product_input = input("Enter product and category: ")
#             product, category = product_input.split(',')
#             product_categories.add((product.strip(), category.strip()))
#         except ValueError:
#             print("Invalid input. Please enter in the format 'product, category'.")

#     categorized = {}
#     for product, category in product_categories:
#         if category not in categorized: # if it's not in our categorized dictionary it will then create the key for us using the category so if we did shirt, nike it would create
#             # nike: [shirt]
#             categorized[category] = []
#         categorized[category].append(product)

#     for category, products in categorized.items():
#         print(f"Category: {category}")
#         for product in products: 
#             print(f" - {product}")



# try:
#     num_products = int(input("Enter the number of products: ")) 
#     categorize_products(num_products)
# except ValueError:
#     print("Please enter a valid integer for the number of products.")

"""
Exercise 2: Social Media Friend Recommendations

In social media platforms, friend recommendations are essential for enchancing user engagement.
These recommendations are often based on mutual friends.
Your task is to create a python script that takes a user's friend list and the friend list of others, indentifies mutual friends, and suggests potential new friends.

**Instructions:**

1. Take user input for hte number of users on the platform
2. For each user, accept their name and a list of their friends.
3. Store these inputs in a suitable data structure, such as a dictionary with user names as keys and sets of friends as values.
4. Take ijnput for the name of hte user for whom you want to generate friend recommendations.
5. Identify potential friends for this user based on mutual friends with their existing friends. 
6. Display the list of recommended friends, excluding the user's name is not found using try-except blocks.

**Hints:**

- Use a dictionary to map each user's name to a set of their friends for efficent access and manipulation.
- Consider using set intersection to find mutual friends.
- Exclude the user's current friends from the recommendation list.
- Implement try-except blocks for handling incorrect user input or non-existent user names.
"""

# def get_friend_recommendations(users, user_name):
#     if user_name not in users:
#         print("User not found")
#         return
    
#     portential_friends = set()
#     for friend in users[user_name]: #here we are looping through the users and adding their friends inout our set
#         portential_friends.update(users[friend])

#     portential_friends.difference_update(users[user_name]) # here we are updating our set and removing items that exist in both sets
#     portential_friends.discard(user_name) # here we are removing our orignal user name so he doesn't show up in friend recommendations


# try:
#     num_users = int(input("Enter the number of users: "))
#     users = {}

#     for _ in range(num_users):
#         name = input("Enter user name: ")
#         friends = set(input("Enter friends (comma-seperated): ").split(','))
#         users[name] = friends

#     user_name = input("Enter the name of the user to get friend recommendations: ")
#     get_friend_recommendations(users, user_name)
# except ValueError:
#     print("Please enter an integer")

"""
Exercise 3: Inventory Mangement for a Retail Store

Efficient inventory management is crucial for retail stores to keep track of their products and categories.
Your task is to create a python script that facilitates adding new products and updating product categories in the store's inventory, represented as a set of products.

**Instructions:**

1. Initialize an empty set to represent the store's inventory.
2. Implement a function to add a new product to the inventory. Each product should have a name and a category. 
3. Implement a function to update the category of an existing product.
4. Provide options for hte user to add a product, update a product's category, or display the current inventory.
5. Ensure that the inventory does not contain duplicate products.
6. Use try-except blocks to handle cases where the user tries to update a non-existent product or inputs invalid data.

**Hints:**

- Use a set to store products, where each product is a tuple containing the product name and category.
- When adding a product, check if it already exists in the inventory.
- For updating a product's category, find the product in the set, remove it, and add a new tuple with the updated category.
- Consider using string manipulation to process and display product details.
"""

def add_product(inventory):
    product_name = input("Enter the product name: ")
    category = input("Enter the product category: ")
    product = (product_name, category)

    if product in inventory:
        print(f"{product_name} already exists in the inventory.")
    else:
        inventory.add(product)
        print(f"{product_name} added to inventory.")

def update_product(inventory):
    product_name = input("Enter the product name to update: ")
    new_category = input("Enter the new category: ")
    product_found = False

    for product in inventory: 
        if product[0] == product_name:
            inventory.remove(product) # here we are removing the product from our inventory
            inventory.add((product_name, new_category)) # Now we're going to be adding it back in but under a new category
            product_found = True
            print(f"{product_name} had been updated to {new_category} category.")
            break

    if not product_found:
        print(f"{product_name} not found in inventory.")

def display_inventory(inventory):
    print("current Inventory: ")
    for product in inventory:
        print(f"product: {product[0]}, Category: {product[1]}")
        
inventory = set()
while True: 
    print("\n1. Add a product")
    print("2. Update a product")
    print("3. Display inventory")
    print("4. Exit")
    choice = input("Enter yoru choice: ")

    if choice == '1':
        add_product(inventory)
    elif choice == '2': 
        update_product(inventory)
    elif choice == '3':
        display_inventory(inventory)
    elif choice == '4':
        break
    else: 
        print("Invalid choice. Please try again.")