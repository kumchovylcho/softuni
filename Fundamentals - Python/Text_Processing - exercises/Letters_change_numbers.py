from string import ascii_lowercase
text = input().split()
total_sum = 0
alphabet = " " + ascii_lowercase

for string in text:
    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])
    if string[0].isupper():
        total_sum += number / alphabet.index(first_letter.lower())
    elif string[0].islower():
        total_sum += number * alphabet.index(first_letter)

    if string[-1].isupper():
        total_sum -= alphabet.index(last_letter.lower())
    elif string[-1].islower():
        total_sum += alphabet.index(last_letter)

print(f"{total_sum:.2f}")

