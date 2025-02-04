def create_field_and_find_ct(dimensions: tuple[int, int], counter_terrorist_symbol: str) -> tuple[int, int, list[list[str]]]:
    field = []
    rows, cols = dimensions[0], dimensions[1]
    ct_row, ct_col = 0, 0
    for row in range(rows):
        current_row = list(input())[:cols]
        if counter_terrorist_symbol in current_row:
            ct_row, ct_col = row, current_row.index(counter_terrorist_symbol)

        field.append(current_row)

    return ct_row, ct_col, field


def is_in_field(step_row: int, step_col: int, field_dimensions: tuple[int, int]) -> bool:
    return 0 <= step_row < field_dimensions[0] and 0 <= step_col < field_dimensions[1]


def main() -> None:
    dimensions = tuple(int(x) for x in input().split(", "))
    timeleft = 16  # seconds
    counter_terrorist = "C"
    terrorist = "T"
    bomb = "B"
    empty = "*"
    defused = "D"
    bomb_explodes = "X"
    defuse_time_needed = 4

    ct_row, ct_col, field = create_field_and_find_ct(dimensions, counter_terrorist)
    ct_initial_row, ct_initial_col = ct_row, ct_col
    field[ct_row][ct_col] = empty

    movement = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    while timeleft > 0:
        command = input()

        if command in movement:
            timeleft -= 1
            check_row, check_col = ct_row + movement[command][0], ct_col + movement[command][1]
            if not is_in_field(check_row, check_col, dimensions):
                continue

            ct_row, ct_col = check_row, check_col

            block = field[ct_row][ct_col]
            if block == terrorist:
                field[ct_row][ct_col] = empty
                print("Terrorists win!")
                break
        elif command not in movement:
            if timeleft < 2:
                break

            if field[ct_row][ct_col] != bomb:
                timeleft -= 2
                continue

            if timeleft < defuse_time_needed:
                field[ct_row][ct_col] = bomb_explodes
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {defuse_time_needed - timeleft} second/s.")
                break

            timeleft -= defuse_time_needed
            field[ct_row][ct_col] = defused
            print("Counter-terrorist wins!")
            print(f"Bomb has been defused: {timeleft} second/s remaining.")
            break

    else:
        print("Terrorists win!")
        print("Bomb was not defused successfully!")
        print("Time needed: 0 second/s.")


    field[ct_initial_row][ct_initial_col] = counter_terrorist
    for row in field:
        print("".join(row))


main()
