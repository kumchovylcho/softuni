notes = [0] * 10
command = input()
while command != "End":
    tokens = command.split("-")
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)
    command = input()

result = [element for element in notes if element != 0]
print(result)
