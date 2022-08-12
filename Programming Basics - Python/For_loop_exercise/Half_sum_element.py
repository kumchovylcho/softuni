import sys
numbers = int(input())
max_number = -sys.maxsize
sum = 0
for number in range(1, numbers + 1):
    current_numbers = int(input())
    sum += current_numbers
    if current_numbers > max_number:
        max_number = current_numbers
total = sum - max_number
if total == max_number:
    print(f"Yes\nSum = {max_number}")
else:
    diff = abs(max_number - total)
    print(f"No\nDiff = {diff}")
