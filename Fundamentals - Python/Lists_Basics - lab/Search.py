number_of_lines = int(input())
key_word = input()
all_strings = []
for text in range(number_of_lines):
    current_text = input()
    all_strings.append(current_text)
print(all_strings)
for word in range(len(all_strings) - 1, -1, -1):
    string = all_strings[word]
    if key_word not in string:
        all_strings.remove(string)
print(all_strings)
