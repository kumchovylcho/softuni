def valid_length(password):
    return 6 <= len(password) <= 10


def is_alphanumeric(password):
    return password.isalnum()


def has_at_least_two_digits(password):
    return len([x for x in password if x.isdigit()]) >= 2


def password_validator(password):
    errors = []
    if not valid_length(password):
        errors.append("Password must be between 6 and 10 characters")

    if not is_alphanumeric(password):
        errors.append('Password must consist only of letters and digits')

    if not has_at_least_two_digits(password):
        errors.append("Password must have at least 2 digits")

    if not errors:
        return 'Password is valid'

    return "\n".join(errors)


input_password = input()
print(password_validator(input_password))

################################################################################################

# def password_validation(password):
#     list_with_errors = []
#     if not 6 <= len(password) <= 10:
#         list_with_errors.append("Password must be between 6 and 10 characters")
#     counter_of_digits = 0
#     for character in password:
#         if not character.isdigit() and not character.isalpha():
#             list_with_errors.append("Password must consist only of letters and digits")
#             break
#         elif character.isdigit():
#             counter_of_digits += 1
#     if counter_of_digits < 2:
#         list_with_errors.append("Password must have at least 2 digits")
#     return list_with_errors
#
#
# current_password = input()
# errors = password_validation(current_password)
# if not errors:
#     print("Password is valid")
# else:
#     for error in errors:
#         print(error)


# from string import ascii_letters
# allowed_characters = "0123456789" + ascii_letters
# password = input()
#
#
# def is_valid(passWord):
#     valid_password = 0  # if this gets to 1 , then the password is valid
#     check_digits = 0  # if this gets to 2 , then the password has at least 2 digits
#     if 6 <= len(passWord) <= 10:
#         valid_password += 1
#     elif 6 > len(passWord) or len(passWord) > 10:
#         print("Password must be between 6 and 10 characters")
#     for text in passWord:
#         if text not in allowed_characters:
#             print("Password must consist only of letters and digits")
#             valid_password -= 1
#             break
#         elif text.isdigit():
#             check_digits += 1
#     if check_digits < 2:
#         print("Password must have at least 2 digits")
#     if valid_password == 1 and check_digits >= 2:
#         print("Password is valid")
#
#
# is_valid(password)
