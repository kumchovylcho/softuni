numbers = [int(number) for number in input().split()]
average_number = sum(numbers) / len(numbers)

numbers_higher_than_average_number = sorted([number for number in numbers if number > average_number], reverse=True)

if len(numbers_higher_than_average_number) >= 5:
    del numbers_higher_than_average_number[5::]


if len(numbers_higher_than_average_number) == 0:
    print("No")

elif numbers_higher_than_average_number:
    print(*numbers_higher_than_average_number, sep=" ")




# all_numbers = [int(number) for number in input().split()]
# average_number = sum(all_numbers) / len(all_numbers)
#
# numbers_higher_than_average_number = []
# [numbers_higher_than_average_number.append(number) for number in all_numbers if number > average_number]
#
# numbers_higher_than_average_number.sort()
#
# if len(numbers_higher_than_average_number) >= 5:
#     to_starting_position = len(numbers_higher_than_average_number) - 5
#     del numbers_higher_than_average_number[0:to_starting_position]
#     numbers_higher_than_average_number.reverse()
#
#
# elif len(numbers_higher_than_average_number) < 5:
#     numbers_higher_than_average_number.reverse()
#
#
# if sum(numbers_higher_than_average_number) == 0:
#     print("No")
#
# elif len(numbers_higher_than_average_number) > 0:
#     print(*numbers_higher_than_average_number, sep=" ")





