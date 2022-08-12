import sys
numbers = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize
for number in range(1, numbers + 1):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if min_number > current_number:
        min_number = current_number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
