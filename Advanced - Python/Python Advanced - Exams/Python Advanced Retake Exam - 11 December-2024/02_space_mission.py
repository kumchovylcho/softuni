def create_matrix_and_find_spaceship(size: int,
                                     spaceship_symbol: str
                                     ) -> tuple[list[list[str]], int, int]:
    field = []
    spaceship_row = 0
    spaceship_col = 0
    for row in range(size):
        current_row = input().split()
        if spaceship_symbol in current_row:
            spaceship_row = row
            spaceship_col = current_row.index(spaceship_symbol)
            current_row[spaceship_col] = EMPTY

        field.append(current_row)

    return field, spaceship_row, spaceship_col


def valid_position(row: int, col: int, size: int):
    return 0 <= row < size and 0 <= col < size


matrix_size = int(input())
SPACESHIP = "S"
METEOR = "M"
DESTINATION = "P"
SPACE_STATIONS = "R"
EMPTY = "."
METEOR_DAMAGE = 5
REFUEL_AMOUNT = 10
MAX_FUEL = 100
INITIAL_FUEL = 100
FUEL_PER_MOVE = 5
MIN_FUEL = 5

MOVEMENT = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix, start_row, start_col = create_matrix_and_find_spaceship(matrix_size, SPACESHIP)

planet_b_reached = False
within_bounds = True
while not planet_b_reached and INITIAL_FUEL >= MIN_FUEL and within_bounds:
    move_to = input()

    next_row = start_row + MOVEMENT[move_to][0]
    next_col = start_col + MOVEMENT[move_to][1]
    if not valid_position(next_row, next_col, matrix_size):
        within_bounds = False
        continue

    start_row += MOVEMENT[move_to][0]
    start_col += MOVEMENT[move_to][1]
    INITIAL_FUEL -= FUEL_PER_MOVE

    block = matrix[start_row][start_col]
    if block == SPACE_STATIONS:
        INITIAL_FUEL = min(INITIAL_FUEL + REFUEL_AMOUNT, MAX_FUEL)
    elif block == METEOR:
        matrix[start_row][start_col] = EMPTY
        INITIAL_FUEL -= FUEL_PER_MOVE
    elif block == DESTINATION:
        planet_b_reached = True


if planet_b_reached:
    print(f"Mission accomplished! The spaceship reached Planet B with {INITIAL_FUEL} resources left.")
elif not planet_b_reached and INITIAL_FUEL < MIN_FUEL:
    print("Mission failed! The spaceship was stranded in space.")
elif not within_bounds:
    print("Mission failed! The spaceship was lost in space.")


if not planet_b_reached:
    matrix[start_row][start_col] = SPACESHIP

for row in matrix:
    print(" ".join(row))
