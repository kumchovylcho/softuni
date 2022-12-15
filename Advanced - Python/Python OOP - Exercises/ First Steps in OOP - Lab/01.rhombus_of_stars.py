def print_row(size_of_rhombus, stars):
    for row in range(size_of_rhombus - stars):
        print(" ", end="")
    for row in range(1, stars):
        print("*", end=" ")
    print("*")


size = int(input())
for star_count in range(1, size):
    print_row(size, star_count)
for star_count in range(size, 0, -1):
    print_row(size, star_count)
