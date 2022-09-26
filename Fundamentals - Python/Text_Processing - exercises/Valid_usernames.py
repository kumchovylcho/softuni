import string
usernames = input().split(", ")
for name in usernames:
    if 3 <= len(name) <= 16:
        for letter in name:
            if letter not in "-_" + string.ascii_letters + string.digits:
                break
        else:
            print(name)
