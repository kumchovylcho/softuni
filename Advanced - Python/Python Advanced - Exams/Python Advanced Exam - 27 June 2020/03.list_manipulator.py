def list_manipulator(*args):
    numbers = args[0]
    command, where = args[1], args[2]
    if command == "add":
        if where == "beginning":
            numbers = list(args[3:]) + numbers
        elif where == "end":
            numbers = numbers + list(args[3:])
    elif command == "remove":
        if where == "beginning" and str(args[-1]).isdigit():
            remove_items = args[3]
            numbers = numbers[remove_items:]
        elif where == "beginning" and args[-1].isalpha():
            numbers = numbers[1:]
        elif where == "end" and str(args[-1]).isdigit():
            remove_items = args[3]
            numbers = numbers[:-remove_items]
        elif where == "end" and args[-1].isalpha():
            numbers.pop()
    return numbers
