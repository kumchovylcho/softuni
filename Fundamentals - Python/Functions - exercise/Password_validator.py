from string import ascii_letters
allowed_characters = "0123456789" + ascii_letters
password = input()


def is_valid(passWord):
    valid_password = 0  # if this gets to 1 , then the password is valid
    check_digits = 0  # if this gets to 2 , then the password has at least 2 digits
    if 6 <= len(passWord) <= 10:
        valid_password += 1
    elif 6 > len(passWord) or len(passWord) > 10:
        print("Password must be between 6 and 10 characters")
    for text in passWord:
        if text not in allowed_characters:
            print("Password must consist only of letters and digits")
            valid_password -= 1
            break
        elif text.isdigit():
            check_digits += 1
    if check_digits < 2:
        print("Password must have at least 2 digits")
    if valid_password == 1 and check_digits >= 2:
        print("Password is valid")


is_valid(password)
