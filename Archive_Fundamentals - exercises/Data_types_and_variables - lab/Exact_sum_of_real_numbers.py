from decimal import Decimal
numbers = int(input())
total = 0
for _ in range(numbers):
    number = Decimal(input())
    total += number
print(total)