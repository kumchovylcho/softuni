message = input()


def main():
    command = input()
    while command != "Decode":
        command = command.split("|")

        if command[0] == "Move":
            move(int(command[1]))

        elif command[0] == "Insert":
            insert(int(command[1]), command[2])

        elif command[0] == "ChangeAll":
            change_all(command[1], command[2])
        command = input()
    print(f"The decrypted message is: {message}")


def change_all(substring, replacement):
    global message
    if substring in message:
        message = message.replace(substring, replacement)


def insert(index, letter):
    global message
    message = f"{message[0:index]}{letter}{message[index:]}"


def move(number_of_letters):
    global message
    first_letters = message[0:number_of_letters]
    message = message[number_of_letters:] + first_letters


main()


# message = input()
#
#
# command = input()
# while command != "Decode":
#     command = command.split("|")
#
#     if command[0] == "Move":
#         how_many_letters = int(command[1])
#         first_letters = message[0:how_many_letters]
#         message = message[how_many_letters:] + first_letters
#
#     elif command[0] == "Insert":
#         index = int(command[1])
#         new_letter = command[2]
#         message = f"{message[0:index]}{new_letter}{message[index:]}"
#
#     elif command[0] == "ChangeAll":
#         occurrences = command[1]
#         replace = command[2]
#         if occurrences in message:
#             message = message.replace(occurrences, replace)
#
#     command = input()
#
# print(f"The decrypted message is: {message}")
