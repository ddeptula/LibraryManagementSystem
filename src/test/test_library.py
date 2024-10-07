import unittest
from library.book import Book
from library.user import User
from library.library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Book 1", "Author1", "12345")
        self.book2 = Book("Book 2", "Author2", "54321")
        self.user = User("User1 Test", "1000")

        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_user(self.user)

    def test_add_and_remove_book(self):
        self.library.remove_book(self.book1)
        self.assertNotIn(self.book1, self.library.books)

    def test_add_and_remove_user(self):
        self.library.remove_user(self.user)
        self.assertNotIn(self.user, self.library.users)

    def test_borrow_book(self):
        self.library.borrow_book(self.user, self.book1)
        self.assertIn(self.book1, self.user.borrowed_books)
        self.assertFalse(self.book1.available)

    def test_return_book(self):
        self.library.borrow_book(self.user, self.book1)
        self.library.return_book(self.user, self.book1)
        self.assertNotIn(self.book1, self.user.borrowed_books)
        self.assertTrue(self.book1.available)

    def test_list_available_books(self):
        self.library.borrow_book(self.user, self.book1)
        available_books = self.library.list_available_books()
        self.assertNotIn(str(self.book1), available_books)
        self.assertIn(str(self.book2), available_books)


if __name__ == '__main__':
    unittest.main()
