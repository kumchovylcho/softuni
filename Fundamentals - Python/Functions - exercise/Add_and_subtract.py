def sum_numbers(first, second):
    result = first + second
    return result


def subtract(first_two, third):
    result = first_two - third
    return result


def add_and_subtract(first, second, third):
    sum_of_the_first_two = sum_numbers(first, second)
    result = subtract(sum_of_the_first_two, third)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))


# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
#
# def sum_numbers(first_num, second_num):
#     return first_num + second_num
#
#
# def subtract(sum, third_num):
#     return sum - third_num
#
#
# def add_and_subtract(first_number, second_number, third_number):
#     return subtract(sum_numbers(first_number, second_number), third_number)
#
#
# print(add_and_subtract(first_number, second_number, third_number))
