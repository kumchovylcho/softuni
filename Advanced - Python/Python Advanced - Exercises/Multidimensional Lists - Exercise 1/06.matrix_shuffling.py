def swap(row_one, col_one, row_two, col_two):
    matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
    for row in range(len(matrix)):
        print(' '.join(matrix[row]))


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]
command = input()
while command != "END":
    operation, *data = [int(x) if x.isdigit() else x for x in command.split()]
    if operation != "swap" or len(data) != 4 or any([True for x in data if x < 0 or x > len(matrix)]):
        print("Invalid input!")
    elif operation == "swap":
        swap(*data)
    command = input()
