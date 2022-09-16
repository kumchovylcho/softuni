word = input()
while word != "End":
    if word == "SoftUni":
        word = input()
        continue
    [print(letter * 2, end='') for letter in word]
    print()
    word = input()


# new_word = ""
# word = input()
# while word != "End":
#     if word == "SoftUni":
#         word = input()
#         continue
#     for letter in range(len(word)):
#         new_word += word[letter] * 2
#     print(new_word)
#     new_word = ""
#     word = input()
