import re

input_line = input()
title_pattern = r'<title>(.+)<\/title>'
match_title = re.search(title_pattern, input_line)
content_pattern = r'>([^<>]*)<?'
match_content = re.findall(content_pattern, input_line)
content = ''

for part in match_content:
    if part != match_title.group(1):
        part = part.replace('\\n', '')
        content += part.strip() + ' '

print(f"Title: {match_title.group(1)}")
print(f'Content: {content.strip()}')
content = content.strip()
