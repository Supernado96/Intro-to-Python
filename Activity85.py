# Library System
# Build a simple library system using a class. Each book is an object. Your system lets users borrow and return books and tracks whether each book is currently available.

# What you need to use
# ------------------------------------------------------------------------
# 1.  Book class      →  __init__ sets title, author, and is_borrowed = False
# 2.  borrow()        →  sets is_borrowed to True and prints a confirmation
# 3.  return_book()   →  sets is_borrowed to False and prints a confirmation
# 4.  3 Book objects  →  demonstrate both borrow() and return_book()
# 5.  self            →  used to access and update attributes inside methods
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  Book class with __init__ setting title, author, is_borrowed   →   5 marks
# 2.  borrow() sets is_borrowed True and prints confirmation         →  10 marks
# 3.  return_book() sets is_borrowed False and prints confirmation   →  10 marks
# 4.  At least 3 Book objects with both methods demonstrated         →  10 marks
# 5.  Program runs without any errors                                →   5 marks
# ========================================================================
# Total  →  40 marks
# ========================================================================

# How to submit 🚀
# Push your completed code to a public GitHub repository and paste the
# repo link in the box below. Make sure your repo is public and your
# code runs correctly before submitting.

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        if self.is_borrowed == True:
            print(f"{self.title} already borrowed.❌")
        self.is_borrowed = True
        print(f"{self.title} successfully borrowed!✅")
    def return_book(self):
        if self.is_borrowed == False:
            print(f"{self.title} is not borrowed yet.❌")
        else:
            self.is_borrowed = False
            print(f"{self.title} successfully returned!✅")


harry_potter = Book("Harry Potter", "JK Rowling")
monte_cristo = Book("The Count of Monte Cristo", "Alexandré Dumas")
dog_man = Book("Dog Man", "Dav Pilkey")

harry_potter.borrow()
monte_cristo.borrow()
harry_potter.return_book()
dog_man.borrow()
dog_man.return_book()
monte_cristo.return_book()