numbers = [int(number) for number in input().split()]
inverted_values = [abs(number) if number < 0 else -abs(number) for number in numbers]
# inverted_values = [number * -1 for number in all_numbers]  # if the number is negative, the minuses fall
print(numbers)


# all_numbers = input()
# lst = all_numbers.split(" ")
# new_list = shuffled_cards()
# for number in lst:
#     current_number = int(number)
#     if current_number < 0:
#         current_number = abs(current_number)
#     else:
#         current_number = -abs(current_number)
#     new_list.append(current_number)
# print(new_list)
