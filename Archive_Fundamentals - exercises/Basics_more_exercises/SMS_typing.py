from string import ascii_lowercase
count_of_characters = int(input())

message = ''
for character in range(count_of_characters):
    letter = input()
    if len(letter) == 1:
        if letter == '2':
            message += 'a'
        elif letter == '3':
            message += 'd'
        elif letter == '4':
            message += 'g'
        elif letter == '5':
            message += 'j'
        elif letter == '6':
            message += 'm'
        elif letter == '7':
            message += 'p'
        elif letter == '8':
            message += 't'
        elif letter == '9':
            message += 'w'
        elif letter == '0':
            message += ' '
    elif len(letter) > 1:
        main_digit = letter[0]
        off_set = (int(main_digit) - 2) * 3
        if int(main_digit) == 9 or int(main_digit) == 8:
            off_set += 1
        letter_index = off_set + len(letter) - 1
        message += ascii_lowercase[letter_index]
print(message)