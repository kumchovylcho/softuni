from enum import Enum


class CellType(Enum):
    PLAYER = "P"
    MONSTER = "M"
    HEALTH = "H"
    EXIT = "X"
    EMPTY_SPOT = "-"


def create_matrix_and_find_traveller(matrix_size: int) -> tuple:
    traveller_row = 0
    traveller_col = 0
    matrix = []
    for row in range(matrix_size):
        current_row = list(input())
        if CellType.PLAYER.value in current_row:
            traveller_row = row
            traveller_col = current_row.index(CellType.PLAYER.value)
            current_row[traveller_col] = CellType.EMPTY_SPOT.value

        matrix.append(current_row)

    return traveller_row, traveller_col, matrix


def valid_index(row: int, col: int, matrix_size: int) -> bool:
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def adjust_health_after_potion(current_health: int, max_health: int) -> int:
    return max_health if current_health >= max_health else current_health


def main() -> None:
    matrix_size = int(input())
    traveller_row, traveller_col, matrix = create_matrix_and_find_traveller(
        matrix_size
    )

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, -1),
    }

    potion_recover_amount = 15
    monster_damage = 40
    start_health = 100
    max_health = 100
    has_escaped = False
    while start_health > 0 and not has_escaped:
        direction = input()

        if not valid_index(
            traveller_row + directions[direction][0],
            traveller_col + directions[direction][1],
            matrix_size,
        ):
            continue

        traveller_row += directions[direction][0]
        traveller_col += directions[direction][1]

        if matrix[traveller_row][traveller_col] == CellType.MONSTER.value:
            start_health -= monster_damage
            if start_health > 0:
                matrix[traveller_row][traveller_col] = CellType.EMPTY_SPOT.value
                continue

            start_health = 0
        elif matrix[traveller_row][traveller_col] == CellType.HEALTH.value:
            start_health += potion_recover_amount
            start_health = adjust_health_after_potion(start_health, max_health)
            matrix[traveller_row][traveller_col] = CellType.EMPTY_SPOT.value
        elif matrix[traveller_row][traveller_col] == CellType.EXIT.value:
            has_escaped = True
            continue

    if start_health == 0:
        print("Player is dead. Maze over!")
    elif start_health and has_escaped:
        print("Player escaped the maze. Danger passed!")

    print(f"Player's health: {start_health} units")
    matrix[traveller_row][traveller_col] = CellType.PLAYER.value
    for row in matrix:
        print("".join(row))



main()
