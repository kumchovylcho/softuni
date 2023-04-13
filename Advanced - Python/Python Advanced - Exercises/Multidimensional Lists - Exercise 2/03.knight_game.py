def knight_interaction(row, col):
    directions = (
        (-1, -2),  # up left
        (-2, -1),  # up left
        (-2, 1),  # up right
        (-1, 2),  # up right
        (1, 2),  # down right
        (2, 1),  # down right
        (1, -2),  # down left
        (2, -1),  # down left
    )
    interactions = 0
    for check_row, check_col in directions:
        move_row, move_col = row + check_row, col + check_col
        if check_valid_index(move_row, move_col):
            if matrix[move_row][move_col] == "K":
                interactions += 1
    return interactions


def find_knights(field: list, interactions: dict, removed_knights=0):
    for pos, value in interactions.items():
        row, col = [int(x) for x in pos.split()]

        horse_interactions = knight_interaction(row, col)

        if horse_interactions:
            interactions[f"{row} {col}"] = horse_interactions


    interactions = reset_knights_with_positive_hits(
        remove_knight_with_most_interactions(interactions)
    )

    if not interactions:
        return removed_knights

    return find_knights(field, interactions, removed_knights + 1)


def check_valid_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def remove_knight_with_most_interactions(current_knights: dict):
    biggest_interactions = max(current_knights.values()) if current_knights else 0

    for position in current_knights:
        if current_knights[position] == biggest_interactions:
            del_row, del_col = [int(x) for x in position.split()]
            matrix[del_row][del_col] = "0"

            current_knights.pop(position)
            break

    return current_knights


def reset_knights_with_positive_hits(current_knights: dict):
    while 0 in current_knights.values():
        for pos, hits in current_knights.items():
            if hits == 0:
                current_knights.pop(pos)
                break

    return {pos: 0 for pos, hits in current_knights.items() if hits > 0}


matrix_size = int(input())
matrix = []

all_horses = {}

for row in range(matrix_size):
    matrix.append(list(input()))

    for col in range(matrix_size):
        if matrix[row][col] == "K":
            all_horses[f"{row} {col}"] = all_horses.get(f"{row} {col}", 0)


print(find_knights(matrix, all_horses))




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
