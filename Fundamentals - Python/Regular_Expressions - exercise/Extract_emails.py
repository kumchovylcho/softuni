import re
extract_email = input()
pattern = re.compile(r'(?P<email>(?<=\s)([a-z0-9]+[\\.\-_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+\b)')
matches = pattern.finditer(extract_email)
for match in matches:
    print(match['email'])