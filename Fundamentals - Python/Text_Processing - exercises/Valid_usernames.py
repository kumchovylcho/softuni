import string
usernames = input().split(", ")
for name in usernames:
    if 3 <= len(name) <= 16:
        for letter in name:
            if letter not in "-_" + string.ascii_letters + string.digits:
                break
        else:
            print(name)


# def no_redundant_symbol(username):
#     if ' ' in username:
#         return False
#     return True
#
#
# def lenght_is_valid(username):
#     if 3 <= len(username) <= 16:
#         return True
#     return False
#
#
# def valid_characters(username):
#     for character in username:
#         if not character.isalnum() and character not in "-_":
#             return False
#     return True
#
#
# def username_is_valid(username):
#     if valid_characters(username) and lenght_is_valid(username) and no_redundant_symbol(username):
#         return True
#     return False
#
#
# usernames = input().split(", ")
# for name in usernames:
#     if username_is_valid(name):
#         print(name)