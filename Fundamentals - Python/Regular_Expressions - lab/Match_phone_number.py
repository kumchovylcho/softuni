import re
phone_numbers = input()
# pattern = r'\+359[ ]2[ ][0-9]{3}[ ][0-9]{4}\b|\+359[-]2[-][0-9]{3}[-][0-9]{4}\b'
pattern = r"\+359([ -])2\1([0-9]{3})\1([0-9]{4})\b"

matches = re.finditer(pattern, phone_numbers)
results = []
for match in matches:
    results.append(match[0])
print(*results, sep=', ')