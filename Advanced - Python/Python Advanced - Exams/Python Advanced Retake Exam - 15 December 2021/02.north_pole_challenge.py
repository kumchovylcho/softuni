def find_santa(rows):
    for row in range(rows):
        if "Y" in matrix[row]:
            col = matrix[row].index("Y")
            matrix[row][col] = "x"
            return row, col


def check_collected_items():
    result = 0
    for row in range(matrix_rows):
        for col in range(matrix_cols):
            if matrix[row][col] != "." and matrix[row][col] != "x" and matrix[row][col] != "Y":
                result += 1
    if result == 0:
        return True
    return False


def movement(current_row, current_col, direction, moves):
    for where, row, col in possible_positions:
        if direction == where:
            for _ in range(moves):
                current_row, current_col = current_row + row, current_col + col
                if current_row == -1:
                    current_row = matrix_rows - 1
                elif current_row == matrix_rows:
                    current_row = 0
                elif current_col == -1:
                    current_col = matrix_cols - 1
                elif current_col == matrix_cols:
                    current_col = 0
                check_square(current_row, current_col)
                matrix[current_row][current_col] = "x"
                if check_collected_items():
                    return current_row, current_col
    return current_row, current_col


def check_square(row, col):
    if matrix[row][col] == "D":
        collected_items['Christmas decorations'] += 1
    elif matrix[row][col] == "G":
        collected_items['Gifts'] += 1
    elif matrix[row][col] == "C":
        collected_items['Cookies'] += 1


matrix_rows, matrix_cols = [int(x) for x in input().split(", ")]
matrix = [[col for col in input().split()] for row in range(matrix_rows)]
santa_row, santa_col = find_santa(matrix_rows)
collected_items = {
    'Christmas decorations': 0,
    'Gifts': 0,
    'Cookies': 0,
}
found_all = False
possible_positions = (
    ('up', -1, 0),
    ('down', 1, 0),
    ('left', 0, -1),
    ('right', 0, 1)
)
command = input()
while command != "End":
    operation, steps = [int(x) if x.isdigit() else x for x in command.split("-")]
    santa_row, santa_col = movement(santa_row, santa_col, operation, steps)
    if check_collected_items():
        found_all = True
        break
    command = input()
matrix[santa_row][santa_col] = "Y"
if found_all:
    print("Merry Christmas!")
print("You've collected:")
for key, value in collected_items.items():
    print(f"- {value} {key}")
[print(*matrix[row]) for row in range(matrix_rows)]
