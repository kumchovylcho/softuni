text = input()
letter_checker = ''
for letter in text:
    if letter != letter_checker:
        print(letter, end="")
        letter_checker = letter
