number_of_strings = int(input())
for words in range(1, number_of_strings + 1):
    current_word = input()
    if "," in current_word or "." in current_word or "_" in current_word:
        print(f"{current_word} is not pure!")
    else:
        print(f"{current_word} is pure.")
