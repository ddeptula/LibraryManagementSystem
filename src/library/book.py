class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"Book: {self.title} by {self.author}, ISBN: {self.isbn}"

    def borrow_book(self):
        if self.available:
            self.available = False
        else:
            raise Exception("Book is not available.")

    def return_book(self):
        self.available = True
