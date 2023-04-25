rows = int(input())

middle = rows // 2 if rows % 2 == 0 else rows // 2 + 1

forward_slash = "/" * ((rows * 2) - 2)


print(f"{'*' * (rows * 2)}{' ' * rows}{'*' * (rows * 2)}")
for i in range(2, rows):
    inbetween_symbols = " " * rows

    if i == middle:
        inbetween_symbols = "|" * rows

    print(f"*{forward_slash}*{inbetween_symbols}*{forward_slash}*")


print(f"{'*' * (rows * 2)}{' ' * rows}{'*' * (rows * 2)}")

