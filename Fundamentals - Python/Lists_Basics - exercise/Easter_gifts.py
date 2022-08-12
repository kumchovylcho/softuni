gifts = input().split()
command = input()
while command != "No Money":
    list_with_commands = command.split()
    if list_with_commands[0] == "OutOfStock":
        for word in range(len(gifts)):
            if gifts[word] == list_with_commands[1]:
                gifts[word] = "None"
    elif list_with_commands[0] == "Required":
        for word in range(len(gifts)):
            if word == int(list_with_commands[2]):
                gifts[word] = list_with_commands[1]
    elif list_with_commands[0] == "JustInCase":
        gifts[-1] = list_with_commands[1]
    command = input()
for words in gifts:
    if words != "None":
        print(words, end=" ")
