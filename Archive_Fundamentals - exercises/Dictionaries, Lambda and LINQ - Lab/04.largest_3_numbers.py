numbers = [int(x) for x in input().split()]
print(*sorted(numbers, reverse=True)[:3])