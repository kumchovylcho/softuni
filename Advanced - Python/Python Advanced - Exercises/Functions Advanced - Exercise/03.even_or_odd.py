def even_odd(*args):
    command = args[-1]
    if command == "even":
        return [digit for digit in args[:-1] if digit % 2 == 0]
    elif command == "odd":
        return [digit for digit in args[:-1] if digit % 2 != 0]
