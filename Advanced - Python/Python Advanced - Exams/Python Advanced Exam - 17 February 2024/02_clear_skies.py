rows = int(input())
start_row, start_col = 0, 0
armor = 300
enemies = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = []
for row in range(rows):
    current_row = list(input())

    if "J" in current_row:
        start_row = row
        start_col = current_row.index("J")
        current_row[start_col] = "-"

    if "E" in current_row:
        enemies += current_row.count("E")

    matrix.append(current_row)

while enemies and armor > 0:
    command = input()

    start_row += directions[command][0]
    start_col += directions[command][1]

    if matrix[start_row][start_col] == "-":
        continue

    if matrix[start_row][start_col] == "R":
        armor = 300
        matrix[start_row][start_col] = "-"

    elif matrix[start_row][start_col] == "E":
        enemies -= 1
        matrix[start_row][start_col] = "-"

        if enemies:
            armor -= 100

if not enemies:
    print("Mission accomplished, you neutralized the aerial threat!")
elif armor <= 0:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{start_row}, {start_col}]!")

matrix[start_row][start_col] = "J"
for row in matrix:
    print("".join(row))