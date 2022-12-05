def find_rover():
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "E":
                return row, col


def explore(row, col):
    deposits = {
        "W": "Water",
        "M": "Metal",
        "C": "Concrete"
    }
    symbol = matrix[row][col]
    if symbol in deposits:
        rover_resources['deposits'].add(symbol)
        print(f"{deposits[symbol]} deposit found at ({row}, {col})")
    elif symbol == "R":
        rover_resources['rock'] = True
        print(f"Rover got broken at ({row}, {col})")


def check_boundary(row, col):
    if col < 0:
        col = matrix_size - 1
    elif col >= matrix_size:
        col = 0
    elif row < 0:
        row = matrix_size - 1
    elif row >= matrix_size:
        row = 0
    return row, col
    # for c_pos, n_pos in ((-1, 5), (6, 0)):
    #     if col == c_pos:
    #         col = n_pos
    #     if row == c_pos:
    #         row = n_pos
    # return row, col


matrix_size = 6
matrix = [[col for col in input().split()] for row in range(matrix_size)]
directions = input().split(", ")
rover_resources = {
    'deposits': set(),
    'rock': False
}
possible_directions = (
    ('up', -1, 0),
    ('down', 1, 0),
    ('left', 0, -1),
    ('right', 0, 1)
)
rover_row, rover_col = find_rover()
while directions and not rover_resources['rock']:
    current_direction = directions.pop(0)
    for direction, row, col in possible_directions:
        if direction == current_direction:
            rover_row, rover_col = rover_row + row, rover_col + col
            rover_row, rover_col = check_boundary(rover_row, rover_col)
            explore(rover_row, rover_col)
            break
if len(rover_resources['deposits']) == 3:  # if the rover found all the deposits
    print("Area suitable to start the colony.")
elif len(rover_resources['deposits']) != 3:
    print("Area not suitable to start the colony.")
