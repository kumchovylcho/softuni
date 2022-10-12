def min_max_and_sum(number):
    return min(number), max(number), sum(numbers)


numbers = [int(num) for num in input().split()]
min_of_numbers, max_of_numbers, sum_of_numbers = min_max_and_sum(numbers)
print(f"The minimum number is {min_of_numbers}")
print(f"The maximum number is {max_of_numbers}")
print(f"The sum number is: {sum_of_numbers}")
