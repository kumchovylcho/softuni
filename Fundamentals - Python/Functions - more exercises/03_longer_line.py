from math import floor


def get_closest_point(x: float, y: float, x2: float, y2: float) -> tuple[float, float]:
    first_point = abs(x) + abs(y)
    second_point = abs(x2) + abs(y2)
    if first_point <= second_point:
        return x, y

    return x2, y2


def longer_line(x1: float,
                y1: float,
                x2: float,
                y2: float,
                x3: float,
                y3: float,
                x4: float,
                y4: float
                ) -> str:
    lines = [
        ((x1, y1), (x2, y2), abs(x1) + abs(x2) + abs(y1) + abs(y2)),
        ((x3, y3), (x4, y4), abs(x3) + abs(x4) + abs(y3) + abs(y4))
    ]

    # -lines.index(line), so it selects the first line if they are equal
    # it works like sorting. If the sum of the lines are equal, then get the first line
    (start, end, _) = max(lines, key=lambda line: (line[2], -lines.index(line)))
    start_x, start_y = get_closest_point(*start, *end)
    # get the end point compared to the start(closest)
    end_x, end_y = end if (start_x, start_y) == start else start

    return f"({start_x}, {start_y})({end_x}, {end_y})"


result = longer_line(*[floor(float(input())) for _ in range(8)])
print(result)


#####################################################################################


# import math
#
# x1, x2, y1, y2 = math.floor(float(input())), math.floor(float(input())), math.floor(float(input())), math.floor(
#     float(input()))
# z1, z2, v1, v2 = math.floor(float(input())), math.floor(float(input())), math.floor(float(input())), math.floor(
#     float(input()))
#
# sum_x = math.floor(abs(x1) + abs(x2))
# sum_y = math.floor(abs(y1) + abs(y2))
# sum_z = math.floor(abs(z1) + abs(z2))
# sum_v = math.floor(abs(v1) + abs(v2))
#
#
# def whats_closer(arg1, arg2, arg3, arg4):
#     one = arg1 + arg2
#     two = arg3 + arg4
#     if one > two:
#         if abs(x1) + abs(x2) > abs(y1) + abs(y2):
#             return f"({y1}, {y2})({x1}, {x2})"
#         else:
#             return f"({x1}, {x2})({y1}, {y2})"
#     elif one < two:
#         if abs(z1) + abs(z2) > abs(v1) + abs(v2):
#             return f"({v1}, {v2})({z1}, {z2})"
#         else:
#             return f"({z1}, {z2})({v1}, {v2})"
#     else:
#         if abs(z1) + abs(z2) > abs(v1) + abs(v2):
#             return f"({v1}, {v2})({z1}, {z2})"
#         else:
#             return f"({z1}, {z2})({v1}, {v2})"
#
#
# print(whats_closer(sum_x, sum_y, sum_z, sum_v))