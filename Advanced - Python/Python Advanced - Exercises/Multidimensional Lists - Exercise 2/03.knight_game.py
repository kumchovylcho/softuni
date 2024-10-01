def knight_interactions(row: int,
                        col: int,
                        field: list[list[str]],
                        movements: tuple,
                        knight_symbol: str
                        ) -> int:
    interactions = 0
    for check_row, check_col in movements:
        move_row, move_col = row + check_row, col + check_col
        if not check_valid_index(move_row, move_col, field):
            continue

        if field[move_row][move_col] != knight_symbol:
            continue

        interactions += 1

    return interactions


def find_knights(field: list[list[str]], knight_symbol: str) -> dict[(int, int), int]:
    knights_positions = {}
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == knight_symbol:
                knights_positions[(row, col)] = 0
    return knights_positions


def check_valid_index(row: int, col: int, field: list[list[str]]) -> bool:
    return 0 <= row < len(field) and 0 <= col < len(field[0])


def get_knight_with_most_interactions(current_knights: dict[tuple[int, int], int]) -> tuple[int, int]:
    """
    There will always be a knight.
    """
    biggest_interactions = max(current_knights.values())
    for horse_r, horse_c in current_knights:
        if current_knights[(horse_r, horse_c)] == biggest_interactions:
            return horse_r, horse_c


def main(field: list[list[str]], movements: tuple) -> int:
    knights = find_knights(field, KNIGHT_SYMBOL)

    deleted_knights = 0
    has_interactions = True
    while has_interactions:
        for knight_r, knight_c in knights:
            interactions_amount = knight_interactions(knight_r, knight_c, field, movements, KNIGHT_SYMBOL)
            if interactions_amount:
                knights[(knight_r, knight_c)] += interactions_amount

        # knights are no more interacting
        if sum(knights.values()) == 0:
            has_interactions = False
            continue

        deleted_knights += 1
        remove_row, remove_col = get_knight_with_most_interactions(knights)
        knights.pop((remove_row, remove_col))
        matrix[remove_row][remove_col] = EMPTY_POSITION

        # resetting the interactions
        knights = {(row, col): 0 for row, col in knights}

    return deleted_knights


directions = (
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (1, -2),
    (2, -1),
)
KNIGHT_SYMBOL = "K"
EMPTY_POSITION = "0"
matrix_size = int(input())
matrix = [[x for x in input()] for _ in range(matrix_size)]

removed_knights = main(matrix, directions)
print(removed_knights)







# def knight_interaction(row, col):
#     directions = (
#         (-1, -2),  # up left
#         (-2, -1),  # up left
#         (-2, 1),  # up right
#         (-1, 2),  # up right
#         (1, 2),  # down right
#         (2, 1),  # down right
#         (1, -2),  # down left
#         (2, -1),  # down left
#     )
#     interactions = 0
#     for check_row, check_col in directions:
#         move_row, move_col = row + check_row, col + check_col
#         if check_valid_index(move_row, move_col):
#             if matrix[move_row][move_col] == "K":
#                 interactions += 1
#     return interactions
#
#
# def find_knights(field: list, interactions: dict, removed_knights=0):
#     for pos, value in interactions.items():
#         row, col = [int(x) for x in pos.split()]
#
#         horse_interactions = knight_interaction(row, col)
#
#         if horse_interactions:
#             interactions[f"{row} {col}"] = horse_interactions
#
#
#     interactions = reset_knights_with_positive_hits(
#         remove_knight_with_most_interactions(interactions)
#     )
#
#     if not interactions:
#         return removed_knights
#
#     return find_knights(field, interactions, removed_knights + 1)
#
#
# def check_valid_index(row, col):
#     if 0 <= row < matrix_size and 0 <= col < matrix_size:
#         return True
#
#
# def remove_knight_with_most_interactions(current_knights: dict):
#     biggest_interactions = max(current_knights.values()) if current_knights else 0
#
#     for position in current_knights:
#         if current_knights[position] == biggest_interactions:
#             del_row, del_col = [int(x) for x in position.split()]
#             matrix[del_row][del_col] = "0"
#
#             current_knights.pop(position)
#             break
#
#     return current_knights
#
#
# def reset_knights_with_positive_hits(current_knights: dict):
#     while 0 in current_knights.values():
#         for pos, hits in current_knights.items():
#             if hits == 0:
#                 current_knights.pop(pos)
#                 break
#
#     return {pos: 0 for pos, hits in current_knights.items() if hits > 0}
#
#
# matrix_size = int(input())
# matrix = []
#
# all_horses = {}
#
# for row in range(matrix_size):
#     matrix.append(list(input()))
#
#     for col in range(matrix_size):
#         if matrix[row][col] == "K":
#             all_horses[f"{row} {col}"] = all_horses.get(f"{row} {col}", 0)
#
#
# print(find_knights(matrix, all_horses))




# def knight_interaction(row, col):
#     directions = (
#         (-1, -2),  # up left
#         (-2, -1),  # up left
#         (-2, 1),  # up right
#         (-1, 2),  # up right
#         (1, 2),  # down right
#         (2, 1),  # down right
#         (1, -2),  # down left
#         (2, -1),  # down left
#     )
#     interactions = 0
#     for check_row, check_col in directions:
#         move_row, move_col = row + check_row, col + check_col
#         if check_valid_index(move_row, move_col):
#             if matrix[move_row][move_col] == "K":
#                 interactions += 1
#     return interactions
#
#
# def find_knights():
#     all_interactions = {}
#     for row in range(matrix_size):
#         for col in range(matrix_size):
#             if matrix[row][col] == "K":
#                 interactions = knight_interaction(row, col)
#                 if interactions:
#                     all_interactions[f"{row} {col}"] = all_interactions.get(f"{row} {col}", interactions)
#     return all_interactions
#
#
# def check_valid_index(row, col):
#     if 0 <= row < matrix_size and 0 <= col < matrix_size:
#         return True
#
#
# def remove_knight_with_most_interactions(current_knights: dict):
#     biggest_interactions = max(current_knights.values())
#     for position in current_knights:
#         if current_knights[position] == biggest_interactions:
#             del_row, del_col = [int(x) for x in position.split()]
#             matrix[del_row][del_col] = "0"
#             break
#
#
# matrix_size = int(input())
# matrix = [[x for x in input()] for _ in range(matrix_size)]
# interact_knights = True
# removed_knights = 0
# while interact_knights:
#     interacted_knights = find_knights()
#     if interacted_knights:
#         removed_knights += 1
#         remove_knight_with_most_interactions(interacted_knights)
#         continue
#     interact_knights = False
# print(removed_knights)
