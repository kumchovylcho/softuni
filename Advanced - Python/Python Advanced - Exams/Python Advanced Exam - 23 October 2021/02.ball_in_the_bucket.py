def check_valid_index(current_row, current_col):
    if 0 <= current_row < matrix_size and 0 <= current_col < matrix_size:
        return True


def sum_of_colon(current_row, current_col, collected_points):
    if matrix[current_row][current_col] == "B":
        matrix[current_row][current_col] = "hit"
        for row in range(matrix_size):
            if matrix[row][current_col] != "hit":
                collected_points += matrix[row][current_col]
    return collected_points


def try_create_item(current_points):
    items = {
        'Football': {'lower': 100, 'upper': 199, 'won': False},
        'Teddy Bear': {'lower': 200, 'upper': 299, 'won': False},
        'Lego Construction Set': {'lower': 300, 'upper': 450, 'won': False}
    }
    for item, value in items.items():
        if value['lower'] <= current_points <= value['upper']:
            items[item]['won'] = True  # not needed line of code
            return item


matrix_size = 6
total_sum = 0
matrix = [[int(col) if col[-1].isdigit() else col for col in input().split()] for row in range(matrix_size)]
for _ in range(3):
    current_position = input().split(", ")
    row, col = int(current_position[0].strip("(")), int(current_position[-1].strip(")"))
    if check_valid_index(row, col):
        total_sum += sum_of_colon(row, col, 0)
created_item = try_create_item(total_sum)
if created_item:
    print(f"Good job! You scored {total_sum} points, and you've won {created_item}.")
elif not created_item:
    print(f"Sorry! You need {100 - total_sum} points more to win a prize.")
