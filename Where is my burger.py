import json
from datetime import datetime
import random
FILE_PATH = "library_books.json"
'''Students will build a Library Book Management System that can:
Add books to the library (title, author, genre).
Borrow books, updating a popularity score for each book.
Return books (optional bonus: track borrowing history).
Show the current list of books and their popularity scores.
Save the data in a JSON file, so it persists when the program closes

Use lists and dictionaries to store and manage data.
Create functions with parameters to make code modular.
Implement loops and conditionals for user interaction.
Read/write JSO-N files to make data persistent.
Perform simple data analysis: find the most popular book, total books, etc.'''
books = ["Where","Is","My","Burger"]
with open('books.json', 'w') as file:
 books = json.dump(books, file, indent=4)
def add_book():
    input("Print the book you want to add to the libary")
def borrow_book():
    print("Book Sucessfuly Borrowed for 7 days!")
def show_books():
    print("Showing:")
def show_stats():
    print("Showing:")
print(books)
01010010101001010 0100100