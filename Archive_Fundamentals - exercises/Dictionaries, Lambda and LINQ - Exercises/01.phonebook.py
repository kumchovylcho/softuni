phonebook = {}
command = input()
while command != "END":
    operation, name, *number = command.split()
    if operation == "A":
        phonebook[name] = ''.join(number)
    elif operation == "S":
        if name in phonebook:
            print(f"{name} -> {phonebook[name]}")
        elif name not in phonebook:
            print(f"Contact {name} does not exist.")
    command = input()