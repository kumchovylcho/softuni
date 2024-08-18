def create_matrix_and_find_player(field_size: int) -> tuple:
    p_row, p_col = 0, 0
    matrix = []
    for row in range(field_size):
        row_input = input().split()
        if PLAYER_SYMBOL in row_input:
            p_row, p_col = row, row_input.index(PLAYER_SYMBOL)
            row_input[p_col] = WALK_OVER

        matrix.append(row_input)

    return matrix, p_row, p_col


def display_result(field: list, output_msgs_list: list) -> None:
    print("\n".join(output_msgs_list))
    for row in field:
        print(" ".join(row))


def valid_index(row: int, col: int, field: list) -> bool:
    return 0 <= row < len(field) and 0 <= col < len(field[0])


def explore_block(row: int, col: int, field: list) -> int:
    symbol = field[row][col]
    if symbol == OBSTACLE:
        return -1

    if symbol == STAR:
        return 1

    return 0


def main(stars: int, field_size: int) -> None:
    matrix, start_row, start_col = create_matrix_and_find_player(field_size)

    while 0 < stars < GOAL_STARS:
        direction = input()

        try_row, try_col = start_row + movements[direction][0], start_col + movements[direction][1]
        if not valid_index(try_row, try_col, matrix):
            start_row, start_col = PUNISH_TELEPORT_LOCATION
            block_value = explore_block(start_row, start_col, matrix)

            if block_value > 0:
                stars += block_value
                matrix[start_row][start_col] = WALK_OVER
            continue

        block_value = explore_block(try_row, try_col, matrix)
        if block_value < 0:
            stars += block_value
            continue

        start_row += movements[direction][0]
        start_col += movements[direction][1]

        stars += explore_block(start_row, start_col, matrix)
        matrix[start_row][start_col] = WALK_OVER


    matrix[start_row][start_col] = PLAYER_SYMBOL
    display_result(
        matrix,
        [
            GAME_WON_MESSAGE if stars == GOAL_STARS else GAME_LOST_MESSAGE,
            f"Your final position is [{start_row}, {start_col}]"
        ]
    )


GAME_WON_MESSAGE = "You won! You have collected 10 stars."
GAME_LOST_MESSAGE = "Game over! You are out of any stars."
PLAYER_SYMBOL = "P"
STAR = "*"
OBSTACLE = "#"
WALK_OVER = "."
GOAL_STARS = 10
stars_collected = 2
PUNISH_TELEPORT_LOCATION = (0, 0)

movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

main(stars_collected, int(input()))
