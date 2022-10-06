import re
numbers = input()
pattern = re.compile(r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))')
matches = pattern.finditer(numbers)
for match in matches:
    print(match[0], end=' ')