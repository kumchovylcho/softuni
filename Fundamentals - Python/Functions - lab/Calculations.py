calculator_executor = {
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: int(a / b),
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b
}

current_operator = input()
current_a = int(input())
current_b = int(input())

print(calculator_executor[current_operator](current_a, current_b))


# def calculations(number_one, number_two, operator):
#     result = None
#     if operator == "multiply":
#         result = number_one * number_two
#     elif operator == "divide":
#         result = int(number_one / number_two)
#     elif operator == "add":
#         result = number_one + number_two
#     elif operator == "subtract":
#         result = number_one - number_two
#     return result
#
#
# operation = input()
# first_number = int(input())
# second_number = int(input())
#
# print(calculations(first_number, second_number, operation))
