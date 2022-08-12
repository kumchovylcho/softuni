word = input()
a = 0
e = 0
i = 0
o = 0
u = 0
for letter in word:
    if letter == "a":
        a += 1
    elif letter == "e":
        e += 2
    elif letter == "i":
        i += 3
    elif letter == "o":
        o += 4
    elif letter == "u":
        u += 5
total = a + e + i + o + u
print(total)
