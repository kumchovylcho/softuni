main_list = [float(digit) for digit in input().split()]


def round_numbers(numbers):
    result = [round(digit) for digit in numbers]
    return result


print(round_numbers(main_list))


# all_numbers = input().split()
# new_numbers = []
#
#
# def rounding_the_number(current_number):
#     current_number = float(current_number)
#     result = round(current_number)
#     new_numbers.append(result)
#
#
# for number in all_numbers:
#     rounding_the_number(number)
# print(new_numbers)


# all_numbers = [round(float(number)) for number in input().split()]
# print(all_numbers)

