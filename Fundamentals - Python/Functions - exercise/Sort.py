def sort_numbers(numbers):
    return sorted(numbers)


all_numbers = [int(number) for number in input().split()]
print(sort_numbers(all_numbers))


# all_numbers = print(sorted([int(digit) for digit in input().split()]))


# all_numbers = input().split()
#
#
# def sort(lst):
#     new_list = []
#     for number in lst:
#         number = int(number)
#         new_list.append(number)
#     return sorted(new_list)
#
#
# print(sort(all_numbers))
