text = input()
result = ''
current_combination = ''

for character in range(len(text)):
    if character + 1 < len(text) and text[character].isdigit() and text[character + 1].isdigit():
        current_combination = current_combination * int(text[character:character + 2])
        result += current_combination
        current_combination = ''
    elif text[character].isdigit():
        current_combination = current_combination * int(text[character])
        result += current_combination
        current_combination = ''
    else:
        current_combination += text[character]

result = result.upper()
print(f"Unique symbols used: {len(set(result))}")
print(result)


# text = input()
# result = ''
# current_combination = ''
#
# for character in range(len(text)):
#     if character + 1 < len(text) and text[character].isdigit() and text[character + 1].isdigit():
#         current_combination = current_combination * int(text[character:character + 2])
#         result += current_combination
#         current_combination = ''
#     elif text[character].isdigit():
#         current_combination = current_combination * int(text[character])
#         result += current_combination
#         current_combination = ''
#     else:
#         current_combination += text[character]
#
# result = result.upper()
# letter_checker = ''
# for letter in result:
#     if letter not in letter_checker:        # if letter in letter checker:
#       letter_checker += letter              #    continue
#                                             # letter_checker += letter
#
# print(f"Unique symbols used: {len(letter_checker)}")
# print(result)

