number = int(input())
counter = 1
for row in range(number + 1):
    for column in range(1, row + 1):
        if counter > number:
            break
        print(f"{counter}", end=" ")
        counter += 1
    print()
    if counter > number:
        break
