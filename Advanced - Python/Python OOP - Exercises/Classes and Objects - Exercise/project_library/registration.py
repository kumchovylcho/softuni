from project.library import Library
from project.user import User


class Registration:

    def add_user(self, user: User, library: Library):
        for people in library.user_records:
            if people.user_id == user.user_id:
                return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        for people in library.user_records:
            if people.user_id == user.user_id:
                library.user_records.remove(user)
                return
        return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for people in library.user_records:
            if people.user_id == user_id:
                if people.username != new_username:
                    if people.username in library.rented_books:
                        library.rented_books[new_username] = library.rented_books.pop(people.username)
                    people.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                return f"Please check again the provided username - it should be different than the username used so" \
                       f" far!"
        return f"There is no user with id = {user_id}!"
