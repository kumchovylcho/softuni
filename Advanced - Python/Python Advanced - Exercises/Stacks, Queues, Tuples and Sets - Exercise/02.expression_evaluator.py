from collections import deque
evaluation = deque([int(digit) if digit[-1].isdigit() else digit for digit in input().split()])
extracted_info = deque()
while evaluation:
    extracted_item = evaluation.popleft()
    if extracted_item in ['*', '/', '+', '-']:
        result = extracted_info.popleft()
        if extracted_item == '*':
            while extracted_info:
                result *= extracted_info.popleft()
        elif extracted_item == '+':
            while extracted_info:
                result += extracted_info.popleft()
        elif extracted_item == '-':
            while extracted_info:
                result -= extracted_info.popleft()
        elif extracted_item == '/':
            while extracted_info:
                result //= extracted_info.popleft()
        extracted_info = deque([result])
    else:
        extracted_info.append(extracted_item)
print(*extracted_info)