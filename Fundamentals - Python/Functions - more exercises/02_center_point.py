from math import floor


def floor_numbers(*numbers):
    return tuple(floor(x) for x in numbers)


def closer_point(x, y, x2, y2):
    if abs(x) + abs(y) > abs(x2) + abs(y2):
        return floor_numbers(x2, y2)

    return floor_numbers(x, y)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


print(closer_point(x1, y1, x2, y2))

#############################################################################

# from math import floor
#
# x1 = floor(float(input()))
# x2 = floor(float(input()))
# y1 = floor(float(input()))
# y2 = floor(float(input()))
#
# sum_x = floor(abs(x1) + abs(x2))
# sum_y = floor(abs(y1) + abs(y2))
#
#
# def center_point(arg1, arg2):
#     if arg1 <= arg2:
#         return f"({x1}, {x2})"
#     elif arg2 <= arg1:
#         return f"({y1}, {y2})"
#
#
# print(center_point(sum_x, sum_y))
