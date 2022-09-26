digits = ''
letters = ''
symbols = ''
text = input()
for letter in text:
    if letter.isalpha():
        letters += letter
    elif letter.isdigit():
        digits += letter
    else:
        symbols += letter
print(f"{digits}\n{letters}\n{symbols}")