numbers = [int(num) for num in input().split()]


def min_max_and_sum(number):
    min_number = f"The minimum number is {min(number)}"
    max_number = f"The maximum number is {max(number)}"
    sum_numbers = f"The sum number is: {sum(number)}"
    return f"{min_number}\n{max_number}\n{sum_numbers}"


print(min_max_and_sum(numbers))
