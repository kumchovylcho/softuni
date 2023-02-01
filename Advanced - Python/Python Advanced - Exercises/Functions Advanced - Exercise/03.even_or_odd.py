def even_odd(*args):
    command = args[-1]
    operations = {
        "even": lambda numbers: [x for x in numbers[:-1] if int(x) % 2 == 0],
        "odd": lambda numbers: [x for x in numbers[:-1] if int(x) % 2 != 0]
    }
    return operations[command](args)


# def even_odd(*args):
#     command = args[-1]
#     if command == "even":
#         return [digit for digit in args[:-1] if digit % 2 == 0]
#     elif command == "odd":
#         return [digit for digit in args[:-1] if digit % 2 != 0]
