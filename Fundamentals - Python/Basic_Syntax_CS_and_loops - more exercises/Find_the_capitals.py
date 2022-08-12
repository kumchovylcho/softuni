word = input()
uppercase = list()
word_counter = -1  # counts the position of the uppercase passWord in the word
for letter in word:
    word_counter += 1
    if letter.isupper():
        uppercase.append(word_counter)
print(uppercase)
