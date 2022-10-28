list_with_numbers = [int(item) for item in input().split(", ")]
start_group = 10
while list_with_numbers:
    number_below_start_group = [item for item in list_with_numbers if item <= start_group]
    list_with_numbers = [item for item in list_with_numbers if item > start_group]
    print(f"Group of {start_group}'s: {number_below_start_group}")
    start_group += 10
"""
First comprehension finds the numbers which are below or equal to the start group and then we print the list.
The second comprehension updates the main list by checking which numbers are bigger than the current group.
"""


# numbers = [int(n) for n in input().split(", ")]
# check_numbers = list()
#
# for number in range(1, 10 + 1):
#     check_numbers.clear()
#     if len(numbers) != 0:
#         for num in numbers:
#             if int(num) <= number * 10:
#                 check_numbers.append(num)
#         for d in check_numbers:
#             numbers.remove(d)
#
#         print(f"Group of {number * 10}'s: {check_numbers}")
