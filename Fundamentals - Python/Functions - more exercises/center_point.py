from math import floor

x1 = floor(float(input()))
x2 = floor(float(input()))
y1 = floor(float(input()))
y2 = floor(float(input()))

sum_x = floor(abs(x1) + abs(x2))
sum_y = floor(abs(y1) + abs(y2))


def center_point(arg1, arg2):
    if arg1 <= arg2:
        return f"({x1}, {x2})"
    elif arg2 <= arg1:
        return f"({y1}, {y2})"


print(center_point(sum_x, sum_y))
