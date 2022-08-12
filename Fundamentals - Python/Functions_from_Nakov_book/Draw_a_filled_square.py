number = int(input())


def top_and_bottom(n):
    result = n * 2
    return print(result * "-")


def body(n):
    v = "\/"
    result = (n - 1) * v
    for col in range(number - 2):
        print("-" + result + "-")


top_and_bottom(number)
body(number)
top_and_bottom(number)
