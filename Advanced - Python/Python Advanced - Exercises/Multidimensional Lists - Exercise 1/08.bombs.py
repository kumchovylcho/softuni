def bomb_explosion(row, col):
    explosion_directions = (
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up left
        (-1, 1),  # up right
        (1, -1),  # down left
        (1, 1)  # down right
    )
    explode_power = matrix[row][col]
    for dmg_row, dmg_col in explosion_directions:
        current_row, current_col = row + dmg_row, col + dmg_col
        if check_valid_index(current_row, current_col):
            if matrix[current_row][current_col] > 0:
                matrix[current_row][current_col] -= explode_power
    matrix[row][col] = 0


def check_valid_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def find_alive_cells():
    result = []
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] > 0:
                result.append(matrix[row][col])
    return len(result), sum(result)


matrix_size = int(input())
matrix = [[int(col) for col in input().split()] for row in range(matrix_size)]
bombs_positions = input().split()
for indexes in bombs_positions:
    end_index = indexes.index(",")
    row, col = int(indexes[:end_index]), int(indexes[end_index + 1:])
    if matrix[row][col] > 0:
        bomb_explosion(row, col)
alive_cells, sum_of_alive_cells = find_alive_cells()
print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alive_cells}")
[print(*matrix[row], sep=' ') for row in range(matrix_size)]
