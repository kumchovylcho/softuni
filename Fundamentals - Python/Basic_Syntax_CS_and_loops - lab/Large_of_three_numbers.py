import sys
first_number = int(input())
second_number = int(input())
third_number = int(input())
largest_number = -sys.maxsize
if first_number > largest_number:
    largest_number = first_number
if second_number > largest_number:
    largest_number = second_number
if third_number > largest_number:
    largest_number = third_number
print(largest_number)
