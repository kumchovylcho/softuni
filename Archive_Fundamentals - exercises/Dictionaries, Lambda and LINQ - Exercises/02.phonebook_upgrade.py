phonebook = {}
command = input()
while command != "END":
    operation, *data = command.split()
    if operation == "A":
        name = data[0]
        number = data[1]
        phonebook[name] = ''.join(number)
    elif operation == "S":
        name = data[0]
        if name in phonebook:
            print(f"{name} -> {phonebook[name]}")
        elif name not in phonebook:
            print(f"Contact {name} does not exist.")
    elif operation == "ListAll":
        for key, value in sorted(phonebook.items()):
            print(f"{key} -> {value}")
    command = input()
