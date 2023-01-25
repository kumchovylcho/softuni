from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookStore(TestCase):

    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_successful_initialization(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_books_limit_below_zero_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test__len__(self):
        self.bookstore.availability_in_store_by_book_titles = {"Tamer": 10, "Tamer_2": 10}
        self.assertEqual(20, len(self.bookstore))

    def test_receive_book_not_enough_space_exception_error(self):
        self.bookstore.availability_in_store_by_book_titles = {"Tamer": 10, "Tamer_2": 10}
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Tamer", 10)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_successful_receive_book(self):
        actual = self.bookstore.receive_book("Tamer", 5)
        self.assertEqual({"Tamer": 5}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual("5 copies of Tamer are available in the bookstore.", actual)

        actual_2 = self.bookstore.receive_book("Tamer", 5)
        self.assertEqual({"Tamer": 10}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(1, len(self.bookstore.availability_in_store_by_book_titles))
        self.assertEqual("10 copies of Tamer are available in the bookstore.", actual_2)

    def test_sell_book_with_non_existent_book_title_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Tamer", 5)
        self.assertEqual("Book Tamer doesn't exist!", str(ex.exception))

    def test_sell_book_can_not_sell_more_books_than_you_have_exception_error(self):
        self.bookstore.receive_book("Tamer", 5)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Tamer", 6)
        self.assertEqual("Tamer has not enough copies to sell. Left: 5", str(ex.exception))

    def test_successful_sell_book(self):
        self.bookstore.receive_book("Tamer", 5)

        actual = self.bookstore.sell_book("Tamer", 3)
        self.assertEqual("Sold 3 copies of Tamer", actual)
        self.assertEqual({"Tamer": 2}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(3, self.bookstore.total_sold_books)

    def test__str__(self):
        self.bookstore.receive_book("Tamer", 2)
        self.bookstore.receive_book("Tamer_2", 2)
        self.bookstore.receive_book("Tamer_3", 2)

        self.bookstore.sell_book("Tamer", 2)

        expected = "Total sold books: 2\n" \
                   "Current availability: 4\n" \
                   " - Tamer: 0 copies\n" \
                   " - Tamer_2: 2 copies\n" \
                   " - Tamer_3: 2 copies"

        self.assertEqual(expected, str(self.bookstore))


if __name__ == "__main__":
    main()