def find_ship_on_field():
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == "S":
                matrix[row][col] = "-"
                return row, col


def check_current_square(row, col):
    if matrix[row][col] == "*":
        battle_field_info['mines limit'] -= 1
    elif matrix[row][col] == "C":
        battle_field_info['enemy'] -= 1
    matrix[row][col] = "-"


matrix_size = int(input())
matrix = [[col for col in input()] for row in range(matrix_size)]
directions = {
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0},
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1},
}
battle_field_info = {
    'enemy': 3,
    'mines limit': 3
}
current_row, current_col = find_ship_on_field()
while battle_field_info['enemy'] and battle_field_info['mines limit']:
    command = input()
    current_row, current_col = current_row + directions[command]['row'], current_col + directions[command]['col']
    check_current_square(current_row, current_col)
if not battle_field_info['enemy']:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
if not battle_field_info['mines limit']:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{current_row}, {current_col}]!")
matrix[current_row][current_col] = "S"
[print(''.join(matrix[row])) for row in range(matrix_size)]
