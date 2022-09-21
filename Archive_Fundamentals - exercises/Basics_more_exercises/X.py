rows = int(input())
spaces_in_x = rows - 4
empty_spaces = (rows - 2) * " "
print(f"x{empty_spaces}x")
for column in range(1, rows // 2):
    empty_spaces_before_and_after_x = column * " "
    empty_spaces_between_x = spaces_in_x * " "
    print(f"{empty_spaces_before_and_after_x}x{empty_spaces_between_x}x{empty_spaces_before_and_after_x}")
    spaces_in_x -= 2
alone_x = (rows // 2) * " "
print(f"{alone_x}x{alone_x}")
spaces_in_x = 1
for column_2 in range((rows // 2), 0, -1):
    empty_spaces_before_and_after_x = (column_2 - 1) * " "
    print(f"{empty_spaces_before_and_after_x}x{spaces_in_x * ' '}x{empty_spaces_before_and_after_x}")
    spaces_in_x += 2
