from collections import deque

expression = deque(int(x) if x[-1].isdigit() else x for x in input().split())
current_result = []
while expression:
    symbol = expression.popleft()
    if str(symbol) in "+-*/":
        result = current_result.pop(0)
        while current_result:
            if symbol == "+":
                result += current_result.pop(0)
            elif symbol == "-":
                result -= current_result.pop(0)
            elif symbol == "*":
                result *= current_result.pop(0)
            elif symbol == "/":
                result //= current_result.pop(0)
        current_result.insert(0, result)
        continue
    current_result.append(symbol)
print(current_result[0])


# from collections import deque
# evaluation = deque([int(digit) if digit[-1].isdigit() else digit for digit in input().split()])
# extracted_info = deque()
# while evaluation:
#     extracted_item = evaluation.popleft()
#     if extracted_item in ['*', '/', '+', '-']:
#         result = extracted_info.popleft()
#         if extracted_item == '*':
#             while extracted_info:
#                 result *= extracted_info.popleft()
#         elif extracted_item == '+':
#             while extracted_info:
#                 result += extracted_info.popleft()
#         elif extracted_item == '-':
#             while extracted_info:
#                 result -= extracted_info.popleft()
#         elif extracted_item == '/':
#             while extracted_info:
#                 result //= extracted_info.popleft()
#         extracted_info = deque([result])
#     else:
#         extracted_info.append(extracted_item)
# print(*extracted_info)