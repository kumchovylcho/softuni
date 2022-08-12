number = int(input())


def check(digit):
    if digit < 0:
        return f"The number {digit} is negative."
    elif digit > 0:
        return f"The number {digit} is positive."
    else:
        return f"The number {digit} is zero."


print(check(number))