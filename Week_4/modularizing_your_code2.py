#1. Import the whole module

import math


# Lets put it to use

print(math.sqrt(9))
# - Note that you must specify the module name when calling a function within it.

# 1. import as an alias

import math as m

# lets put it to use

print(m.sqrt(25))

# - This shortens the module name, this is common with libraries like numpy, pandas, etc

# 3. Import specific functions or variables

from math import sqrt, pie

print(sqrt(36))
print(pie)

# - here you dont need the prefix 'math.' anymore

# 4. Import everything from the module

from math import *

print(sqrt(49))
print(pi)

# - This is usually not recommended because it can cause name conflits if two modules have functions with the same name

# my_module/first.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
    
# my_module/second.py

def greet(name):
    return f"Hello, {name}! I am creating my own module"


def reverse_string(string):
    return string[::-1]


def count_characters(string):
    return len(string)


def count_words(string):
    return len(string.split())

# my_module/main.py

import first
import second

# lets use the functions in the first.py file


print("=== Math Functions ===")
print("5 + 3 =", first.add(5, 3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))

# Lets us the functions in the second.py file
print("\n=== String Functions ===")
print(second.greet("Ridwan"))
print("Reverse of 'Python' =", second.reverse_string("Python"))
print("Character count in sentence =", second.count_characters("Python modules are powerful"))
print("Word count in sentence =", second.count_words("Python modules are powerful"))


# __init__.py
print("my_package is being imported")

# Optional: import functions directly for easier access
from .math_utils import add, subtract
from .string_utils import capitalize_text

# math_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# string_utils.py

def capitalize_text(text):
    return text.capitalize()

def reverse_text(text):
    return text[::-1]

# string_utils.py

def capitalize_text(text):
    return text.capitalize()

def reverse_text(text):
    return text[::-1]

# data.py

students = []

def add_student(name, track):
    students.append({"name": name, "track": track})

def get_students():
    return students

# utils.py

def format_student(student):
    return f"{student['name']} is learning {student['track']} at NCC Digital Industrial Park, Abeokuta."

# main.py → Project entry point

# main.py

import data
import utils

# Add some students
data.add_student("Paul", "AI Engineering")
data.add_student("Blessing", "AI Development")

# Print formatted student records
for s in data.get_students():
    print(utils.format_student(s))

# data/data.py - This will handle data storage

books = []

def add_book(title, author):
    books.append({"title": title, "author": author, "available": True})

def get_books():
    return books

# utils/helpers.py - This will handle helper functions

def format_book(book):
    status = "Available" if book["available"] else "Borrowed"
    return f"{book['title']} by {book['author']} - {status}"

# services/library.py  - This will handle business logic

import data.data as data

def borrow_book(title):
    for book in data.get_books():
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            return f"You have borrowed '{book['title']}'"
    return "Book not available."

# main.py - This will be our project entry point


from data import data
from utils import helpers
from services import library

# Add some books
data.add_book("Python Basics", "John Doe")
data.add_book("Advanced Python", "Jane Smith")

# Display all books
print("Library Collection:")
for b in data.get_books():
    print(helpers.format_book(b))

# Borrow a book
print("\nBorrowing a book:")
print(library.borrow_book("Python Basics"))

# Display books again
print("\nUpdated Library Collection:")
for b in data.get_books():
    print(helpers.format_book(b))


# data/data.py - This will handle data storage in json format

import json
import os

FILE_PATH = "library_data.json"
books = []

def load_books():
    """Load books from JSON file if it exists"""
    global books
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            books = json.load(f)
    else:
        books = []

def save_books():
    """Save current books list to JSON file"""
    with open(FILE_PATH, "w") as f:
        json.dump(books, f, indent=4)

def add_book(title, author):
    books.append({"title": title, "author": author, "available": True})
    save_books()

def get_books():
    return books

# utils/helpers.py - This will handle helper functions

def format_book(book, index):
    status = "Available" if book["available"] else "Borrowed"
    return f"{index}. {book['title']} by {book['author']} - {status}"

# services/library.py - This will update to save after borrow/return
import data.data as data

def borrow_book(title):
    for book in data.get_books():
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            data.save_books()
            return f"You have borrowed '{book['title']}'"
    return "Book not available."

def return_book(title):
    for book in data.get_books():
        if book["title"].lower() == title.lower() and not book["available"]:
            book["available"] = True
            data.save_books()
            return f"You have returned '{book['title']}'"
    return "Book not found or not borrowed."

# main.py - This intitialize by loading books at start up
from data import data
from utils import helpers
from services import library

def show_books():
    books = data.get_books()
    if not books:
        print("No books in the library yet.")
        return
    for i, b in enumerate(books, start=1):
        print(helpers.format_book(b, i))

def main():
    data.load_books()  # Load books when app starts
    
    while True:
        print("\n__Library Menu__")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            data.add_book(title, author)
            print(f"'{title}' by {author} added to library.")

        elif choice == "2":
            print("\nLibrary Collection:")
            show_books()

        elif choice == "3":
            title = input("Enter book title to borrow: ")
            print(library.borrow_book(title))

        elif choice == "4":
            title = input("Enter book title to return: ")
            print(library.return_book(title))

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()
