numbers = input()
average_number = sum(numbers) / len(numbers)

top_5_numbers = []

for number in numbers:
    if len(top_5_numbers) > 5:
        break
    if number > average_number:
        top_5_numbers.append(number)
