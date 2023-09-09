string = input()

digits = []
symbols = []
for letter in string:
    if letter.isdigit():
        digits.append(int(letter))
        continue

    symbols.append(letter)

take_digits = digits[::2]
skip_digits = digits[1::2]

result = []
for take, skip in zip(take_digits, skip_digits):
    result += symbols[:take]

    symbols = symbols[take + skip:]

print("".join(result))