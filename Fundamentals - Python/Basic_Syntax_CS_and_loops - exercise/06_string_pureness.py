iterations = int(input())

for _ in range(iterations):
    word = input()

    is_impure = len([x for x in ",._" if x in word])

    result = f"{word} is pure."
    if is_impure:
        result = f"{word} is not pure!"

    print(result)

################################################################################################

# string_rules = {
#     "banned symbols": [",", ".", "_"]
# }
#
# number_of_strings = int(input())
# for words in range(number_of_strings):
#     current_word = input()
#     for letter in current_word:
#         if letter in string_rules['banned symbols']:
#             print(f"{current_word} is not pure!")
#             break
#     else:
#         print(f"{current_word} is pure.")

################################################################################################

# number_of_strings = int(input())
# for words in range(number_of_strings):
#     current_word = input()
#     [print(f"{current_word} is not pure!") if "," in current_word or "." in current_word or "_" in current_word
#      else print(f"{current_word} is pure.") for _ in range(1)]


# number_of_strings = int(input())
# for words in range(1, number_of_strings + 1):
#     current_word = input()
#     if "," in current_word or "." in current_word or "_" in current_word:
#         print(f"{current_word} is not pure!")
#     else:
#         print(f"{current_word} is pure.")
