import re
text = input()
pattern = re.compile(r'([@|#])(?P<first>[A-Za-z]{3,})\1{2}(?P<second>[A-Za-z]{3,})\1')
matches = pattern.finditer(text)
mirror_words = {
    "mirror words": [],
    "invalid pairs": []
}
for match in matches:
    first_word = match['first']
    second_word = match['second']
    if second_word[::-1] == first_word and first_word[::-1] == second_word:
        mirror_words['mirror words'].append(f"{first_word} <=> {second_word}")
    else:
        mirror_words['invalid pairs'].append(f"{first_word} <=> {second_word}")
if not mirror_words['mirror words'] and not mirror_words['invalid pairs']:
    print(f"No word pairs found!")
if mirror_words['mirror words'] or mirror_words['invalid pairs']:
    valid_pairs = len(mirror_words['mirror words'] + mirror_words['invalid pairs'])
    print(f"{valid_pairs} word pairs found!")
if not mirror_words['mirror words']:
    print("No mirror words!")
if mirror_words['mirror words']:
    print("The mirror words are:")
    print(', '.join(mirror_words['mirror words']))
