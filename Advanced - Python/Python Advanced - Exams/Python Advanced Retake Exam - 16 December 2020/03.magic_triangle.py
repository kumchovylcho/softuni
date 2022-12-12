def get_magic_triangle(number):
    matrix = [[1], [1, 1]]
    for row in range(number - len(matrix)):
        matrix.append([])
        result = []
        for digit in range(len(matrix[-2]) - 1):
            result.append(matrix[-2][digit] + matrix[-2][digit + 1])
        matrix[-1].append(1)
        matrix[-1] += result
        matrix[-1].append(1)
    return matrix


get_magic_triangle(10)
