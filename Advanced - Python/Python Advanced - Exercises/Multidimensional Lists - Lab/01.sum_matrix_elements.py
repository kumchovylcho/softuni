rows, columns = [int(digit) for digit in input().split(", ")]
matrix = []
total_value = 0
for row in range(rows):
    current_row = [int(digit) for digit in input().split(", ")]
    matrix.append(current_row)
for row in matrix:
    total_value += sum(row)
print(total_value)
print(matrix)