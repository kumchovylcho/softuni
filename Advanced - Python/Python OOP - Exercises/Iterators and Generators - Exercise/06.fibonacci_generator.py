def fibonacci():
    numbers = [0, 1, 1]
    for digit in numbers:
        yield digit
    while True:
        number = numbers[-1] + numbers[-2]
        yield number
        numbers.append(number)
