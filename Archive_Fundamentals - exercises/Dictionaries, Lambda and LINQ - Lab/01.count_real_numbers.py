occurrences = {}
numbers = [float(x) if '.' in x else int(x) for x in input().split()]
for number in numbers:
    occurrences[number] = occurrences.get(number, 0) + 1
for key, value in sorted(occurrences.items()):
    print(f"{key} -> {value}")