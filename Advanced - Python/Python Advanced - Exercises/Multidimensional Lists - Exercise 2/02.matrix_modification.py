def check_valid_index(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        return True
    return False


def add(row, col, amount, current_matrix):
    current_matrix[row][col] += amount
    return current_matrix


def subtract(row, col, amount, current_matrix):
    current_matrix[row][col] -= amount
    return current_matrix


rows = int(input())
matrix = [[int(col) for col in input().split()] for row in range(rows)]
command = input()
while command != "END":
    operation, row, col, value = [int(x) if x[-1].isdigit() else x for x in command.split()]
    if not check_valid_index(row, col):
        print("Invalid coordinates")
        command = input()
        continue
    if operation == "Add":
        matrix = add(row, col, value, matrix)
    elif operation == "Subtract":
        matrix = subtract(row, col, value, matrix)
    command = input()
for row_ in range(len(matrix)):
    print(*matrix[row_])