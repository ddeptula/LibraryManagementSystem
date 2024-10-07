import unittest
from library.book import Book
from library.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.book = Book("Book1", "Author1", "12345")
        self.user = User("User1 Test", "1000")

    def test_borrow_book(self):
        self.user.borrow_book(self.book)
        self.assertIn(self.book, self.user.borrowed_books)
        self.assertFalse(self.book.available)

    def test_return_book(self):
        self.user.borrow_book(self.book)
        self.user.return_book(self.book)
        self.assertNotIn(self.book, self.user.borrowed_books)
        self.assertTrue(self.book.available)

    def test_view_borrowed_books(self):
        self.user.borrow_book(self.book)
        self.assertIn(str(self.book), self.user.view_borrowed_books())


if __name__ == '__main__':
    unittest.main()
