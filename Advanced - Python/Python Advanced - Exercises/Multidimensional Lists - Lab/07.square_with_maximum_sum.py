from sys import maxsize


def check_index(row, col):
    if 0 <= row + 2 <= start_row and 0 <= col + 2 <= start_col:
        return True


def check_square(row, col):
    current_numbers = []
    for check_row in range(row, row + 2):
        for check_col in range(col, col + 2):
            current_numbers.append(matrix[check_row][check_col])
    if sum(current_numbers) > best_square['sum']:
        best_square['sum'] = sum(current_numbers)
        best_square['numbers'] = current_numbers


start_row, start_col = [int(x) for x in input().split(", ")]
matrix = [[int(col) for col in input().split(", ")] for row in range(start_row)]
best_square = {
    'sum': -maxsize,
    'numbers': []
}
for row in range(start_row):
    for col in range(start_col):
        if check_index(row, col):
            check_square(row, col)
print(*best_square['numbers'][:2], sep=' ')
print(*best_square['numbers'][2:], sep=' ')
print(best_square['sum'])
