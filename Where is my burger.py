import json
from datetime import datetime
import random
'''Students will build a Library Book Management System that can:
Add books to the library (title, author, genre).
Borrow books, updating a popularity score for each book.
Return books (optional bonus: track borrowing history).
Show the current list of books and their popularity scores.
Save the data in a JSON file, so it persists when the program closes

Use lists and dictionaries to store and manage data.
Create functions with parameters to make code modular.
Implement loops and conditionals for user interaction.
Read/write JSON files to make data persistent.
Perform simple data analysis: find the most popular book, total books, etc.'''
con1 = 1
books = {
     
}
#Allows you to add a book to the libary by inputing its
def add_book(title, author, genre):
   with open('books.json', 'r') as f:
           books = json.load(f)
   if title in books:
       books[title]["Copies"] += 1
       print("another copy has been added.\n")
   else:
       books[title]={"Title": title, "Author": author, "Genre": genre, "Copies": 1, "Popularity Score": 0}
       print("Book has successfully been added!\n")

   with open('books.json', 'w') as f:
       json.dump(books, f, indent=4)
#Lets you borrow a book from the libary
def borrow_book(title):
   with open('books.json', 'r') as f:
           books = json.load(f) 
   if books[borrow]["Copies"]>0:
       books[borrow]["Copies"]-=1
       books[borrow]["Popularity Score"]+=1
       print("You have successfully borrowed the book!.\n")
   else:
       print("This book is not currently available.\n")

   with open('books.json', 'w') as f:
       json.dump(books, f, indent=4)
#Shows all the books that are registered
def show_books():
   with open('books.json', 'r') as f:
           books = json.load(f)
   for Title in books:
       print(books[Title]["Title"])
#Allows you to input a book to return
def return_book(return1):  
   with open('books.json', 'r') as f:
           books = json.load(f)
   if return1 in books:
       books[return1]["Copies"]+=1
       print("The book has been successfully returned!\n")
  
   with open('books.json', 'w') as f:
       json.dump(books, f, indent=4)
#Shows all the stats from the books you added or the ones that were already there,
def show_stats():  
   with open('books.json', 'r') as f:
           books = json.load(f)     
   print(json.dumps(books, indent=4))
while con1==1:
   choice1=input("Welcome, what would you like to do?\nAdd Book\nBorrow Book\nReturn Book\nShow Stats\n(Input clear to reset the file)\n")
   choice2=choice1.casefold()
   if choice2 == "add book":
       title = input("What is the book's title?\n")
       author = input("Who is the author of the book?\n")
       genre = input("What is the book's genre?\n")
       add_book(title, author, genre)

   elif choice2 == "borrow book":
       show_books()
       borrow = input("What book do you want to borrow?\n")
       borrow_book(borrow)

   elif choice2 == "clear":
       with open('books.json', 'w') as f:
           json.dump(books, f)
           print("Successfully Cleared!")

   elif choice2 == "return book":
       show_books()
       return1=input("What book do you want to return?\n")
       return_book(return1)

   elif choice2 == "show stats":
       show_stats()
