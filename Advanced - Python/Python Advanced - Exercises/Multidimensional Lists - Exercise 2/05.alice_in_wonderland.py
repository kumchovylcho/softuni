def find_alice():
    for row in range(matrix_size):
        if "A" in matrix[row]:
            col = matrix[row].index("A")
            matrix[row][col] = "*"
            return row, col


def check_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def check_current_square(row, col):
    if matrix[row][col] == "R":
        alice_info['out or trap'] = True
    elif matrix[row][col] != "." and matrix[row][col] != "*":
        alice_info['tea'] += matrix[row][col]
    matrix[row][col] = "*"


matrix_size = int(input())
matrix = [[int(col) if col.isdigit() else col for col in input().split()] for _row in range(matrix_size)]
directions = {
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0},
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1}
}
alice_info = {
    'tea': 0,
    'out or trap': False
}
current_row, current_col = find_alice()
while alice_info['tea'] < 10 and not alice_info['out or trap']:
    command = input()
    if check_index(current_row + directions[command]['row'],
                   current_col + directions[command]['col']):
        current_row, current_col = current_row + directions[command]['row'], current_col + directions[command]['col']
        check_current_square(current_row, current_col)
        continue
    alice_info['out or trap'] = True
if alice_info['out or trap']:
    print("Alice didn't make it to the tea party.")
elif not alice_info['out or trap']:
    print("She did it! She went to the party.")
[print(' '.join(str(x) for x in matrix[row])) for row in range(matrix_size)]




# def find_alice():
#     for row in range(len(matrix)):
#         if "A" in matrix[row]:
#             col = matrix[row].index("A")
#             matrix[row][col] = "*"
#             return [row, col]
#
#
# def check_index(row, col):
#     if 0 <= row < len(matrix) and 0 <= col < len(matrix):
#         return True
#     return False
#
#
# def check_obstacles(row, col):
#     unwanted_symbols = ["*", ".", "R"]
#     if matrix[row][col] not in unwanted_symbols:
#         alice_task['collected'] += matrix[row][col]
#     elif matrix[row][col] == "R":
#         alice_task['out of matrix'] = True
#     matrix[row][col] = "*"
#     alice_task['alice'] = [row, col]
#
#
# def go_up(row, col):
#     check_row = row - 1
#     if check_index(check_row, col):
#         check_obstacles(check_row, col)
#     else:
#         alice_task['out of matrix'] = True
#
#
# def go_down(row, col):
#     check_row = row + 1
#     if check_index(check_row, col):
#         check_obstacles(check_row, col)
#     else:
#         alice_task['out of matrix'] = True
#
#
# def go_right(row, col):
#     check_col = col + 1
#     if check_index(row, check_col):
#         check_obstacles(row, check_col)
#     else:
#         alice_task['out of matrix'] = True
#
#
# def go_left(row, col):
#     check_col = col - 1
#     if check_index(row, check_col):
#         check_obstacles(row, check_col)
#     else:
#         alice_task['out of matrix'] = True
#
#
# rows = int(input())
# matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(rows)]
# alice_position = find_alice()
# alice_task = {
#     'alice': alice_position,
#     'goal': 10,
#     'collected': 0,
#     'out of matrix': False
# }
# directions = {
#     'up': go_up,
#     'down': go_down,
#     'left': go_left,
#     'right': go_right
# }
# while alice_task['collected'] < alice_task['goal'] and not alice_task['out of matrix']:
#     command = input()
#     directions[command](*alice_task['alice'])
#     # if command == "up":
#     #     go_up(*alice_task['alice'])
#     # elif command == "down":
#     #     go_down(*alice_task['alice'])
#     # elif command == "left":
#     #     go_left(*alice_task['alice'])
#     # elif command == "right":
#     #     go_right(*alice_task['alice'])
# if alice_task['collected'] >= alice_task['goal'] and not alice_task['out of matrix']:
#     print("She did it! She went to the party.")
# elif alice_task['collected'] < alice_task['goal'] or alice_task['out of matrix']:
#     print("Alice didn't make it to the tea party.")
# [print(*matrix[row]) for row in range(len(matrix))]
