class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: [Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title: str):
        for book in self.books:
            if book.title == title:
                return book


first_book = Book("Safrid", "Tamer")
library = Library()

library.add_book(first_book)