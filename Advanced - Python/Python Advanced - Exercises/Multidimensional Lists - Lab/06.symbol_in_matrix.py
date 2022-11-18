matrix = []
rows = int(input())
for row in range(rows):
    text = [input()]
    matrix.append(text)
symbol_to_search = input()
is_found = False
for row_ in range(len(matrix)):
    for text in matrix[row_]:
        if symbol_to_search in text:
            print(f"({row_}, {text.index(symbol_to_search)})")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f"{symbol_to_search} does not occur in the matrix")