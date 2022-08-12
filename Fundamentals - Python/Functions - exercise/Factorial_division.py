first_number = int(input())
second_number = int(input())


def factorial_division(first_digit, second_digit):
    result_of_first_digit = 0
    result_of_second_digit = 0
    for digit in range(0, first_digit + 1):
        result_of_first_digit *= digit
        if result_of_first_digit == 0:
            result_of_first_digit += 1
    for digit in range(0, second_digit + 1):
        result_of_second_digit *= digit
        if result_of_second_digit == 0:
            result_of_second_digit += 1
    return f"{(result_of_first_digit / result_of_second_digit):.2f}"


print(factorial_division(first_number, second_number))