numbers = int(input())
total = 0
count_current_numbers = 0
while count_current_numbers < numbers:
    count_current_numbers += 1
    current_number = int(input())
    total += current_number

average_number = total / count_current_numbers
print(f"{average_number:.2f}")
