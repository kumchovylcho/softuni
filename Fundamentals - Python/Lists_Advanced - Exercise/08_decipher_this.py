words = input().split()
result = []

for word in words:
    cur_word = list(word)

    char_code = []
    while cur_word[0] in "0123456789":
        char_code.append(cur_word.pop(0))

    cur_word.insert(0, chr(int("".join(char_code))))
    cur_word[1], cur_word[-1] = cur_word[-1], cur_word[1]

    result.append("".join(cur_word))

print(" ".join(result))



# coded_message = input().split()
# check_numbers = "0123456789"
#
# first_letter = ""
# rest_of_the_word = ""
#
# for word in coded_message:
#     first_letter = ""
#     rest_of_the_word = ""
#     for letter in word:
#         if letter in check_numbers:
#             first_letter += letter
#         elif letter not in check_numbers:
#             rest_of_the_word += letter
#     if len(rest_of_the_word) > 1:
#         second_letter = rest_of_the_word[-1]
#         last_letter = rest_of_the_word[0]
#         print(f"{chr(int(first_letter))}{second_letter}{rest_of_the_word[1:-1]}{last_letter}", end=" ")
#     elif len(rest_of_the_word) == 1:
#         print(f"{chr(int(first_letter))}{rest_of_the_word}", end=" ")