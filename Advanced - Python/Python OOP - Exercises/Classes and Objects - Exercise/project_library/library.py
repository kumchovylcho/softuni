from project.user import User


class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in Library.books_available:
            if book_name in Library.books_available[author]:
                Library.books_available[author].remove(book_name)
                if user.username not in Library.rented_books:
                    Library.rented_books[user.username] = {}
                Library.rented_books[user.username][book_name] = days_to_return
                user.books.append(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for book in Library.rented_books:
            for book_names, days_left in Library.rented_books[book].items():
                if book_names == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {days_left} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            Library.books_available[author].append(book_name)
            del Library.rented_books[user.username][book_name]
        return f"{user.username} doesn't have this book in his/her records!"
