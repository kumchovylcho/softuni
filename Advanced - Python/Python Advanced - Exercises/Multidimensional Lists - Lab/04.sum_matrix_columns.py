rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
for col in range(cols):
    sum_of_column = 0
    for row in range(rows):
        sum_of_column += matrix[row][col]
    print(sum_of_column)


# rows, columns = [int(x) for x in input().split(", ")]
# matrix = []
# for row in range(rows):
#     numbers = [int(number) for number in input().split()]
#     matrix.append(numbers)
# for column in zip(*matrix):
#     print(sum(column))
