rows = int(input())

print(f"+ {'- ' * (rows - 2)}+")

for _ in range(rows - 2):
    print(f"| {'- ' * (rows - 2)}|")

print(f"+ {'- ' * (rows - 2)}+")