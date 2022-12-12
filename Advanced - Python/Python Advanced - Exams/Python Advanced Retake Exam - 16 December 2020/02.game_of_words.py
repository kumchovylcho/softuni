def find_player(size_of_matrix):
    for row in range(size_of_matrix):
        if "P" in matrix[row]:
            col = matrix[row].index("P")
            matrix[row][col] = "-"
            return row, col


def check_valid_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def check_for_letter(row, col, current_string):
    if matrix[row][col] != "-":
        current_string += matrix[row][col]
        matrix[row][col] = "-"
    return current_string


main_string = input()
matrix_size = int(input())
matrix = [[col for col in input()] for row in range(matrix_size)]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
player_row, player_col = find_player(matrix_size)
number_of_moves = int(input())
for _ in range(number_of_moves):
    command = input()
    if check_valid_index(player_row + directions[command][0],
                         player_col + directions[command][1]):
        player_row, player_col = player_row + directions[command][0], player_col + directions[command][1]
        main_string = check_for_letter(player_row, player_col, main_string)
    else:
        main_string = main_string[:-1]
matrix[player_row][player_col] = "P"
print(main_string)
[print(*matrix[row], sep='') for row in range(matrix_size)]
