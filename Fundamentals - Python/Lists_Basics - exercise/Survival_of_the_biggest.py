numbers = [int(number) for number in input().split()]
numbers_to_remove = int(input())
for remove in range(numbers_to_remove):
    numbers.remove(min(numbers))
# [numbers.remove(min(numbers)) for number in range(numbers_to_remove)]
print(*numbers, sep=', ')


# numbers = input().split()
# how_many_to_remove = int(input())
# int_numbers = []
# for number in numbers:
#     int_numbers.append(int(number))
# for remove in range(how_many_to_remove):
#     numbers.remove(min(numbers))
# print(*numbers, sep=", ")
