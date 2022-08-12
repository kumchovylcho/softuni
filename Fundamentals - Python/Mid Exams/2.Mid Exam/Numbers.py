numbers = [int(number) for number in input().split()]
average_number = sum(numbers) / len(numbers)

numbers_higher_than_average_number = sorted([number for number in numbers if number > average_number], reverse=True)

if len(numbers_higher_than_average_number) >= 5:
    del numbers_higher_than_average_number[5::]


if len(numbers_higher_than_average_number) == 0:
    print("No")

elif numbers_higher_than_average_number:
    print(*numbers_higher_than_average_number, sep=" ")


