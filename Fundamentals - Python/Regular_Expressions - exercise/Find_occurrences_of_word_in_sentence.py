import re
text = input().lower()
word_to_check = input().lower()
pattern = re.compile(r'\b' + word_to_check + r'\b')
matches = pattern.finditer(text)
result = [match for match in matches]
print(len(result))
