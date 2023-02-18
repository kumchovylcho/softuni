def find_starter_position():
    for row in range(ROWS):
        if "B" in matrix[row]:
            col = matrix[row].index("B")
            matrix[row][col] = "-"
            return row, col


def check_valid_index(row, col):
    if 0 <= row < ROWS and 0 <= col < COLS:
        return True


def check_furniture(row, col):
    if matrix[row][col] == "O":
        return True


def check_for_other_player(row, col):
    if matrix[row][col] == "P":
        matrix[row][col] = "-"
        return True


ROWS, COLS = [int(x) for x in input().split()]
matrix = [[c for c in input().split()] for r in range(ROWS)]

players_touched = 0
steps = 0

start_row, start_col = find_starter_position()

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()
while players_touched < 3 and command != "Finish":
    try_row, try_col = start_row + directions[command][0], start_col + directions[command][1]
    if check_valid_index(try_row, try_col):
        if not check_furniture(try_row, try_col):
            if check_for_other_player(try_row, try_col):
                players_touched += 1

            start_row, start_col = try_row, try_col
            steps += 1

    command = input()

print("Game over!")
print(f"Touched opponents: {players_touched} Moves made: {steps}")