numbers_with_zeros = [int(number) for number in input().split(", ")]

finding_the_zeros = [number for number in numbers_with_zeros if number == 0]
numbers_without_zeros = [number for number in numbers_with_zeros if number > 0]
list_with_zeros_at_the_back = numbers_without_zeros + finding_the_zeros

print(list_with_zeros_at_the_back)
