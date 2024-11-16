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
and further cate"""




























