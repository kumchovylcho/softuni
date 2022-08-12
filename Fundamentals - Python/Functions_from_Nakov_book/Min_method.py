digit_one = int(input())
digit_two = int(input())
digit_three = int(input())


def get_min(first, second, third):
    result = 0
    if first > second:
        result = second
    else:
        result = first
    if result > third:
        result = third
    return result


print(get_min(digit_one, digit_two, digit_three))
