def valid_index(row: int, col: int) -> bool:
    return 0 <= row < rows and 0 <= col < cols


VALID_NUM_ARGS = 4
VALID_SWAP_COMMAND = "swap"
STOP_PROGRAM_COMMAND = "END"
INVALID_INPUT_MSG = "Invalid input!"
DISPLAY_RESULT_SEPARATOR = " "

rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

command = input()
while command != STOP_PROGRAM_COMMAND:
    operation, *rows_and_cols = [int(x) if x.isdigit() else x for x in command.split()]

    valid_input = True

    if operation != VALID_SWAP_COMMAND:
        valid_input = False
    elif len(rows_and_cols) != VALID_NUM_ARGS:
        valid_input = False
    elif any(not valid_index(rows_and_cols[i], rows_and_cols[i + 1])
             for i in range(0, len(rows_and_cols), VALID_NUM_ARGS // 2)):
        valid_input = False

    if not valid_input:
        command = input()
        print(INVALID_INPUT_MSG)
        continue

    row_one, col_one, row_two, col_two = rows_and_cols
    matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]

    for row in range(len(matrix)):
        print(DISPLAY_RESULT_SEPARATOR.join(matrix[row]))

    command = input()



#########################################################################


# def swap(row_one, col_one, row_two, col_two):
#     matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
#     for row in range(len(matrix)):
#         print(' '.join(matrix[row]))
#
#
# rows, cols = [int(x) for x in input().split()]
# matrix = [[x for x in input().split()] for _ in range(rows)]
# command = input()
# while command != "END":
#     operation, *data = [int(x) if x.isdigit() else x for x in command.split()]
#     if operation != "swap" or len(data) != 4 or any([True for x in data if x < 0 or x > len(matrix)]):
#         print("Invalid input!")
#     elif operation == "swap":
#         swap(*data)
#     command = input()
