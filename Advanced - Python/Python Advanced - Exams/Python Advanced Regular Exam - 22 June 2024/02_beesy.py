from enum import Enum


class FieldData(Enum):
    BEE = "B"
    HIVE = "H"
    EMPTY_POS = "-"


def create_field_and_find_bee(matrix_size):
    initial_row, initial_col = 0, 0
    field = []
    for row in range(matrix_size):
        curr_row = list(input())
        if FieldData.BEE.value in curr_row:
            initial_row, initial_col = row, curr_row.index(FieldData.BEE.value)
            curr_row[initial_col] = FieldData.EMPTY_POS.value

        field.append(curr_row)

    return initial_row, initial_col, field


def keep_inside_field(row, col, field):
    if row < 0:
        row = len(field) - 1
    elif row >= len(field):
        row = 0
    elif col < 0:
        col = len(field[0]) - 1
    elif col >= len(field[0]):
        col = 0

    return row, col


def collect_flower(row, col, field):
    value_on_field = field[row][col]
    if value_on_field.isdigit():
        field[row][col] = FieldData.EMPTY_POS.value
        return int(value_on_field)
    return 0


def main(move_row, move_col, field):
    movements = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }
    dynamic_row = move_row
    dynamic_col = move_col

    bee_energy_consumption = 1
    collected_nectar = 0
    goal_nectar = 30
    initial_energy = 15
    has_reached_hive = False
    has_restored_energy = True

    while initial_energy > 0 and not has_reached_hive:
        command = input()

        initial_energy -= bee_energy_consumption

        dynamic_row += movements[command][0]
        dynamic_col += movements[command][1]
        dynamic_row, dynamic_col = keep_inside_field(dynamic_row, dynamic_col, field)

        if field[dynamic_row][dynamic_col] == FieldData.HIVE.value:
            has_reached_hive = True
            continue

        collected_nectar += collect_flower(dynamic_row, dynamic_col, field)

        if not initial_energy and collected_nectar >= goal_nectar and has_restored_energy:
            has_restored_energy = False
            initial_energy += collected_nectar - goal_nectar
            collected_nectar = goal_nectar


    if has_reached_hive and collected_nectar >= goal_nectar:
        print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")
    elif has_reached_hive and collected_nectar < goal_nectar:
        print("Beesy did not manage to collect enough nectar.")
    elif not has_reached_hive and not initial_energy:
        print("This is the end! Beesy ran out of energy.")

    field[dynamic_row][dynamic_col] = FieldData.BEE.value
    for row in field:
        print("".join(row))


field_size = int(input())
start_row, start_col, matrix = create_field_and_find_bee(field_size)
main(start_row, start_col, matrix)