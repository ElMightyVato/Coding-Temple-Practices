"""
Exercise 1: City Library Management System

To Create a Python program that manages book records in a city library system, allowing for adding, searching, lending, and returning books

**Problem Statment:**
The city library needs a digital system to keep track of its books.
The system should allow library staff to add new books, search for books by title, lend books to members, and receive returned books
Each book should have a title, author, and an availability status.

**Instructions:**

1. **Define a book class**:
    - Include attributes for title, author, and availabitilty.
    - Define methods for checking out and returning a book, which update the availaibiltiy status.
2. **Create a library class**:
    - Store a collection of books.
    - Include methods to add books, search for a book by title, lend a book, and return a book.
3. **Implement user Interaction**:
    - Use input functions to allow staff to add, search, lend, return books.
    - Use loops and conditional statements to handle different user actions.
4. **Error Handling**:
    - Implement try-except blocks to handle situations like searching for a book that doesn't exist or lending out an already lent book
5. **Data Structures**:
    - Use a list to store the collection of book objects in the library class.
    - Use a dictionary or a sett for effiecent searching of books by title.
    """

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_avilable = True

    def check_out(self):
        if self.is_avilable:
            self.is_avilable = False
            return True
        return False
    
    def return_book(self):
        self.is_avilable = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def lend_book(self,title):
        book = self.find_book(title)
        if book and book.check_out():
            print(f"Book '{title}' has been lent out.")
        else:
            print(f"Book '{title}' is not avaialbe")

    def return_book(self, title)
        book = self.find_book(title)
        if book:
            book.return_book()
            print(f"Book '{title}' has been returned.")
        else:
            print(f"Book '{title}' not found in library")

library = Library()

while True:
    action = input("Enter action (add, lend, return, search, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == 'add':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(book(title, author))
            print(f"Added book '{title}'.")
        elif action == 'lend':
            title = input("Enter book title to lend: ")
            library.lend_book(title)
        elif action == 'return':
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif action == 'search':
            title = input("Enter book title to search: ")
            book = library.find_book(title)
            if book:
                availability = "available" if book.is_available else "not available"
                print(f" {title} by {book.author} is {availability}.")
            else:
                print(f"Book {title} not found.")
    except Exception as e:
        print(f"An error occured: {e}")

print("Library system closed.")