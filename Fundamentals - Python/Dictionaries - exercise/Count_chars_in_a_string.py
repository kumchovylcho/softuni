letters_info = dict()

text = input().replace(" ", "")

for letter in text:
    if letter not in letters_info:
        letters_info[letter] = 1

    elif letter in letters_info:
        letters_info[letter] += 1

for keys in letters_info:
    print(f"{keys} -> {letters_info[keys]}")


# words = input().replace(" ", "")
#
# character_counter = dict()
#
# for letter in words:
#     if letter not in character_counter:
#         character_counter[letter] = 1
#     elif letter in character_counter:
#         character_counter[letter] += 1
#
# [print(f"{letter} -> {character_counter[letter]}") for letter in character_counter]
