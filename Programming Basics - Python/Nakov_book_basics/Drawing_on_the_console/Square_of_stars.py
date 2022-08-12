stars = int(input())
for row in range(stars):
    print("*", end="")
    for col in range(1, stars):
        print(" *", end="")
    print()