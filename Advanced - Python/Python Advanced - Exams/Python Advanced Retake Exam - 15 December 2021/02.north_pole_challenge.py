def find_santa_and_count_items_on_map():
    s_row, s_col = 0, 0
    for row in range(rows):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "Y":
                matrix[row][col] = "x"
                s_row, s_col = row, col

            elif matrix[row][col] not in "x.":
                items_on_map[matrix[row][col]] += 1

    return s_row, s_col


def check_for_traverse(row, col):
    if row >= rows:
        row = 0
    elif row < 0:
        row = rows - 1

    elif col >= cols:
        col = 0
    elif col < 0:
        col = cols - 1

    return row, col


def try_to_collect_item(row, col):
    item = matrix[row][col]
    if matrix[row][col] in collected_items.keys():
        collected_items[item] += 1

        items_on_map[item] -= 1


def move(s_row: int, s_col: int, travel_steps: int, where_to: str):
    for _ in range(travel_steps):
        s_row, s_col = directions[where_to][0] + s_row, directions[where_to][1] + s_col

        s_row, s_col = check_for_traverse(s_row, s_col)

        try_to_collect_item(s_row, s_col)

        matrix[s_row][s_col] = "x"

        if not sum(items_on_map.values()):
            break

    return s_row, s_col


rows, cols = map(int, input().split(", "))
matrix = [[x for x in input().split()] for _ in range(rows)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

collected_items = {
    "D": 0,
    "G": 0,
    "C": 0,
}

items_on_map = {
    "D": 0,
    "G": 0,
    "C": 0,
}

santa_row, santa_col = find_santa_and_count_items_on_map()

collected_all_items = False

command = input()
while command != "End":
    direction, steps = [int(x) if x.isdigit() else x for x in command.split("-")]

    santa_row, santa_col = move(santa_row, santa_col, steps, direction)

    if not sum(items_on_map.values()):
        collected_all_items = True
        break

    command = input()


if collected_all_items:
    print("Merry Christmas!")

matrix[santa_row][santa_col] = "Y"

print("You've collected:")
print(f"- {collected_items['D']} Christmas decorations")
print(f"- {collected_items['G']} Gifts")
print(f"- {collected_items['C']} Cookies")

[print(*matrix[row]) for row in range(rows)]


# def find_santa(rows):
#     for row in range(rows):
#         if "Y" in matrix[row]:
#             col = matrix[row].index("Y")
#             matrix[row][col] = "x"
#             return row, col
#
#
# def check_collected_items():
#     result = 0
#     for row in range(matrix_rows):
#         for col in range(matrix_cols):
#             if matrix[row][col] != "." and matrix[row][col] != "x" and matrix[row][col] != "Y":
#                 result += 1
#     if result == 0:
#         return True
#     return False
#
#
# def movement(current_row, current_col, direction, moves):
#     for where, row, col in possible_positions:
#         if direction == where:
#             for _ in range(moves):
#                 current_row, current_col = current_row + row, current_col + col
#                 if current_row == -1:
#                     current_row = matrix_rows - 1
#                 elif current_row == matrix_rows:
#                     current_row = 0
#                 elif current_col == -1:
#                     current_col = matrix_cols - 1
#                 elif current_col == matrix_cols:
#                     current_col = 0
#                 check_square(current_row, current_col)
#                 matrix[current_row][current_col] = "x"
#                 if check_collected_items():
#                     return current_row, current_col
#     return current_row, current_col
#
#
# def check_square(row, col):
#     if matrix[row][col] == "D":
#         collected_items['Christmas decorations'] += 1
#     elif matrix[row][col] == "G":
#         collected_items['Gifts'] += 1
#     elif matrix[row][col] == "C":
#         collected_items['Cookies'] += 1
#
#
# matrix_rows, matrix_cols = [int(x) for x in input().split(", ")]
# matrix = [[col for col in input().split()] for row in range(matrix_rows)]
# santa_row, santa_col = find_santa(matrix_rows)
# collected_items = {
#     'Christmas decorations': 0,
#     'Gifts': 0,
#     'Cookies': 0,
# }
# found_all = False
# possible_positions = (
#     ('up', -1, 0),
#     ('down', 1, 0),
#     ('left', 0, -1),
#     ('right', 0, 1)
# )
# command = input()
# while command != "End":
#     operation, steps = [int(x) if x.isdigit() else x for x in command.split("-")]
#     santa_row, santa_col = movement(santa_row, santa_col, operation, steps)
#     if check_collected_items():
#         found_all = True
#         break
#     command = input()
# matrix[santa_row][santa_col] = "Y"
# if found_all:
#     print("Merry Christmas!")
# print("You've collected:")
# for key, value in collected_items.items():
#     print(f"- {value} {key}")
# [print(*matrix[row]) for row in range(matrix_rows)]
