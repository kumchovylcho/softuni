def set_check_helper(collection, length):
    if len(collection) == length and "1" in collection:
        return "First player won"

    if len(collection) == length and "2" in collection:
        return "Second player won"


def check_rows(row1, row2, row3):
    for row in (row1, row2, row3):
       if all(x == "1" for x in row):
           return "First player won"

       elif all(x == "2" for x in row):
           return "Second player won"

    return 0


def check_columns(row1, row2, row3):
    for col in range(3):
        result = set()
        for row in (row1, row2, row3):
            result.add(row[col])

        winner = set_check_helper(result, 1)
        if winner:
            return winner

    return 0


def check_diagonals(row1, row2, row3):
    rows = [row1, row2, row3]

    left_diag_checker = set()
    right_diag_checker = set()
    for i in range(3):
        right_index = (i + 1) * -1
        left_diag_checker.add(rows[i][i])
        right_diag_checker.add(rows[i][right_index])


    for result in left_diag_checker, right_diag_checker:
        winner = set_check_helper(result, 1)
        if winner:
            return winner

    return 0


def solver(row1, row2, row3):
    for result in (check_rows(row1, row2, row3),
                   check_columns(row1, row2, row3),
                   check_diagonals(row1, row2, row3)
                   ):
        if result:
            return result

    return "Draw!"


row_1 = input().split()
row_2 = input().split()
row_3 = input().split()

print(solver(row_1, row_2, row_3))




# row_1 = [int(number) for number in input().split()]
# row_2 = [int(number) for number in input().split()]
# row_3 = [int(number) for number in input().split()]
# first_player_wins = False
# second_player_wins = False
# draw = False
#
#
# def game():
#     global first_player_wins, second_player_wins, draw
#     if (row_1[0] == 1 and row_2[0] == 1 and row_3[0] == 1) or \
#         (row_1[1] == 1 and row_2[1] == 1 and row_3[1] == 1) or \
#         (row_1[2] == 1 and row_2[2] == 1 and row_3[2] == 1) or \
#         (row_1[0] == 1 and row_2[1] == 1 and row_3[2] == 1) or \
#         (row_1[2] == 1 and row_2[1] == 1 and row_3[0] == 1) or \
#         (row_1[0] == 1 and row_1[1] == 1 and row_1[2] == 1) or \
#         (row_2[0] == 1 and row_2[1] == 1 and row_2[2] == 1) or \
#         (row_3[0] == 1 and row_3[1] == 1 and row_3[2] == 1):
#         first_player_wins = True
#
#     elif (row_1[0] == 2 and row_2[0] == 2 and row_3[0] == 2) or \
#         (row_1[1] == 2 and row_2[1] == 2 and row_3[1] == 2) or \
#         (row_1[2] == 2 and row_2[2] == 2 and row_3[2] == 2) or \
#         (row_1[0] == 2 and row_2[1] == 2 and row_3[2] == 2) or \
#         (row_1[2] == 2 and row_2[1] == 2 and row_3[0] == 2) or \
#         (row_1[0] == 2 and row_1[1] == 2 and row_1[2] == 2) or \
#         (row_2[0] == 2 and row_2[1] == 2 and row_2[2] == 2) or \
#         (row_3[0] == 2 and row_3[1] == 2 and row_3[2] == 2):
#         second_player_wins = True
#
#     else:
#         draw = True
#
#     return first_player_wins, second_player_wins, draw
#
#
# game()
#
# if first_player_wins:
#     print("First player won")
# elif second_player_wins:
#     print("Second player won")
# elif draw:
#     print("Draw!")