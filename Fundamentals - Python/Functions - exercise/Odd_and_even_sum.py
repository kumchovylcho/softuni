number = input()


def odd_and_even(digit):
    even = 0
    odd = 0
    for num in digit:
        num = int(num)
        if num % 2 == 0:
            even += num
        elif num % 2 != 0:
            odd += num
    return f"Odd sum = {odd}, Even sum = {even}"


print(odd_and_even(number))
