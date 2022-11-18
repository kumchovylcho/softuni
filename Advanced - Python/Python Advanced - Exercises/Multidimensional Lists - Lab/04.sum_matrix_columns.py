rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for row in range(rows):
    numbers = [int(number) for number in input().split()]
    matrix.append(numbers)
for column in zip(*matrix):
    print(sum(column))
