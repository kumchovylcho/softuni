def find_player():
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "P":
                matrix[row][col] = "."
                return row, col


def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True


def find_bunnies():
    bunnies_position = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                bunnies_position.append([row, col])
    return bunnies_position


def multiply_bunnies(positions_with_bunnies, check_if_dead, p_row, p_col):
    for b_row, b_col in positions_with_bunnies:
        for d_row, d_col in directions.values():
            check_row, check_col = b_row + d_row, b_col + d_col
            if check_valid_index(check_row, check_col):
                if check_row == p_row and check_col == p_col:
                    check_if_dead = True
                matrix[check_row][check_col] = "B"
    return check_if_dead


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input()] for _ in range(rows)]
commands = input()
player_row, player_col = find_player()
directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}
is_dead, is_escaped = False, False
for command in commands:
    if check_valid_index(player_row + directions[command][0],
                         player_col + directions[command][1]):
        player_row, player_col = player_row + directions[command][0], player_col + directions[command][1]
        if matrix[player_row][player_col] == "B":
            is_dead = True
    else:
        is_escaped = True
    bunnies = find_bunnies()
    is_dead = multiply_bunnies(bunnies, is_dead, player_row, player_col)
    if is_dead or is_escaped:
        break
[print(''.join(matrix[row])) for row in range(rows)]
if is_escaped:
    print(f"won: {player_row} {player_col}")
elif is_dead:
    print(f"dead: {player_row} {player_col}")
