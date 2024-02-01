def create(row, col, replacement_value):
    if matrix[row][col] == ".":
        matrix[row][col] = replacement_value


def update(row, col, replacement_value, show_square=False):
    if matrix[row][col] != ".":
        if show_square:
            print(matrix[row][col])
        elif not show_square:
            matrix[row][col] = replacement_value


def delete(row, col):
    update(row, col, ".")


def read(row, col):
    update(row, col, "", show_square=True)


def show_result():
    [print(' '.join(matrix[row])) for row in range(matrix_size)]


matrix_size = 6
matrix = [[col for col in input().split()] for row in range(matrix_size)]
start_row, start_col = [int(x) for x in input() if x.isdigit()]

operations = {
    'Create': create,
    'Update': update,
    'Delete': delete,
    'Read': read
}

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

command = input()
while command != "Stop":
    operation, direction, *value = [x for x in command.split(", ")]

    start_row, start_col = start_row + movement[direction][0], start_col + movement[direction][1]
    operations[operation](start_row, start_col, *value)

    command = input()

show_result()
