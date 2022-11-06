import re

text = input()

pattern = re.compile(r'(?P<all_sum_word>(::|\*\*)(?P<clear_word>[A-Z][a-z]{2,})(\2))')
digits_pattern = re.compile(r'[0-9]+')

result_text = list(re.finditer(pattern, text))
result_digits = re.finditer(digits_pattern, text)

list_digits = [x for x in text if x.isdigit()]
threshold = 1
for multiply in list_digits:
    threshold *= int(multiply)
print(f"Cool threshold: {threshold}")
print(f"{len(result_text)} emojis found in the text. The cool ones are:")

for result_animal in result_text:
    ch_sum = 0
    for ch in result_animal['clear_word']:
        ch_sum += ord(ch)
    if ch_sum > threshold:
        print(f"{result_animal['all_sum_word']}")

#
# import re
# text = input()
# pattern = re.compile(r'(:{2}|\*{2})(?P<word>[A-Z][a-z]{2,})\1')
# matches = list(pattern.finditer(text))
# threshold = 1
# for character in text:
#     if character.isdigit():
#         threshold *= int(character)
# print(f"Cool threshold: {threshold}")
# print(f"{len(matches)} emojis found in the text. The cool ones are:")
# for match in matches:
#     sum_of_ascii_letters = sum([ord(letter) for letter in match['word']])
#     if sum_of_ascii_letters >= threshold:
#         print(match[0])
