class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow_book()
            self.borrowed_books.append(book)
        else:
            raise Exception("Book is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            raise Exception("This book was not borrowed by the user.")

    def view_borrowed_books(self):
        return [str(book) for book in self.borrowed_books]
