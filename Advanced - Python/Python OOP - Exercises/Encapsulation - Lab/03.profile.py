class Profile:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, current_username):
        if 5 <= len(current_username) <= 15:
            self.__username = current_username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, current_password):
        if len(current_password) >= 8 and \
                [1 for x in current_password if x.isupper()] and \
                [1 for x in current_password if x.isdigit()]:
            self.__password = current_password
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# class Profile:
#
#     def __init__(self, username: str, password: str):
#         self.username = username
#         self.password = password
#
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, current_name):
#         if 5 <= len(current_name) <= 15:
#             self.__username = current_name
#         else:
#             raise ValueError("The username must be between 5 and 15 characters.")
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, current_password):
#         if len(current_password) >= 8:
#             uppercase, digit = 0, 0
#             for symbol in current_password:
#                 if symbol.isupper():
#                     uppercase += 1
#                 elif symbol.isdigit():
#                     digit += 1
#             if uppercase and digit:
#                 self.__password = current_password
#         if len(current_password) < 8 or not sum(1 for x in current_password if x.isupper()) or \
#                 not sum(1 for x in current_password if x.isdigit()):
#             raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#
#     def __str__(self):
#         return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'
