matrix = input().split("|")[::-1]
for row in range(len(matrix)):
    for text in matrix[row].split():
        print(text, end=' ')
