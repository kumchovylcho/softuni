number = int(input())
for column in range(1, number + 1):
    for row in range(column):
        print(column, end=" ")
    print()

