def create(row, col, replacement_value):
    if matrix[row][col] == ".":
        matrix[row][col] = replacement_value


def update(row, col, replacement_value):
    if matrix[row][col] != ".":
        matrix[row][col] = replacement_value


def delete(row, col):
    if matrix[row][col] != ".":
        matrix[row][col] = "."


def read(row, col):
    if matrix[row][col] != ".":
        print(matrix[row][col])


def show_result():
    [print(' '.join(matrix[row])) for row in range(matrix_size)]


matrix_size = 6
matrix = [[col for col in input().split()] for row in range(matrix_size)]
start_row, start_col = [int(x) for x in input() if x.isdigit()]
start_position = [start_row, start_col]
operations = {
    'Create': create,
    'Update': update,
    'Delete': delete,
    'Read': read
}
command = input()
while command != "Stop":
    operation, direction, *value = [x for x in command.split(", ")]
    for where, row, col in ('up', -1, 0), ('down', 1, 0), ('right', 0, 1), ('left', 0, -1):
        if where == direction:
            start_position = start_position[0] + row, start_position[1] + col
            operations[operation](*start_position, *value)
    command = input()
show_result()
