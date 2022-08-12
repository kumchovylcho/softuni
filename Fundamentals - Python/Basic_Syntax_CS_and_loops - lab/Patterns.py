number_of_max_stars = int(input())
for star in range(1, number_of_max_stars + 1):
    for star_backwards in range(0, star):
        print("*", end="")
    print()
for star in range(number_of_max_stars - 1, 0, -1):
    for star_backwards in range(0, star):
        print("*", end="")
    print()
