new_word = ""
word = input()
while word != "End":
    if word == "SoftUni":
        word = input()
        continue
    for letter in range(len(word)):
        new_word += word[letter] * 2
    print(new_word)
    new_word = ""
    word = input()
