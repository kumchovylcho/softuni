from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):

    def setUp(self) -> None:
        self.library = Library("Tamer")

    def test_empty_name_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_successful_initialization(self):
        self.assertEqual("Tamer", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_successful_add_book(self):
        self.library.add_book("Tamer", "ribarcheto")
        self.assertEqual({"Tamer": ["ribarcheto"]}, self.library.books_by_authors)
        self.library.add_book("Tamer", "ribarcheto")
        self.assertEqual({"Tamer": ["ribarcheto"]}, self.library.books_by_authors)
        self.library.add_book("Tamer", "ribarche")
        self.assertEqual({"Tamer": ["ribarcheto", "ribarche"]}, self.library.books_by_authors)
        self.assertEqual(2, len(self.library.books_by_authors["Tamer"]))

    def test_successful_add_reader(self):
        self.library.add_reader("Tamer")
        self.assertEqual({"Tamer": []}, self.library.readers)

    def test_add_reader_with_same_name(self):
        self.library.add_reader("Tamer")
        self.assertEqual(f"Tamer is already registered in the Tamer library.", self.library.add_reader("Tamer"))

    def test_rent_book_reader_name_not_in_readers(self):
        actual = self.library.rent_book("Tamer", "Tamer", "ribarcheto")
        self.assertEqual("Tamer is not registered in the Tamer Library.", actual)

    def test_rent_book_author_not_in_books_by_authors(self):
        self.library.add_reader("Tamer")
        actual = self.library.rent_book("Tamer", "Tamer", "ribarcheto")
        self.assertEqual("Tamer Library does not have any Tamer's books.", actual)

    def test_rent_book_title_does_not_exist(self):
        self.library.add_reader("Tamer")
        self.library.add_book("Tamer", "ribarche")
        actual = self.library.rent_book("Tamer", "Tamer", "ribarcheTO")
        self.assertEqual("""Tamer Library does not have Tamer's "ribarcheTO".""", actual)

    def test_successful_rent_book(self):
        self.library.add_reader("Tamer")
        self.library.add_book("Tomi", "ribarche")
        self.assertEqual({"Tomi": ["ribarche"]}, self.library.books_by_authors)
        self.assertEqual({"Tamer": []}, self.library.readers)
        self.library.rent_book("Tamer", "Tomi", "ribarche")
        self.assertEqual({"Tamer": [{"Tomi": "ribarche"}]}, self.library.readers)
        self.assertEqual({"Tomi": []}, self.library.books_by_authors)


if __name__ == "__main__":
    main()
