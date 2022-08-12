numbers = [int(number) for number in input().split()]
average_number = sum(numbers) / len(numbers)

numbers_higher_than_average_number = [number for number in numbers if number > average_number]

numbers_higher_than_average_number.sort()

if len(numbers_higher_than_average_number) >= 5:
    to_starting_position = len(numbers_higher_than_average_number) - 5
    del numbers_higher_than_average_number[0:to_starting_position]

numbers_higher_than_average_number.reverse()

if sum(numbers_higher_than_average_number) == 0:
    print("No")

elif len(numbers_higher_than_average_number) > 0:
    print(*numbers_higher_than_average_number, sep=" ")


