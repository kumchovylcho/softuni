from string import ascii_lowercase, ascii_uppercase

allowed_letters = ascii_lowercase + ascii_uppercase

secret_letters = {
    "o": 0,
    "c": 0,
    "n": 0
}

final_string = []
current_string = []

symbol = input()
while symbol != "End":

    if symbol in allowed_letters:
        if symbol in secret_letters and secret_letters[symbol] == 0:
            secret_letters[symbol] += 1

        else:
            current_string.append(symbol)
        if all(x == 1 for x in secret_letters.values()):
            final_string.append(''.join(current_string) + " ")
            current_string = []

            for key in secret_letters:
                secret_letters[key] = 0

    symbol = input()

print(''.join(final_string))


# from string import ascii_lowercase, ascii_uppercase
# letter_lowercase = ascii_lowercase
# letter_uppercase = ascii_uppercase
# c = 0
# o = 0
# n = 0
# hidden_word = ""
# word = ""
# letters = input()
# while letters != "End":
#     if letters in letter_lowercase + letter_uppercase:
#         if letters == "c":
#             c += 1
#             if c > 1:
#                 word += letters
#         elif letters == "o":
#             o += 1
#             if o > 1:
#                 word += letters
#         elif letters == "n":
#             n += 1
#             if n > 1:
#                 word += letters
#         else:
#             word += letters
#     if c >= 1 and o >= 1 and n >= 1:
#         c = 0
#         o = 0
#         n = 0
#         hidden_word += word + " "
#         word = ""
#     letters = input()
# if letters == "End":
#     print(hidden_word)
