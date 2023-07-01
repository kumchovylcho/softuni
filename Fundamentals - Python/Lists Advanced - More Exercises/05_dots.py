def check_wall(row: int, col: int):
    return matrix[row][col] in "-–"


def valid_index(row: int, col: int):
    return 0 <= row < rows and 0 <= col < cols


def is_visited(row: int, col: int):
    return matrix[row][col] == "v"


def is_dot(row: int, col: int):
    return matrix[row][col] == "."


def find_max_connections(row: int, col: int):
    if not valid_index(row, col):
        return

    if check_wall(row, col):
        return

    if is_visited(row, col):
        return

    path_connections.append(1)
    if is_dot(row, col):
        max_connections.append(sum(path_connections))

    matrix[row][col] = "v"

    find_max_connections(row + 1, col)
    find_max_connections(row - 1, col)
    find_max_connections(row, col + 1)
    find_max_connections(row, col - 1)


rows = int(input())

matrix = []
for row in range(rows):
    current_row = input().split()
    matrix.append(current_row)

cols = len(matrix[0])

max_connections = []
for row in range(rows):
    for col in range(cols):
        if check_wall(row, col):
            continue

        path_connections = []
        find_max_connections(row, col)


print(max(max_connections) if max_connections else 0)
