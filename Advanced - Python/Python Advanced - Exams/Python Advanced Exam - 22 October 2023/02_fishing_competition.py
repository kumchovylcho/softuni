from typing import Tuple


def valid_index(row: int, col: int) -> bool:
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def traverse_ship(row: int, col: int) -> Tuple[int, int]:
    if row < 0:
        row = matrix_size - 1

    elif row >= matrix_size:
        row = 0

    if col < 0:
        col = matrix_size - 1

    elif col >= matrix_size:
        col = 0

    return row, col


ship_symbol = "S"
end_program_command = "collect the nets"
whirlpool_symbol = "W"
empty_symbol = "-"
quota_goal = 20

matrix_size = int(input())
matrix = []
start_row, start_col = 0, 0

for i in range(matrix_size):
    row = list(input())

    if ship_symbol in row:
        col = row.index(ship_symbol)
        start_row, start_col = i, col
        row[col] = empty_symbol

    matrix.append(row)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

collected_fish = 0
has_sank = False

command = input()
while command != end_program_command:
    start_row += directions[command][0]
    start_col += directions[command][1]

    if not valid_index(start_row, start_col):
        start_row, start_col = traverse_ship(start_row, start_col)

    curr_pos = matrix[start_row][start_col]
    if curr_pos.isdigit():
        collected_fish += int(curr_pos)

    if curr_pos == whirlpool_symbol:
        has_sank = True
        collected_fish = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{start_row},{start_col}]")
        break

    matrix[start_row][start_col] = empty_symbol

    command = input()


if collected_fish >= quota_goal:
    print("Success! You managed to reach the quota!")

elif not has_sank and collected_fish < quota_goal:
    tons_needed = quota_goal - collected_fish
    print(f"You didn't catch enough fish and didn't reach the quota! You need {tons_needed} tons of fish more.")

if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")

matrix[start_row][start_col] = ship_symbol

if not has_sank:
    for m_row in matrix:
        print("".join(m_row))
