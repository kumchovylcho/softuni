def find_santa_and_nice_kids():
    santa_pos = []
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == "S":
                santa_pos.append(row)
                santa_pos.append(col)
                matrix[row][col] = "-"
            elif matrix[row][col] == "V":
                santa_info['all nice kids'] += 1
    santa_info['left nice'] = santa_info['all nice kids']
    return santa_pos


def check_valid_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def check_square(row, col):
    if matrix[row][col] == "V":
        matrix[row][col] = "-"
        santa_info['presents'] -= 1
        santa_info['left nice'] -= 1
    elif matrix[row][col] == "X":
        matrix[row][col] = "-"
    elif matrix[row][col] == "C":
        for d_row, d_col in directions.values():
            check_row, check_col = row + d_row, col + d_col
            if check_valid_index(check_row, check_col):
                if matrix[check_row][check_col] == "V":
                    matrix[check_row][check_col] = "-"
                    santa_info['presents'] -= 1
                    santa_info['left nice'] -= 1
                elif matrix[check_row][check_col] == "X":
                    matrix[check_row][check_col] = "-"
                    santa_info['presents'] -= 1
                if not santa_info['presents']:
                    return


all_presents = int(input())
matrix_size = int(input())
matrix = [[x for x in input().split()] for _ in range(matrix_size)]
directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}
santa_info = {
    'left nice': 0,
    'all nice kids': 0,
    'presents': all_presents
}
santa_row, santa_col = find_santa_and_nice_kids()
command = input()
while command != "Christmas morning":
    if check_valid_index(santa_row + directions[command][0],
                         santa_col + directions[command][1]):
        santa_row, santa_col = santa_row + directions[command][0], santa_col + directions[command][1]
        check_square(santa_row, santa_col)
    if not santa_info['presents']:
        break
    command = input()
if not santa_info['presents'] and santa_info['left nice']:
    print("Santa ran out of presents!")
matrix[santa_row][santa_col] = "S"
[print(' '.join(matrix[row])) for row in range(matrix_size)]
if not santa_info['left nice']:
    print(f"Good job, Santa! {santa_info['all nice kids']} happy nice kid/s.")
elif santa_info['left nice']:
    print(f"No presents for {santa_info['left nice']} nice kid/s.")
