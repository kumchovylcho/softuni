def odd_and_even(number):
    sum_of_even = [int(digit) for digit in number if int(digit) % 2 == 0]
    sum_of_odd = [int(digit) for digit in number if int(digit) % 2 != 0]
    return sum_of_even, sum_of_odd


number_as_string = input()
even_numbers_sum, odd_numbers_sum = odd_and_even(number_as_string)
print(f"Odd sum = {sum(odd_numbers_sum)}, Even sum = {sum(even_numbers_sum)}")


# number = input()
#
#
# def odd_and_even(digit):
#     even = 0
#     odd = 0
#     for num in digit:
#         num = int(num)
#         if num % 2 == 0:
#             even += num
#         elif num % 2 != 0:
#             odd += num
#     return f"Odd sum = {odd}, Even sum = {even}"
#
#
# print(odd_and_even(number))
