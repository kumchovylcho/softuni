class Password:

    def __init__(self, main_string):
        self.main_string = main_string

    def take_odd(self):
        self.main_string = self.main_string[1::2]
        Password.print_string(self)

    def cut(self, index, length):
        start_index = index
        end_index = index + length
        self.main_string = self.main_string[:start_index] + self.main_string[end_index:]
        Password.print_string(self)

    def substitute(self, substring, new_word):
        if substring in self.main_string:
            self.main_string = self.main_string.replace(substring, new_word)
            Password.print_string(self)
        elif substring not in self.main_string:
            print("Nothing to replace!")

    def print_string(self):
        print(self.main_string)

    def __repr__(self):
        return f"{self.main_string}"


text = input()
main_text = Password(text)
operations = {
    'TakeOdd': main_text.take_odd,
    'Cut': main_text.cut,
    'Substitute': main_text.substitute
}
command = input()
while command != "Done":
    task, *info = [int(item) if item.isdigit() else item for item in command.split()]
    operations[task](*info)
    # if task == 'TakeOdd':
    #     main_text.take_odd()
    # elif task == 'Cut':
    #     main_text.cut(*info)
    # elif task == 'Substitute':
    #     main_text.substitute(*info)
    command = input()
print(f"Your password is: {main_text}")


# password = input()
# no_substring = False
#
#
# def main():
#     global password
#     global no_substring
#     command = input()
#     while command != "Done":
#         command = command.split()
#         no_substring = False
#
#         if command[0] == "TakeOdd":
#             take_odd()
#
#         elif command[0] == "Cut":
#             cut(int(command[1]), int(command[2]))
#
#         elif command[0] == "Substitute":
#             substitute(command[1], command[2])
#
#         if not no_substring:
#             print(password)
#         command = input()
#
#     print(f"Your password is: {password}")
#
#
# def take_odd():
#     global password
#     password = password[1::2]
#
#
# def cut(index, length_of_word):
#     global password
#     password = password[:index] + password[index + length_of_word:]
#
#
# def substitute(substring, replacement_word):
#     global password
#     global no_substring
#     if substring in password:
#         password = password.replace(substring, replacement_word)
#     elif substring not in password:
#         no_substring = True
#         print("Nothing to replace!")
#
#
# main()


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
