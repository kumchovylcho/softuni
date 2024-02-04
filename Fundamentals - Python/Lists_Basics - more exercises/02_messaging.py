numbers = input().split()
string = list(input())

final_message = []
while numbers:
    index = sum(int(x) for x in numbers.pop(0))
    character = string.pop(index % len(string))
    final_message.append(character)

print(''.join(final_message))




# numbers = [number for number in input().split()]
# text = list(input())
# index = 0
# final_string = ""
#
#
# def check_text(letter_position):
#     global text
#     global final_string
#     if 0 <= letter_position < len(text):
#         final_string += text[letter_position]
#         text.pop(letter_position)
#     elif letter_position >= len(text):
#         index_to_remove = index - len(text)
#         final_string += text[index_to_remove]
#         text.pop(index_to_remove)
#
#
# for number in numbers:
#     index = 0
#     for digit in number:
#         index += int(digit)
#     check_text(index)
#
# print(final_string)
