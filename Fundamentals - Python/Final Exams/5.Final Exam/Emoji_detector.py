import re
text = input()
pattern = re.compile(r'(:{2}|\*{2})(?P<word>[A-Z][a-z]{2,})\1')
matches = list(pattern.finditer(text))
threshold = 1
for character in text:
    if character.isdigit():
        threshold *= int(character)
print(f"Cool threshold: {threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for match in matches:
    sum_of_ascii_letters = sum([ord(letter) for letter in match['word']])
    if sum_of_ascii_letters >= threshold:
        print(match[0])
