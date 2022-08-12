first_number = float(input())
second_number = float(input())


def power(a, b):
    result = a ** b
    if result % 1 == 0:
        return int(result)
    else:
        return result


print(power(first_number, second_number))