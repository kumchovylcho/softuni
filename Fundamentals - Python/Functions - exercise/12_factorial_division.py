def get_factorial(number: int):
    output = 1
    for i in range(1, number + 1):
        output *= i

    return output

    # Recursive
    # if number == 0:
    #     return 1
    #
    # return number * get_factorial(number - 1)


first_number = int(input())
second_number = int(input())
result = get_factorial(first_number) / get_factorial(second_number)
print(f"{result:.2f}")



#########################################################################



# def factorial_numbers(first, second):
#     result_first_number, result_second_number = 1, 1
#     for first_digit in range(1, first + 1):
#         result_first_number *= first_digit
#     for second_digit in range(1, second + 1):
#         result_second_number *= second_digit
#     return result_first_number / result_second_number
#
#
# first_number = int(input())
# second_number = int(input())
# result = factorial_numbers(first_number, second_number)
# print(f"{result:.2f}")



# first_number = int(input())
# second_number = int(input())
#
#
# def factorial_division(first_digit, second_digit):
#     result_of_first_digit = 0
#     result_of_second_digit = 0
#     for digit in range(0, first_digit + 1):
#         result_of_first_digit *= digit
#         if result_of_first_digit == 0:
#             result_of_first_digit += 1
#     for digit in range(0, second_digit + 1):
#         result_of_second_digit *= digit
#         if result_of_second_digit == 0:
#             result_of_second_digit += 1
#     return f"{(result_of_first_digit / result_of_second_digit):.2f}"
#
#
# print(factorial_division(first_number, second_number))