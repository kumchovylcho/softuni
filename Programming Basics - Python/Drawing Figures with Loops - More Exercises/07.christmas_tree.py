rows = int(input())

print(f"{' ' * (rows + 1)}|{' ' * (rows + 1)}")

for i in range(rows - 1, -1, -1):
    print(f"{' ' * i}{'*' * (rows - i)}", end=" | ")

    for j in range(i , i + 1):
        print(f"{'*' * (rows - i)}{' ' * i}")