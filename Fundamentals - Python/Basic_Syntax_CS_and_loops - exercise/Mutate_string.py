first_word, second_word = list(input()), list(input())
for index in range(len(first_word)):
    if first_word[index] != second_word[index]:
        first_word[index] = second_word[index]
        print(*first_word, sep='')


# first_text = input()
# second_text = input()
# list_one = shuffled_cards(first_text)
# list_two = shuffled_cards(second_text)
# i = 0
# target_list = shuffled_cards(first_text)
# for letter_a, letter_b in zip(list_one, list_two):
#     if letter_a != letter_b:
#         target_list[i] = letter_b
#         for _ in target_list:
#             print(f"{_}", end="")
#         print()
#     i += 1