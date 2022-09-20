word = input()
if word[-1] == "y":
    word = word[:-1] + "ies"
elif word[-1] == "o" or \
        word[-1] == "s" or \
        word[-1] == "x" or \
        word[-1] == "z" or \
        word[-2:] == "ch" or \
        word[-2:] == "sh":
    word += "es"
else:
    word += "s"
print(word)
