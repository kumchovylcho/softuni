def find_queens():
    found_queens = []
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == "Q":
                found_queens.append([row, col])
    return found_queens


def check_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def try_to_reach_king(row, col):
    possible_directions = (
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up left
        (-1, 1),  # up right
        (1, 1),  # down right
        (1, -1)  # down left
    )
    look_row, look_col = row, col
    for check_row, check_col in possible_directions:
        queen_on_the_way = False
        for look in range(matrix_size):
            look_row, look_col = look_row + check_row, look_col + check_col
            if check_index(look_row, look_col):
                if matrix[look_row][look_col] == "Q":
                    queen_on_the_way = True
                if matrix[look_row][look_col] == "K" and not queen_on_the_way:
                    return True
            else:
                look_row, look_col = row, col
                break


matrix_size = 8
matrix = [[col for col in input().split()] for _ in range(matrix_size)]
all_queens = find_queens()
queens_that_can_attack = []
for queen in all_queens:
    if try_to_reach_king(queen[0], queen[1]):
        queens_that_can_attack.append(queen)
if queens_that_can_attack:
    [print(queens_that_can_attack[row]) for row in range(len(queens_that_can_attack))]
elif not queens_that_can_attack:
    print("The king is safe!")
