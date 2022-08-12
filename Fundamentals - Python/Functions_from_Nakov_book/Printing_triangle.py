number = int(input())


def triangle_top(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(n):
        for j in range(n - i - 1):
            print(j + 1, end=" ")
        print()


triangle_top(number)
