words = input().replace(" ", "")

character_counter = dict()

for letter in words:
    if letter not in character_counter:
        character_counter[letter] = 1
    elif letter in character_counter:
        character_counter[letter] += 1

[print(f"{letter} -> {character_counter[letter]}") for letter in character_counter]