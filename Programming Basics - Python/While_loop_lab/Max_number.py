import sys
max_number = -sys.maxsize
numbers = input()
while numbers != "Stop":
    numbers = int(numbers)
    if numbers > max_number:
        max_number = numbers
    numbers = input()
print(max_number)
