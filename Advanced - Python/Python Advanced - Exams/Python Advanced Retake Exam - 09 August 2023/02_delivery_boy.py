def valid_index(row: int, col: int, max_rows: int, max_cols: int) -> bool:
    return 0 <= row < max_rows and 0 <= col < max_cols


rows, cols = [int(x) for x in input().split()]

start_row, start_col = 0, 0
boy_static_row, boy_static_col = 0, 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []
for row in range(rows):
    current_row = list(input())

    if "B" in current_row:
        col = current_row.index("B")

        start_row, start_col = row, col
        boy_static_row, boy_static_col = row, col

    matrix.append(current_row)

is_out_of_field = False
is_delivered = False
while not is_delivered:
    command = input()

    try_row = start_row + directions[command][0]
    try_col = start_col + directions[command][1]

    if not valid_index(try_row,
                       try_col,
                       rows,
                       cols):
        is_out_of_field = True
        break

    if matrix[try_row][try_col] == "*":
        continue

    start_row = try_row
    start_col = try_col

    if matrix[start_row][start_col] == "P":
        matrix[start_row][start_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif matrix[start_row][start_col] == "A":
        matrix[start_row][start_col] = "P"
        is_delivered = True

    elif matrix[start_row][start_col] == "-":
        matrix[start_row][start_col] = "."


if is_out_of_field:
    matrix[boy_static_row][boy_static_col] = " "
    print("The delivery is late. Order is canceled.")

elif is_delivered:
    print("Pizza is delivered on time! Next order...")

for row in range(len(matrix)):
    print("".join(matrix[row]))
