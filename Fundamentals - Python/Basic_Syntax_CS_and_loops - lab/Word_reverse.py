word = input()
reversed_word = ""
for letters in range(len(word) - 1, -1, - 1):
    reversed_word += word[letters]
print(reversed_word)
