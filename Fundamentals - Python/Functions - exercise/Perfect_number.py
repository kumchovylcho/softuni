def is_perfect(num):
    result = num // 2
    while result > 2:
        result //= 2
    if result == 1:
        return f"We have a perfect number!"
    elif result != 1:
        return f"It's not so perfect."


number = int(input())
result = is_perfect(number)
print(result)
