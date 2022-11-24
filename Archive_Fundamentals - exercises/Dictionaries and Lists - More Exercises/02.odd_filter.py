numbers = [int(x) for x in input().split()]
numbers = [number for number in numbers if number % 2 == 0]
average = sum(numbers) / len(numbers)
for number in range(len(numbers)):
    if numbers[number] > average:
        numbers[number] += 1
    elif numbers[number] < average:
        numbers[number] -= 1
print(' '.join(str(x) for x in numbers))