values = [float(number) for number in input().split()]
count_numbers = {}
for number in values:
    count_numbers[number] = count_numbers.get(number, 0) + 1
for key, values in count_numbers.items():
    print(f"{key} - {values} times")