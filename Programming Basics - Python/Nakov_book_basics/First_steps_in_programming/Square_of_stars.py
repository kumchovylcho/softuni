number_of_stars = int(input())
col = number_of_stars - 2
print("*" * number_of_stars)
for column in range(number_of_stars - 2):
    print("*", end="")
    print(" " * col, end="")
    print("*")
print("*" * number_of_stars)

