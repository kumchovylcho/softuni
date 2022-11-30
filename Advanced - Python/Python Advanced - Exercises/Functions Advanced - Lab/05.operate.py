def operate(*args):
    operation, numbers = args[0], args[1:]
    result = None
    if operation == "+":
        result = sum([digit for digit in args[1:]])
    elif operation == "-":
        first_number = args[1]
        for digit in args[2:]:
            first_number -= digit
        result = first_number
    elif operation == "*":
        first = 1
        for digit in args[1:]:
            first *= digit
        result = first
    elif operation == "/":
        first = args[1]
        for digit in args[2:]:
            first /= digit
        result = first
    return result


print(operate("*", 4, 3))