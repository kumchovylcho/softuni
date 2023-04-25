rows = int(input())

upper_part = rows // 2 + 1 if rows % 2 != 0 else rows // 2
lower_part = rows - upper_part


first_row_stars = 2 if rows % 2 == 0 else 1

print(f"{'-' * ((rows - first_row_stars) // 2)}{'*' * first_row_stars}{'-' * ((rows - first_row_stars) // 2)}")

for _ in range(upper_part - 1):
    first_row_stars += 2

    if first_row_stars > rows:
        first_row_stars = rows

    print(f"{'-' * ((rows - first_row_stars) // 2)}{'*' * first_row_stars}{'-' * ((rows - first_row_stars) // 2)}")


for _ in range(lower_part):
    print(f"|{'*' * (rows - 2)}|")