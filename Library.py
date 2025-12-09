"""
Library Management System with List of Dictionary for storing 
example 
library = [
    {"id":"101", "title":"Harry Potter"}
    {"id":"102", "title":"Rich Dad Poor Dad"}
functions to create
Add()
Search()
Borrow()
Return()
Show()
menu()

data stored in the following format

    "id":book_id,
    "title":title,
    "author":author,
    "count":copies,
    "available":copies

to run in terminal (python Library.py)   
"""
Library=[]
def add():
    book_id =input("Enter B_id")
    title=input("Enter B_Title")
    author =input("Enter B_author")
    copies=int(input("Enter B_copies_Count"))
    n_book={
        "id":book_id,
        "title":title,
        "author":author,
        "count":copies,
        "available":copies
    }
    Library.append(n_book)
    print("Book Added To Library")

def search():
    key =input("Enter search keyword :").lower()
    found=False
    for B in Library:# using logical operator cause easy for writing it in short 
        if(key in B["id"].lower() or key in B["title"].lower() or key in B["author"].lower()):
            print(B)
            found= True
    if not found:
        print("Book not found")

def borrow():
    # sub 1 from the avaiable count
    b_id = input("Enter the Book ID:")
    for book in Library:
        if book["id"] == b_id:
            if book["available"]>0:
                book["available"]-=1
                print("Book Borrowed Successfully")
                return
            else:
                print("No copies Available")
                return
    print ("Book Not Found")

def return_b():
    # add 1 to the copies avaialbe 
    b_id = input("Enter the Book ID:")
    for book in Library:
        if book["id"] == b_id:
            if book["available"]< book["total"]:
                book["available"]+=1
                print("Book Returned Successfully")
                return
            else:
                print("All Copies In library")
                return
    print ("Book Not Found")
def show():
    if not Library:
        print("Library is empty")
        return
    for book in Library:
        print(book)
def menu():
    while True:
         print(" Library Management System ")
         print("1. Add Book")
         print("2. Search Book")
         print("3. Borrow Book")
         print("4. Return Book")
         print("5. Show Books")
         print("6. Exit")
         choice = input("Enter your choice:")
         if choice == "1":
             add()
         elif choice == "2":
             search()
         elif choice == "3":
             borrow()
         elif choice == "4":
             return_b()
         elif choice == "5":
             show()
         elif choice == "6":
             print("Exiting")
             break
         else:
             print("invalid choice.")
menu()