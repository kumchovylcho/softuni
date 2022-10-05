numbers = input().split()
absolute_value = []

for number in numbers:
    absolute_value.append(abs(float(number)))
print(absolute_value)


# numbers = [abs(float(number)) for number in input().split()]
# print(numbers)

