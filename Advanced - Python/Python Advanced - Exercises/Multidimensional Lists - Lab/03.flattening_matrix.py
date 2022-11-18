rows = int(input())
matrix = []
for row in range(rows):
    numbers = [int(number) for number in input().split(", ")]
    matrix.extend(numbers)
print(matrix)