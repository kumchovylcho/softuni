def create_field(field_size: int):
    field = []
    start_r, start_c = 0, 0

    for i in range(field_size):
        current_row = list(input())

        field.append(current_row)
        if "s" in current_row:
            squirrel_col = current_row.index("s")

            start_r, start_c = i, squirrel_col
            field[start_r][start_c] = "*"

    return field, start_r, start_c


def valid_index(row: int, col: int):
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def can_step_on_square(field: list, row: int, col: int):
    return field[row][col] in ("h", "*")


def check_if_hazelnut(field: list, row: int, col: int):
    return field[row][col] == "h"


matrix_size = int(input())
commands = input().split(", ")

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),
    "up": (-1, 0),
}

collected_hazelnuts = 0
GOAL_OF_HAZELNUTS = 3

matrix, row, col = create_field(matrix_size)

game_over_messages = []
for command in commands:
    m_row, m_col = row + directions[command][0], col + directions[command][1]

    if not valid_index(m_row, m_col):
        game_over_messages.append("The squirrel is out of the field.")
        break

    row, col = m_row, m_col

    if not can_step_on_square(matrix, row, col):
        game_over_messages.append("Unfortunately, the squirrel stepped on a trap...")
        break

    if check_if_hazelnut(matrix, row, col):
        matrix[row][col] = "*"
        collected_hazelnuts += 1

        if collected_hazelnuts == GOAL_OF_HAZELNUTS:
            break


if game_over_messages:
    print(game_over_messages[0])

elif collected_hazelnuts < GOAL_OF_HAZELNUTS:
    print("There are more hazelnuts to collect.")

elif collected_hazelnuts >= GOAL_OF_HAZELNUTS:
    print("Good job! You have collected all hazelnuts!")


print(f"Hazelnuts collected: {collected_hazelnuts}")
