def find_snake_and_tunnels(size_of_matrix):
    s_row, s_col, tunnel = 0, 0, []
    for row in range(size_of_matrix):
        for col in range(size_of_matrix):
            if matrix[row][col] == "S":
                s_row, s_col = row, col
                matrix[row][col] = "."
            elif matrix[row][col] == "B":
                tunnel.append([row, col])
    return s_row, s_col, tunnel


def check_valid_index(row, col, size_of_matrix):
    if 0 <= row < size_of_matrix and 0 <= col < size_of_matrix:
        return True


def check_obstacles(row, col, tunnel_pos):
    if matrix[row][col] == "*":
        snake['food'] += 1
        matrix[row][col] = "."
    elif matrix[row][col] == "B":
        matrix[row][col] = "."
        teleport_location = [x for x in tunnel_pos if x != [row, col]]
        row, col = teleport_location[0][0], teleport_location[0][1]
        matrix[row][col] = "."
    elif matrix[row][col] == "-":
        matrix[row][col] = "."
    return row, col


matrix_size = int(input())
matrix = [[col for col in input()] for row in range(matrix_size)]
snake = {
    'food': 0,
    'outside': False
}
directions = {
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0},
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1}
}
snake_row, snake_col, tunnels = find_snake_and_tunnels(matrix_size)
while snake['food'] < 10 and not snake['outside']:
    command = input()
    snake_row, snake_col = snake_row + directions[command]['row'], snake_col + directions[command]['col']
    if check_valid_index(snake_row, snake_col, matrix_size):
        snake_row, snake_col = check_obstacles(snake_row, snake_col, tunnels)
        continue
    snake['outside'] = True
if snake['outside']:
    print("Game over!")
elif not snake['outside']:
    matrix[snake_row][snake_col] = "S"
    print("You won! You fed the snake.")
print(f"Food eaten: {snake['food']}")
[print(''.join(matrix[row])) for row in range(matrix_size)]
