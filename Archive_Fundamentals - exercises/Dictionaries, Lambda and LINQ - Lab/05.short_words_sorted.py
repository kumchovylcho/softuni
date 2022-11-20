import re
text = input().lower()
pattern = re.compile(r'\b[A-Za-z\d\-#]+')
matches = re.findall(pattern, text)
short_words = []
for match in matches:
    if len(match) < 5:
        if match not in short_words:
            short_words.append(match)
print(', '.join(sorted(short_words)))