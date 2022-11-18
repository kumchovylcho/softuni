matrix = []
matrix_size = int(input())
for row in range(matrix_size):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)
result = 0
for index, col in enumerate(zip(*matrix)):
    result += col[index]
print(result)