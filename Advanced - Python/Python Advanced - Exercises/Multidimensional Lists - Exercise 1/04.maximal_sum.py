from sys import maxsize
rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = -maxsize
best_combo = []
for row in range(rows):
    for col in range(cols):
        if 0 <= row + 3 <= rows and 0 <= col + 3 <= cols:
            current_combo = []
            current_sum = 0
            for row_ in range(row, row + 3):
                result = matrix[row_][col:col + 3]
                current_combo.append(result)
                current_sum += sum(result)
            if current_sum > max_sum:
                max_sum = current_sum
                best_combo = current_combo
print(f"Sum = {max_sum}")
for _row in range(len(best_combo)):
    print(*best_combo[_row], sep=' ')
