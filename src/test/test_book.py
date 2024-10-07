import unittest
from library.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Book 1", "Author1", "12345")
        
    def test_book_creation(self):
        self.assertEqual(self.book.title, "Book 1")
        self.assertEqual(self.book.author, "Author1")
        self.assertEqual(self.book.isbn, "12345")
        self.assertTrue(self.book.available)

    def test_borrow_book(self):
        self.book.borrow_book()
        self.assertFalse(self.book.available)

    def test_return_book(self):
        self.book.borrow_book()
        self.book.return_book()
        self.assertTrue(self.book.available)

if __name__ == '__main__':
    unittest.main()
