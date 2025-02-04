def get_even_or_odd_elements(sequence: list[int], even_odd: str) -> list[int]:
    remainder = 0
    if even_odd == "odd":
        remainder = 1

    return [x for x in sequence if x % 2 == remainder]


def exchange(sequence: list[int], index: int) -> list[int]:
    if not 0 <= index < len(sequence):
        print("Invalid index")
        return sequence

    return sequence[index + 1:] + sequence[:index + 1]


def get_index(sequence: list[int], even_odd: str, get_max=True) -> list[int]:
    filtered_by_type = get_even_or_odd_elements(sequence, even_odd)

    if not filtered_by_type:
        print("No matches")
        return sequence

    number = max(filtered_by_type) if get_max else min(filtered_by_type)
    # get the rightmost index
    for i in range(len(sequence) - 1, -1, -1):
        if sequence[i] == number:
            print(i)
            break

    return sequence


def get_count(sequence: list[int], count: int, even_odd: str, first=True) -> list[int]:
    if count > len(sequence):
        print("Invalid count")
        return sequence

    get_slice = slice(0, count) if first else slice(-count, None)
    print(get_even_or_odd_elements(sequence, even_odd)[get_slice])

    return sequence


def main(sequence: list[int]) -> list[int]:
    command = input()
    while command != "end":
        operation, *info = [x if x.isalpha() else int(x) for x in command.split()]

        if operation == "exchange":
            sequence = exchange(sequence, *info)
        elif operation == "first" or operation == "last":
            sequence = get_count(sequence, *info, first=operation == "first")
        elif operation == "max" or operation == "min":
            sequence = get_index(sequence, *info, get_max=operation == "max")

        command = input()

    return sequence


numbers = [int(x) for x in input().split()]
print(main(numbers))



########################################################################



# def valid_index(sequence: list, index: int):
#     return 0 <= index < len(sequence)
#
#
# def invalid_count(sequence: list, count: int):
#     return count > len(sequence)
#
#
# def get_even_or_odd_elements(sequence: list, type: str):
#     if type == "odd":
#         return [x for x in sequence if x % 2 == 1]
#
#     return [x for x in sequence if x % 2 == 0]
#
#
# def exchange(sequence: list, index: int):
#     if not valid_index(sequence, index):
#         print("Invalid index")
#         return sequence
#
#     return sequence[index + 1:] + sequence[:index + 1]
#
#
# def max_index(sequence: list, even_odd: str):
#     max_num = get_even_or_odd_elements(sequence, even_odd)
#
#     if max_num:
#         number = max(max_num)
#         print(len(sequence) - sequence[::-1].index(number) - 1)
#
#     else:
#         print("No matches")
#
#     return sequence
#
# def min_index(sequence: list, even_odd: str):
#     min_num = get_even_or_odd_elements(sequence, even_odd)
#
#     if min_num:
#         number = min(min_num)
#         print(len(sequence) - sequence[::-1].index(number) - 1)
#
#     else:
#         print("No matches")
#
#     return sequence
#
#
# def first_count(sequence: list, count: int, even_odd: str):
#     if invalid_count(sequence, count):
#         print("Invalid count")
#         return sequence
#
#     print(get_even_or_odd_elements(sequence, even_odd)[:count])
#
#     return sequence
#
#
# def last_count(sequence: list, count: int, even_odd: str):
#     if invalid_count(sequence, count):
#         print("Invalid count")
#         return sequence
#
#     print(get_even_or_odd_elements(sequence, even_odd)[-count:])
#
#     return sequence
#
#
# def main(sequence: list, commands: dict):
#     command = input()
#     while command != "end":
#         operation, *info = [x if x.isalpha() else int(x) for x in command.split()]
#
#         sequence = commands[operation](sequence, *info)
#
#         command = input()
#
#     return sequence
#
#
#
# numbers = [int(x) for x in input().split()]
#
# operations = {
#     "exchange": exchange,
#     "max": max_index,
#     "min": min_index,
#     "first": first_count,
#     "last": last_count,
# }
#
#
# print(main(numbers,
#            operations
#            ))



################################################################################################


# numbers = [int(number) for number in input().split()]
#
#
# def exchange(index):
#     global numbers
#     if 0 <= index < len(numbers):
#         numbers = numbers[index + 1:] + numbers[:index + 1]
#     else:
#         print("Invalid index")
#
#
# def min_max(min_max, even_odd):
#     global even, odd
#     if min_max == "max":
#         if even_odd == "even" and even:
#             print((len(numbers) - numbers[::-1].index(max(even)) - 1))
#         elif even_odd == "odd" and odd:
#             print((len(numbers) - numbers[::-1].index(max(odd)) - 1))
#         else:
#             print("No matches")
#     elif min_max == "min":
#         if even_odd == "even" and even:
#             print((len(numbers) - numbers[::-1].index(min(even)) - 1))
#         elif even_odd == "odd" and odd:
#             print((len(numbers) - numbers[::-1].index(min(odd)) - 1))
#         else:
#             print("No matches")
#
#
# def first_last_numbers(first_last, count_of_numbers, even_odd):
#     global even, odd
#     if 0 <= count_of_numbers <= len(numbers):
#         if first_last == "first" and even_odd == "even":
#             print(even[:count_of_numbers])
#         elif first_last == "first" and even_odd == "odd":
#             print(odd[:count_of_numbers])
#         elif first_last == "last" and even_odd == "even":
#             print(even[-count_of_numbers:])
#         elif first_last == "last" and even_odd == "odd":
#             print(odd[-count_of_numbers:])
#     else:
#         print("Invalid count")
#
#
# command = input()
# while command != "end":
#     even = [number for number in numbers if number % 2 == 0]
#     odd = [number for number in numbers if number % 2 != 0]
#     command = command.split()
#     command_type = command[0]
#     if command_type == "exchange":
#         index = int(command[1])
#         exchange(index)
#     elif command_type == "max" or command_type == "min":
#         min_max(command[0], command[1])
#     elif command_type == "first" or command_type == "last":
#         first_last_numbers(command[0], int(command[1]), command[2])
#     command = input()
#
# print(numbers)