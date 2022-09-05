password = input()
no_substring = False


def main():
    global password
    global no_substring
    command = input()
    while command != "Done":
        command = command.split()
        no_substring = False

        if command[0] == "TakeOdd":
            take_odd()

        elif command[0] == "Cut":
            cut(int(command[1]), int(command[2]))

        elif command[0] == "Substitute":
            substitute(command[1], command[2])

        if not no_substring:
            print(password)
        command = input()

    print(f"Your password is: {password}")


def take_odd():
    global password
    password = password[1::2]


def cut(index, length_of_word):
    global password
    password = password[:index] + password[index + length_of_word:]


def substitute(substring, replacement_word):
    global password
    global no_substring
    if substring in password:
        password = password.replace(substring, replacement_word)
    elif substring not in password:
        no_substring = True
        print("Nothing to replace!")


main()


# password = input()
#
# command = input()
# while command != "Done":
#     no_substring = False
#     command = command.split()
#
#     if command[0] == "TakeOdd":
#         password = password[1::2]
#
#     elif command[0] == "Cut":
#         index = int(command[1])
#         length = int(command[2])
#         password = password[:index] + password[index + length:]
#
#     elif command[0] == "Substitute":
#         substring = command[1]
#         substitute = command[2]
#         if substring in password:
#             password = password.replace(substring, substitute)
#         elif substring not in password:
#             no_substring = True
#             print("Nothing to replace!")
#
#     if not no_substring:
#         print(password)
#     command = input()
#
# print(f"Your password is: {password}")
