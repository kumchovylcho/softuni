from sys import maxsize


def check_valid_index(c_row: int, c_col: int):
    if c_row + 1 < ROWS and c_col + 1 < COLS:
        return True
    return False


def add_square_numbers(collection: list, current_sum: int):
    max_square[current_sum] = max_square.get(current_sum, collection)


def get_current_sum_of_square(collection: list):
    return sum(collection)


def get_square_list(c_row: int, c_col: int):
    numbers = []

    for row in range(c_row, c_row + 2):
        for col in range(c_col, c_col + 2):
            current_number = matrix[row][col]

            numbers.append(current_number)

    return numbers


def show_result(collection: dict):
    if not collection:
        return

    biggest_number = max(collection)

    numbers = collection[biggest_number]

    first_half = ' '.join(str(n) for n in numbers[:2])
    second_half = ' '.join(str(n) for n in numbers[2:])

    for partition in (first_half, second_half):
        print(partition)

    print(biggest_number)




ROWS, COLS = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(', ')] for _ in range(ROWS)]

biggest_sum = -maxsize

max_square = {}


for row in range(ROWS):
    for col in range(COLS):
        if not check_valid_index(row, col):
            break

        list_of_numbers = get_square_list(row, col)
        current_square_sum = get_current_sum_of_square(list_of_numbers)

        if current_square_sum > biggest_sum:
            add_square_numbers(list_of_numbers, current_square_sum)
            biggest_sum = current_square_sum

show_result(max_square)





# from sys import maxsize
#
#
# def check_index(row, col):
#     if 0 <= row + 2 <= start_row and 0 <= col + 2 <= start_col:
#         return True
#
#
# def check_square(row, col):
#     current_numbers = []
#     for check_row in range(row, row + 2):
#         for check_col in range(col, col + 2):
#             current_numbers.append(matrix[check_row][check_col])
#     if sum(current_numbers) > best_square['sum']:
#         best_square['sum'] = sum(current_numbers)
#         best_square['numbers'] = current_numbers
#
#
# start_row, start_col = [int(x) for x in input().split(", ")]
# matrix = [[int(col) for col in input().split(", ")] for row in range(start_row)]
# best_square = {
#     'sum': -maxsize,
#     'numbers': []
# }
# for row in range(start_row):
#     for col in range(start_col):
#         if check_index(row, col):
#             check_square(row, col)
# print(*best_square['numbers'][:2], sep=' ')
# print(*best_square['numbers'][2:], sep=' ')
# print(best_square['sum'])
