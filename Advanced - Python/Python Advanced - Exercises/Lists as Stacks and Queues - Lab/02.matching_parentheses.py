arithmetic_operation = input()
check_opening_parenthesis = []
for end_index, symbol in enumerate(arithmetic_operation):
    if symbol == "(":
        check_opening_parenthesis.append(end_index)
    elif symbol == ")":
        start_index = check_opening_parenthesis.pop()
        print(arithmetic_operation[start_index:end_index + 1])