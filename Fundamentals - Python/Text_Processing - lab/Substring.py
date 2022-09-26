text = input()
extract_from_text = input()
while text in extract_from_text:
    extract_from_text = extract_from_text.replace(text, '')
print(extract_from_text)