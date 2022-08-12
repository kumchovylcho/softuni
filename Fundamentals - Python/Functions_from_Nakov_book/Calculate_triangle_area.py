side_a = float(input())
side_b = float(input())


def triangle_area(a, b):
    result = a * b / 2
    if result % 1 == 0:
        return int(result)
    else:
        return result


print(triangle_area(side_a, side_b))
