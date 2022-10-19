def swap(index_1, index_2, current_list):
    current_list[index_1], current_list[index_2] = current_list[index_2], current_list[index_1]
    return current_list


def multiply(index_1, index_2, current_list):
    current_list[index_1] = current_list[index_1] * current_list[index_2]
    return current_list


def decrease(current_list):
    current_list = [number - 1 for number in current_list]
    return current_list


numbers = [int(number) for number in input().split()]
command = input()
while command != "end":
    operation, *indexes = [item if item.isalpha() else int(item) for item in command.split()]
    if operation == "swap":
        numbers = swap(indexes[0], indexes[1], numbers)
    elif operation == "multiply":
        numbers = multiply(indexes[0], indexes[1], numbers)
    elif operation == "decrease":
        numbers = decrease(numbers)
    command = input()

print(*numbers, sep=", ")
