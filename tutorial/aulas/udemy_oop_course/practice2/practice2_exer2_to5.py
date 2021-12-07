'''
2. Create a class named Book with an __init__ method. Inside the __init__ method, create the instance 
variables isbn, title, author, publisher, pages, price, copies.

Create these four instance objects from this class.

book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)
Write a method display that prints the isbn, title, price and number of copies of the book.


3. For the Book class that you have created, write a method named in_stock that returns True if number 
of copies is more than zero, otherwise it returns False.

Create another method named sell that decreases the number of copies by 1 if the book is in stock, 
otherwise it prints the message that the book is out of stock.


4. Create a list named books that contains the 4 Book instance objects that you have created in 
question 2. Iterate over this list using a for loop and call display() for each object in the list.

Write a list comprehension to create another list that contains title of books written by Jack.


5. In the Book class, create a property named price such that the price of a book cannot be less 
than 50 or more than 1000.
'''



class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self._price = price
        self.copies = copies

    def display(self):
        print(f'{self.isbn} {self.title} {self._price} {self.copies}')

    def in_stock(self):
        if self.copies > 0:
            return True
        else:
            return False

    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print('Book is out of stock')

    @property
    def price(self):
        print(self._price)

    @price.setter
    def price(self, new_price):
        try:
            if 50 < new_price < 1000:
                self._price = new_price
            else:
                raise ValueError
        except(ValueError):
            print('Price is not valid')


book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200, 6)

book_list = [book1, book2, book3, book4]

for book in book_list:
    book.display()

jack_books = [book.title for book in book_list if book.author == 'Jack']
print(jack_books)

book1.price
book1.price = 10000
book1.price
