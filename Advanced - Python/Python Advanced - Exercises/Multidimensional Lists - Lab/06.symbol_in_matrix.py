def search_for_symbol(symbol):
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == symbol:
                return f"({row}, {col})"
    return f"{symbol} does not occur in the matrix"


matrix_size = int(input())
matrix = [[x for x in input()] for _ in range(matrix_size)]
symbol_to_look_for = input()
print(search_for_symbol(symbol_to_look_for))


# matrix = []
# rows = int(input())
# for row in range(rows):
#     text = [input()]
#     matrix.append(text)
# symbol_to_search = input()
# is_found = False
# for row_ in range(len(matrix)):
#     for text in matrix[row_]:
#         if symbol_to_search in text:
#             print(f"({row_}, {text.index(symbol_to_search)})")
#             is_found = True
#             break
#     if is_found:
#         break
# if not is_found:
#     print(f"{symbol_to_search} does not occur in the matrix")