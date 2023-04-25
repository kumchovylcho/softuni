max_stars = int(input())

for i in range(1, max_stars + 1):
    print(f"{' ' * (max_stars - i)}{'* ' * i}{' ' * (max_stars - i)}")

for i in range(max_stars - 1, 0, -1):
    print(f"{' ' * (max_stars - i)}{'* ' * i}{' ' * (max_stars - i)}")