class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def borrow_book(self, user, book):
        user.borrow_book(book)

    def return_book(self, user, book):
        user.return_book(book)

    def list_available_books(self):
        return [str(book) for book in self.books if book.available]
