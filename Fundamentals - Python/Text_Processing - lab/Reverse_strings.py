command = input()
while command != "end":
    print(f"{command} = {command[::-1]}")
    command = input()