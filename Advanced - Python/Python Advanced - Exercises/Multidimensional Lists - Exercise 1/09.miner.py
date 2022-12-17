def find_miner_and_coals():
    miner_row, miner_col = 0, 0
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == "s":
                miner_row, miner_col = row, col
                matrix[row][col] = "*"
            elif matrix[row][col] == "c":
                miner_info['coals'] += 1
    return miner_row, miner_col


def check_valid_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def check_current_square(row, col):
    if matrix[row][col] == "c":
        miner_info['coals'] -= 1
        matrix[row][col] = "*"
    elif matrix[row][col] == "e":
        miner_info['exit'] = True


matrix_size = int(input())
commands_with_directions = input().split()
matrix = [[item for item in input().split()] for _ in range(matrix_size)]
directions = {
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0},
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1},
}
miner_info = {
    'coals': 0,
    'exit': False
}
current_row, current_col = find_miner_and_coals()
for command in commands_with_directions:
    if check_valid_index(current_row + directions[command]['row'],
                         current_col + directions[command]['col']):
        current_row, current_col = current_row + directions[command]['row'], current_col + directions[command]['col']
        check_current_square(current_row, current_col)
    if not miner_info['coals'] or miner_info['exit']:
        break
if not miner_info['coals']:
    print(f"You collected all coal! ({current_row}, {current_col})")
elif miner_info['exit']:
    print(f"Game over! ({current_row}, {current_col})")
elif miner_info['coals'] and not miner_info['exit']:
    print(f"{miner_info['coals']} pieces of coal left. ({current_row}, {current_col})")
