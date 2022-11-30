def math_operations(*args, **kwargs):
    counter = 1
    for digit in args:
        if counter == 2:
            kwargs['s'] -= digit
        elif counter == 3:
            if digit != 0:
                kwargs['d'] /= digit
        elif counter == 4:
            kwargs['m'] *= digit
        elif counter == 1:
            kwargs['a'] += digit
        counter += 1
        if counter == 5:
            counter = 1
    result = []
    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result.append(f"{key}: {value:.1f}")
    return '\n'.join(result)
