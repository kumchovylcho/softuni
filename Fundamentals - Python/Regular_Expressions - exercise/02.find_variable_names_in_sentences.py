import re
text = input()
pattern = re.compile(r'\b_(?P<valid>[A-Za-z\d]+\b)')
matches = pattern.finditer(text)
result = [match['valid'] for match in matches]
print(*result, sep=',')


# import re
# print(','.join([match['valid'] for match in re.compile(r'\b_(?P<valid>[A-Za-z\d]+\b)').finditer(input())]))
