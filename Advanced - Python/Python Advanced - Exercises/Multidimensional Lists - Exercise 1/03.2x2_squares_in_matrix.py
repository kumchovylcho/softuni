rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append(input().split())
squares = 0
for row in range(rows):
    for col in range(cols):
        if 0 <= row + 2 <= rows and 0 <= col + 2 <= cols:
            count_identical = 0
            symbol = matrix[row][col]
            for row_check in range(row, row + 2):
                count_identical += matrix[row_check][col:col + 2].count(symbol)
            if count_identical == 4:
                squares += 1
print(squares)