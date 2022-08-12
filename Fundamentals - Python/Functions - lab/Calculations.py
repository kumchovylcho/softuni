operation = input()
first_number = int(input())
second_number = int(input())


def calculations(number_one, number_two, operator):
    result = None
    if operator == "multiply":
        result = number_one * number_two
    elif operator == "divide":
        result = int(number_one / number_two)
    elif operator == "add":
        result = number_one + number_two
    elif operator == "subtract":
        result = number_one - number_two
    return result


print(calculations(first_number, second_number, operation))
