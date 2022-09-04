message = input()


def main():
    global no_substring
    command = input()
    while command != "Reveal":
        no_substring = False
        command = command.split(":|:")
        if command[0] == "InsertSpace":
            insert_space(int(command[1]))

        elif command[0] == "Reverse":
            reverse(command[1])

        elif command[0] == "ChangeAll":
            change_all(command[1], command[2])

        if not no_substring:
            print(message)
        command = input()
    print(f"You have a new text message: {message}")


def insert_space(index):
    global message
    message = f"{message[:index]} {message[index:]}"


def reverse(substring):
    global message
    global no_substring
    if substring in message:
        index_of_first_letter_of_substring = message.index(substring[0])
        index_of_last_letter_of_substring = index_of_first_letter_of_substring + len(substring)

        message_with_removed_word = message[:index_of_first_letter_of_substring] + message[
                                                                                   index_of_last_letter_of_substring:]
        reversed_substring = substring[::-1]

        message = message_with_removed_word + reversed_substring
    elif substring not in message:
        no_substring = True
        print("error")


def change_all(substring, replacement_word):
    global message
    message = message.replace(substring, replacement_word)


main()


# message = input()
#
# command = input()
# while command != "Reveal":
#     no_substring = False
#     command = command.split(":|:")
#     if command[0] == "InsertSpace":
#         index = int(command[1])
#         message = f"{message[:index]} {message[index:]}"
#
#     elif command[0] == "Reverse":
#         substring = command[1]
#         if substring in message:
#             index_of_first_letter_of_substring = message.index(substring[0])
#             index_of_last_letter_of_substring = index_of_first_letter_of_substring + len(substring)
#
#             message_with_removed_word = message[:index_of_first_letter_of_substring] + message[
#                                                                                    index_of_last_letter_of_substring:]
#             reversed_substring = substring[::-1]
#
#             message = message_with_removed_word + reversed_substring
#         elif substring not in message:
#             no_substring = True
#             print("error")
#
#     elif command[0] == "ChangeAll":
#         substring = command[1]
#         replacement_word = command[2]
#         message = message.replace(substring, replacement_word)
#
#     if not no_substring:
#         print(message)
#     command = input()
#
# print(f"You have a new text message: {message}")
