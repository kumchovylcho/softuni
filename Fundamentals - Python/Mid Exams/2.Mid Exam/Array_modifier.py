def swap(current_numbers, indexes):
    index_one, index_two = indexes[0], indexes[1]
    current_numbers[index_one], current_numbers[index_two] = current_numbers[index_two], current_numbers[index_one]
    return current_numbers


def multiply(current_numbers, indexes):
    index_one, index_two = indexes[0], indexes[1]
    current_numbers[index_one] = current_numbers[index_one] * current_numbers[index_two]
    return current_numbers


def decrease(current_numbers, indexes):
    # indexes parament is empty, but needs to be included in the function because of line 28
    current_numbers = [item - 1 for item in current_numbers]
    return current_numbers


list_with_numbers = list(map(int, input().split()))
list_modifier = {
    "swap": swap,
    "multiply": multiply,
    "decrease": decrease
}
command = input()
while command != "end":
    operation, *data = [item if item.isalpha() else int(item) for item in command.split()]
    list_with_numbers = list_modifier[operation](list_with_numbers, data)
    command = input()
print(', '.join(str(item) for item in list_with_numbers))



# def swap(index_1, index_2, current_list):
#     current_list[index_1], current_list[index_2] = current_list[index_2], current_list[index_1]
#     return current_list
#
#
# def multiply(index_1, index_2, current_list):
#     current_list[index_1] = current_list[index_1] * current_list[index_2]
#     return current_list
#
#
# def decrease(current_list):
#     current_list = [number - 1 for number in current_list]
#     return current_list
#
#
# numbers = [int(number) for number in input().split()]
# command = input()
# while command != "end":
#     operation, *indexes = [item if item.isalpha() else int(item) for item in command.split()]
#     if operation == "swap":
#         numbers = swap(indexes[0], indexes[1], numbers)
#     elif operation == "multiply":
#         numbers = multiply(indexes[0], indexes[1], numbers)
#     elif operation == "decrease":
#         numbers = decrease(numbers)
#     command = input()
#
# print(*numbers, sep=", ")
