from collections import deque
vowels = deque(input().split())
consonants = deque(input().split())
find_flowers = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}
found_flower = False
while vowels and consonants and not found_flower:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    for key, flower in find_flowers.items():
        if current_vowel in flower:
            find_flowers[key] = find_flowers[key].replace(current_vowel, "")
        if current_consonant in flower:
            find_flowers[key] = find_flowers[key].replace(current_consonant, "")
        if not find_flowers[key]:
            word_found = key
            found_flower = True
            break
if found_flower:
    print(f"Word found: {word_found}")
elif not found_flower:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
