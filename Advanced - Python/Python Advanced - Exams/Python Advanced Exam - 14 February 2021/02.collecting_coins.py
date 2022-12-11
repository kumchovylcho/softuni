def find_player_position(size_of_matrix):
    for row in range(size_of_matrix):
        if "P" in matrix[row]:
            col = matrix[row].index("P")
            matrix[row][col] = 0
            return row, col


def check_valid_index(row, col):
    if row == matrix_size:
        row = 0
    elif row == -1:
        row = matrix_size - 1
    elif col == matrix_size:
        col = 0
    elif col == -1:
        col = matrix_size - 1
    return row, col


def collect_coins(row, col):
    if str(matrix[row][col]).isdigit():
        player_info['coins'] += matrix[row][col]
        matrix[row][col] = 0
        return
    player_info['hit wall'] = True
    player_info['coins'] //= 2


matrix_size = int(input())
matrix = [[int(col) if col.isdigit() else col for col in input().split()] for row in range(matrix_size)]
player_info = {
    'coins': 0,
    'positions': [],
    'hit wall': False
}
current_row, current_col = find_player_position(matrix_size)
player_info['positions'].append(f"[{current_row}, {current_col}]")
while player_info['coins'] < 100 and not player_info['hit wall']:
    current_direction = input()
    for where, row, col in ('up', -1, 0), ('down', 1, 0), ('left', 0, -1), ('right', 0, 1):
        if current_direction == where:
            current_row, current_col = current_row + row, current_col + col
            current_row, current_col = check_valid_index(current_row, current_col)
            player_info['positions'].append(f"[{current_row}, {current_col}]")
            collect_coins(current_row, current_col)
if not player_info['hit wall']:
    print(f"You won! You've collected {player_info['coins']} coins.")
elif player_info['hit wall']:
    print(f"Game over! You've collected {player_info['coins']} coins.")
print("Your path:")
print('\n'.join(player_info['positions']))
