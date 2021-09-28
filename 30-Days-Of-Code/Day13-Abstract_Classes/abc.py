#!/usr/bin/python

#Write MyBook class
class MyBook(Book):
    # Override the SuperClass's constructor
    def __init__(self, title, author, price=0):
        # Call the SuperClass's init method
        super().__init__(title, author)
        self.price = price

    # Override SuperClass's display method
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

