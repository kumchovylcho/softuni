gifts = input().split()
command = input()
while command != "No Money":
    command = command.split()
    operation, current_gift = command[0], command[1]
    if operation == "OutOfStock":
        gifts = [None if gift == current_gift else gift for gift in gifts]
    elif operation == "Required":
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = current_gift
    elif operation == "JustInCase":
        gifts[-1] = current_gift
    command = input()

for gift in gifts:
    if gift is not None:
        print(f"{gift}", end=' ')


# gifts = input().split()
# command = input()
# while command != "No Money":
#     list_with_commands = command.split()
#     if list_with_commands[0] == "OutOfStock":
#         for word in range(len(gifts)):
#             if gifts[word] == list_with_commands[1]:
#                 gifts[word] = "None"
#     elif list_with_commands[0] == "Required":
#         for word in range(len(gifts)):
#             if word == int(list_with_commands[2]):
#                 gifts[word] = list_with_commands[1]
#     elif list_with_commands[0] == "JustInCase":
#         gifts[-1] = list_with_commands[1]
#     command = input()
# for words in gifts:
#     if words != "None":
#         print(words, end=" ")
