rows = int(input())
matrix = [[int(col) for col in input().split(", ")] for row in range(rows)]
primary_diagonal = []
secondary_diagonal = []
for row in range(rows):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][rows - row - 1])
print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")