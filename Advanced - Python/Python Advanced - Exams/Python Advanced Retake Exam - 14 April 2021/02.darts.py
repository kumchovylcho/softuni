def check_valid_index(row, col, size_of_matrix):
    if 0 <= row < size_of_matrix and 0 <= col < size_of_matrix:
        return True


def dart_board(row, col, current_player):
    if check_valid_index(current_row, current_col, matrix_size):
        result = 0
        for check_row, check_col in (row, -1), (row, 0), (0, col), (-1, col):
            result += matrix[check_row][check_col]
        if matrix[row][col] == "B":
            both_players[current_player]['points'] = 0
        elif matrix[row][col] == "D":
            both_players[current_player]['points'] -= result * 2
        elif matrix[row][col] == "T":
            both_players[current_player]['points'] -= result * 3
        else:
            both_players[current_player]['points'] -= matrix[row][col]


matrix_size = 7
first_player, second_player = input().split(", ")
matrix = [[int(col) if col.isdigit() else col for col in input().split()] for row in range(matrix_size)]
both_players = {
    'player one': {'points': 501, 'throws': 0},
    'player two': {'points': 501, 'throws': 0}
}
take_turns = 1
while both_players['player one']['points'] > 0 and both_players['player two']['points'] > 0:
    current_position = input().split(", ")
    current_row, current_col = int(current_position[0].strip("(")), int(current_position[-1].strip(")"))
    if take_turns % 2 != 0:
        dart_board(current_row, current_col, "player one")
        both_players["player one"]["throws"] += 1
    elif take_turns % 2 == 0:
        dart_board(current_row, current_col, "player two")
        both_players["player two"]["throws"] += 1
    take_turns += 1
if both_players['player one']['points'] <= 0:
    print(f"{first_player} won the game with {both_players['player one']['throws']} throws!")
elif both_players['player two']['points'] <= 0:
    print(f"{second_player} won the game with {both_players['player two']['throws']} throws!")
