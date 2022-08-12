version = input().split(".")


def next_version(current_version):
    first_digit = int(current_version[0])
    second_digit = int(current_version[1])
    third_digit = int(current_version[2])

    if third_digit == 9:
        third_digit = 0
        if second_digit == 9:
            second_digit = 0
            first_digit += 1
            if first_digit > 9:
                first_digit = 0
        elif second_digit < 9:
            second_digit += 1

    elif third_digit < 9:
        third_digit += 1

    return print(f"{first_digit}.{second_digit}.{third_digit}")


next_version(version)
