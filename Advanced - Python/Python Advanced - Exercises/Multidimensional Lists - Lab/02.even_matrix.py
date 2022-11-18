rows = int(input())
matrix = []
for row in range(rows):
    numbers = [int(number) for number in input().split(", ")]
    even_numbers = [digit for digit in numbers if digit % 2 == 0]
    matrix.append(even_numbers)
print(matrix)