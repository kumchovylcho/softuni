from string import ascii_lowercase, ascii_uppercase
letter_lowercase = ascii_lowercase
letter_uppercase = ascii_uppercase
c = 0
o = 0
n = 0
hidden_word = ""
word = ""
letters = input()
while letters != "End":
    if letters in letter_lowercase + letter_uppercase:
        if letters == "c":
            c += 1
            if c > 1:
                word += letters
        elif letters == "o":
            o += 1
            if o > 1:
                word += letters
        elif letters == "n":
            n += 1
            if n > 1:
                word += letters
        else:
            word += letters
    if c >= 1 and o >= 1 and n >= 1:
        c = 0
        o = 0
        n = 0
        hidden_word += word + " "
        word = ""
    letters = input()
if letters == "End":
    print(hidden_word)
