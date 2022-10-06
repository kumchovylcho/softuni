import re
pattern = re.compile(r'\d+')

string = input()
while len(string):
    matches = pattern.finditer(string)
    for match in matches:
        print(match[0], end=' ')
    string = input()