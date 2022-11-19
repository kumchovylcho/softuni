rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
primary_diagonal, secondary_diagonal = [], []
for row in range(rows):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][rows - row - 1])
difference = sum(primary_diagonal) - sum(secondary_diagonal)
print(abs(difference))