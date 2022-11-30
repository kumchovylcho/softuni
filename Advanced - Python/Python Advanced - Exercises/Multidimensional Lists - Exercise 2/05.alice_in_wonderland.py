def find_alice():
    for row in range(len(matrix)):
        if "A" in matrix[row]:
            col = matrix[row].index("A")
            matrix[row][col] = "*"
            return [row, col]


def check_index(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def check_obstacles(row, col):
    unwanted_symbols = ["*", ".", "R"]
    if matrix[row][col] not in unwanted_symbols:
        alice_task['collected'] += matrix[row][col]
    elif matrix[row][col] == "R":
        alice_task['out of matrix'] = True
    matrix[row][col] = "*"
    alice_task['alice'] = [row, col]


def go_up(row, col):
    check_row = row - 1
    if check_index(check_row, col):
        check_obstacles(check_row, col)
    else:
        alice_task['out of matrix'] = True


def go_down(row, col):
    check_row = row + 1
    if check_index(check_row, col):
        check_obstacles(check_row, col)
    else:
        alice_task['out of matrix'] = True


def go_right(row, col):
    check_col = col + 1
    if check_index(row, check_col):
        check_obstacles(row, check_col)
    else:
        alice_task['out of matrix'] = True


def go_left(row, col):
    check_col = col - 1
    if check_index(row, check_col):
        check_obstacles(row, check_col)
    else:
        alice_task['out of matrix'] = True


rows = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(rows)]
alice_position = find_alice()
alice_task = {
    'alice': alice_position,
    'goal': 10,
    'collected': 0,
    'out of matrix': False
}
directions = {
    'up': go_up,
    'down': go_down,
    'left': go_left,
    'right': go_right
}
while alice_task['collected'] < alice_task['goal'] and not alice_task['out of matrix']:
    command = input()
    directions[command](*alice_task['alice'])
    # if command == "up":
    #     go_up(*alice_task['alice'])
    # elif command == "down":
    #     go_down(*alice_task['alice'])
    # elif command == "left":
    #     go_left(*alice_task['alice'])
    # elif command == "right":
    #     go_right(*alice_task['alice'])
if alice_task['collected'] >= alice_task['goal'] and not alice_task['out of matrix']:
    print("She did it! She went to the party.")
elif alice_task['collected'] < alice_task['goal'] or alice_task['out of matrix']:
    print("Alice didn't make it to the tea party.")
[print(*matrix[row]) for row in range(len(matrix))]
