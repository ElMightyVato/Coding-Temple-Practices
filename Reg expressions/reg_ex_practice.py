"""
Exercise 1: E-Commerce Product Data Extraction

In an e-commerce setting, you are faced with a large text file containing detailed product information.
The challenge is to parse this semi-structured data to extract relevant details such as product IDs, names, categories,
and prices, and then store this information for easy access and analysis

**Instructions:**

1. Read a string that contains product information (simulating data from a file).
2. Implement a regex pattern to identify and extract the necessary product details.
3. Store and organize the extracted data into a structured format, like al ist of dictionaries.
4. Incorporate error handling for portential data parsing issues.
5. Display the organized data in a readable format for end-users.

**Hints:**

- Utilize 're.findall()' for pattern-based data extraction
- Craft a regex pattern tailored to the specific data format of the product details.
- Use dictionaries for storing individual product data, and a list to hold all products.
- Implement loops to process and store each extracted product
- Apply try-except blocks to gracefully handle any parsing errors.
"""

# import re


# def extract_product_info(data):
    
#     product_pattern = r"Product ID: (\d+), Name: (.*?), Category: (.*?), Price: \$(\d+\.\d+)"

#     try: 
#         products = re.findall(product_pattern, data)
#         product_list = []
#         print(products) # to visualize what's going on
#         for product in products: 
#             # Creating a dictionary for each product
#             product_dict = {
#                 "ID": product[0],
#                 "Name": product[1],
#                 "Category": product[2],
#                 "Price": product[3]\
#             }
#             product_list.append(product_dict)
#         return product_list
#     except Exception as e:
#         print("An error occured:" , e)
#         return []

# data = """Product ID: 1001, Name: Alpha widget, Category: widgets, Price: $9.99
#             Product ID: 1002, Name: Beta widget, Category: widgets, Price: $29.99
#             Product ID: 1003, Name: Gamma Gadget, Category: Gadgets, Price: $9.99"""\
            
# #Extracting and displaying product information
# product_info = extract_product_info(data)
# for product in product_info:
#     print(f"Product ID: {product['ID']}, Name: {product['Name']}, Category: {product['Category']}, Price: ${product['Price']}")

"""
Exercise 2: Marketing campaing email validator 

You are tasked with preparing an email list for an upcoming marketing campaign.
The list contains various email addresses, some of which may not be in the correct format. Your goal is to validate these email addresses, 
filter out invalid ones, and compile a list of valid email addresses for hte campaign.

**Instructions:**

1. Read a list of email addresses (simulated through a predefined list)
2. Implement a regex pattern to validate the email addresses.
3. Store valid email addresses in one list and invalid ones in another
4. Handle any errors that might occur during validation
5. Display both lists of valid and invalid email addresses.

**Hints:**

- Use 're.match()' with an appropriate regex pattern to validate each email address
- Iterate through the list of emails, applying the validation regex to each.
- Store email addresses in separate lists based on their validity
- Use try-except blocks to handle exceptions during hte validation process.
"""

import re








