import operator


def math_operations(*args, **kwargs):
    operations = {
        "a": operator.add,
        "s": operator.sub,
        "d": operator.truediv,
        "m": operator.mul
    }

    kwargs_as_list = list(kwargs)
    kwargs_length = len(kwargs)

    for index in range(len(args)):
        key = kwargs_as_list[index % kwargs_length]
        number = args[index]

        if key == "d" and number == 0:
            continue

        kwargs[key] = operations[key](kwargs[key], number)

    return "\n".join(
        [
            f"{key}: {value:.1f}"
            for key, value in
            sorted(
                kwargs.items(),
                key=lambda item: (-item[1], item[0])
            )
        ]
    )



# def math_operations(*args, **kwargs):
#     for index in range(len(args)):
#         key = list(kwargs)[index % 4]
#
#         if key == "a":
#             kwargs[key] += args[index]
#         elif key == "s":
#             kwargs[key] -= args[index]
#         elif key == "d":
#             if args[index] != 0:
#                 kwargs[key] /= args[index]
#         elif key == "m":
#             kwargs[key] *= args[index]
#
#     result = []
#     for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
#         result.append(f"{key}: {value:.1f}")
#     return '\n'.join(result)


# def math_operations(*args, **kwargs):
#     counter = 1
#     for digit in args:
#         if counter == 2:
#             kwargs['s'] -= digit
#         elif counter == 3:
#             if digit != 0:
#                 kwargs['d'] /= digit
#         elif counter == 4:
#             kwargs['m'] *= digit
#         elif counter == 1:
#             kwargs['a'] += digit
#         counter += 1
#         if counter == 5:
#             counter = 1
#     result = []
#     for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
#         result.append(f"{key}: {value:.1f}")
#     return '\n'.join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
