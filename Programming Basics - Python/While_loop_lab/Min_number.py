import sys
min_number = sys.maxsize
numbers = input()
while numbers != "Stop":
    numbers = int(numbers)
    if numbers < min_number:
        min_number = numbers
    numbers = input()
print(min_number)
