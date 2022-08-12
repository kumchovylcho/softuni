numbers = [int(number) for number in input().split()]


def swap(index_1, index_2):
    numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]


def multiply(index_1, index_2):
    numbers[index_1] = numbers[index_1] * numbers[index_2]


def decrease(lst):
    lst = [number - 1 for number in numbers]
    return lst


command = input()
while command != "end":
    command = command.split()
    operation = command[0]
    if operation == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        swap(index_1, index_2)
    elif operation == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        multiply(index_1, index_2)

    elif operation == "decrease":
        numbers = decrease(numbers)
    command = input()

print(*numbers, sep=", ")
