# Class 1: Book
# __init__: title, author, price, stock
# is_available(): stock > 0 → True/False
# discount(percent): discounted price
# info(): sab print karo



class Book:
    def __init__(self,title,author,price,stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
        

    def is_available(self):
        if self.stock > 0:
            print("True")
        else:
            print("False")


    def discount(self,percent):
        disc = self.price * percent / 100
        final_price = self.price - disc
        return f"final_price: {final_price}"


    def info(self):
        return (f"Title: {self.title}\n Author: {self.author}\n Price: {self.price}\n Stock: {self.stock}")
    

    # Class 2: Library
# __init__: name, books=[]
# add_book(book): book add karo
# show_books(): lambda sort + print
# search_book(title): search karo
# premium_books(): price>500 wale
#                  (Comprehension!)
# save_report(): file mein save
# summary(): poori report


class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def show_books(self):
        books = sorted(self.books,key=lambda x: x.title )
        for b in books:
            print(b.info())

    def search_book(self,title):
            srch_book = input("enter book title: ").lower()
            for b in self.books:
                if b.title.lower() == srch_book:
                    print(b.info())
                    return
            print("Not Found!")
            


    def premium_books(self):
        pre_book = [b.title for b in self.books if b.price > 500]
        print(f"Premium Books: {pre_book}")

    def save_report(self):
        with open("Library.txt","w") as file:
            for data in self.books:
                file.write(data.info() + "\n")


    def summary(self):
        print("━━━━━━━━━━━━━━━━━━━━━")
        print(f"  {self.name}")
        print("━━━━━━━━━━━━━━━━━━━━━")
        self.show_books()
        self.premium_books()
        self.save_report()
        print("Report saved! ✅")

    

my_book1 = Book("Python","Ali",2500,50)
my_book2 = Book("DataBase","John",2000,0)

library = Library("City Library")

user_title = input("Enter Book Title: ").lower()
library.search_book(user_title)

library.add_book(my_book1)
library.add_book(my_book2)

library.summary()

