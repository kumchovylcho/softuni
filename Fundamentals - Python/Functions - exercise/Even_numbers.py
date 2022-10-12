def is_even(digit):
    if digit % 2 == 0:
        return True
    else:
        return False


numbers = [int(digit) for digit in input().split()]
filtered_numbers = filter(is_even, numbers)
final_result = [number for number in filtered_numbers]
print(final_result)


# all_numbers = input().split()
#
#
# def get_even_numbers(number):
#     lst_with_even_numbers = []
#     for num in number:
#         num = int(num)
#         if num % 2 == 0:
#             lst_with_even_numbers.append(num)
#     return lst_with_even_numbers
#
#
# print(get_even_numbers(all_numbers))