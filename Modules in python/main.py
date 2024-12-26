"""
Exercise 1: Building a contact management system

You are tasked with creating a simple contact mangement system for a small business.
The system should enable adding new contacts, viewing all contacts, searching for a specific contact, and deleting a contact.
Each contact should include a name, phone number, and email address.

**Instructions:**

1. **Create a module:**
    - Start by creating a python module ('contact_manager.py') that will contain all the functions for the contact management system.
2. **Design Functions:**
    - Implement the following functions in your module:
        - 'add_contact(contacts, name, phone, email)': Adds a new contact to the contact list
        - 'view_contacts(contacts)': Displays all the contacts
        - 'Search_contacts(contacts, name)' : Searches for a contact by name.
        - 'delete_contact(contacts, name)': Delets a contact by name.
3. **Implement data structures:**
    - Use a list to store all contacts. Each contact should be a dictionary with keys 'name', 'phone', and 'email'.
4. **User Interface:**
    - In your python file ('main.py'), create a user interface using the 'input' function that allows users to choose an action (add, view, search, delete contacts).
5. **Error Handling:**
    - Include try-except blocks to handle errors, such as searching for a non-existent contact or entering invalid data.
6. **Test your system:**
    - Add at least 5 contacts, search for a couple of them delete one, and view the updated contact list to ensure your system is working.
    
**Hints:**

- Remember to import your 'contact_manager' module in 'main.py'.
- Use a loop to continously dispaly the menu until the user decides to exit.
- For searching and deleting contacts, consider iterating over the list and matching the contact's
"""

import contact_manager

def main():
    contacts = []
    while True:
        print("\\n1. Add Contact\\n2. View Contacts\\n3. Search Contact\\n4. Delete Contact\\n5.Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            contact_manager.add_contact(contacts, name, phone, email)
        elif choice == '2':
            contact_manager.view_contacts(contacts)
        elif choice == '3':
            name = input("Enter name to search: ")
            contact = contact_manager.search_contacts(contacts, name)
            if contact:
                print(f"Contact found: {contact}")
            else:
                print("Contact not found.")
        elif choice == '4':
            name = input("Enter name to delete: ")
            if contact_manager.delete_contact(contacts, name) is not None:
                print("Contact delete.")
            else:
                print("Contact not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __main__ == "__main__":
    main()