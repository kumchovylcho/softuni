numbers = input().split()
how_many_to_remove = int(input())
int_numbers = []
for number in numbers:
    int_numbers.append(int(number))
for remove in range(how_many_to_remove):
    numbers.remove(min(numbers))
print(*numbers, sep=", ")
