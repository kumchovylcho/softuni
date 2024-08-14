rows = int(input())

middle = rows // 2 - 1 if rows % 2 == 0 else rows // 2

forward_slash_amount = "/" * ((rows * 2) - 2)
inbetween_empty_space = " " * rows
inbetween_amount_symbols = "|" * rows
top_and_bottom_stars_amount = rows * 2
top_and_bottom_stars = "*" * top_and_bottom_stars_amount

top_and_bottom_pattern = f"{top_and_bottom_stars}{inbetween_empty_space}{top_and_bottom_stars}"


for i in range(rows):
    if i == 0 or i == rows - 1:
        print(top_and_bottom_pattern)
        continue

    print(f"*{forward_slash_amount}*"
          f"{inbetween_amount_symbols if i == middle else inbetween_empty_space}*"
          f"{forward_slash_amount}*"
          )


########################################################################


# rows = int(input())
#
# middle = rows // 2 if rows % 2 == 0 else rows // 2 + 1
#
# forward_slash = "/" * ((rows * 2) - 2)
#
#
# print(f"{'*' * (rows * 2)}{' ' * rows}{'*' * (rows * 2)}")
# for i in range(2, rows):
#     inbetween_symbols = " " * rows
#
#     if i == middle:
#         inbetween_symbols = "|" * rows
#
#     print(f"*{forward_slash}*{inbetween_symbols}*{forward_slash}*")
#
#
# print(f"{'*' * (rows * 2)}{' ' * rows}{'*' * (rows * 2)}")

