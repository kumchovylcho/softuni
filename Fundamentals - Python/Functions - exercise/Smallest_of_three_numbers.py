first_number = int(input())
second_number = int(input())
third_number = int(input())


def smallest_number(first, second, third):
    return min(first, second, third)


print(smallest_number(first_number, second_number, third_number))


# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
#
# def smallest_number(first, second, third):
#     lst_with_numbers = []
#     lst_with_numbers.append(first)
#     lst_with_numbers.append(second)
#     lst_with_numbers.append(third)
#     lst_with_numbers.sort()
#     return print(lst_with_numbers[0])
#
#
# smallest_number(first_number, second_number, third_number)
