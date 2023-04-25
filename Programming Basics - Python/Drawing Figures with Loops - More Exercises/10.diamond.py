rows = int(input())

if rows in (1, 2):
    print(rows * '*')
    exit()

first_row_stars = 2 if rows % 2 == 0 else 1

upper_part = rows // 2 - 1 if rows % 2 == 0 else rows // 2
lower_part = rows - upper_part - 1 if rows % 2 == 0 else rows - upper_part

print(f"{'-' * ((rows - first_row_stars) // 2)}{'*' * first_row_stars}{'-' * ((rows - first_row_stars) // 2)}")

space_between = 1 if rows % 2 != 0 else 2
for i in range(upper_part - 1, -1, -1):

    print(f"{'-' * i}*{'-' * space_between}*{'-' * i}")
    space_between += 2

space_between = rows - 2
for i in range(1, lower_part - 1):
    space_between -= 2

    print(f"{'-' * i}*{'-' * space_between}*{'-' * i}")


print(f"{'-' * ((rows - first_row_stars) // 2)}{'*' * first_row_stars}{'-' * ((rows - first_row_stars) // 2)}")
