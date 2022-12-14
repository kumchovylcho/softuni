def number_generator():
    directions = (
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up left
        (-1, 1),  # up right
        (1, -1),  # down left
        (1, 1)  # down right
    )
    for row in range(matrix_size):
        for col in range(matrix_size):
            bombs_hit = 0
            look_row, look_col = row, col
            if matrix[look_row][look_col] == "*":
                continue
            for check_row, check_col in directions:
                look_row, look_col = look_row + check_row, look_col + check_col
                if check_index(look_row, look_col):
                    if matrix[look_row][look_col] == "*":
                        bombs_hit += 1
                look_row, look_col = row, col
            matrix[row][col] = str(bombs_hit)


def check_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


matrix_size = int(input())
matrix = [["0" for col in range(matrix_size)] for row in range(matrix_size)]
bombs_count = int(input())
for _ in range(bombs_count):
    mine_position = input().split(", ")
    mine_row, mine_col = int(mine_position[0][1:]), int(mine_position[1][:-1])
    matrix[mine_row][mine_col] = "*"
number_generator()
[print(*matrix[row], sep=' ') for row in range(matrix_size)]
