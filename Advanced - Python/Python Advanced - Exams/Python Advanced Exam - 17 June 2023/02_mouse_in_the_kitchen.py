def valid_index(row: int, col: int):
    return 0 <= row < rows and 0 <= col < cols


def check_if_cheese(row: int, col: int):
    return matrix[row][col] == "C"


def check_can_step(row: int, col: int):
    return matrix[row][col] in ["C", "*"]


def check_if_trap(row: int, col: int):
    return matrix[row][col] == "T"



rows, cols = [int(x) for x in input().split(",")]

matrix = []
m_row, m_col = 0, 0
food_left = 0
for row in range(rows):
    current_line = input()
    if "M" in current_line:
        m_row, m_col = row, current_line.index("M")
        current_line = current_line.replace("M", "*")

    food_left += current_line.count("C")
    matrix.append(list(current_line))


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

is_inside = True
is_trapped = False

command = input()
while food_left and command != "danger":
    try_row, try_col = m_row + directions[command][0], m_col + directions[command][1]

    if not valid_index(try_row, try_col):
        is_inside = False
        break

    if check_can_step(try_row, try_col):
        if check_if_cheese(try_row, try_col):
            matrix[try_row][try_col] = "*"
            food_left -= 1

        m_row, m_col = try_row, try_col

    else:
        if check_if_trap(try_row, try_col):
            m_row, m_col = try_row, try_col
            is_trapped = True
            break

    command = input()


if not is_inside:
    print("No more cheese for tonight!")

if not food_left:
    print("Happy mouse! All the cheese is eaten, good night!")

if is_trapped:
    print("Mouse is trapped!")

if command == "danger" and food_left:
    print("Mouse will come back later!")


matrix[m_row][m_col] = "M"
for row in range(rows):
    print("".join(matrix[row]))