count_of_synonyms = int(input())
synonyms = dict()

for item in range(count_of_synonyms):
    word, synonym = input(), input()

    synonyms[word] = synonyms.get(word, [])
    synonyms[word].append(synonym)

[print(f"{word} - {', '.join(synonyms[word])}") for word in synonyms]


# count_of_synonyms = int(input())
# synonyms = dict()
#
# for item in range(count_of_synonyms):
#     word = input()
#     synonym = input()
#
#     # if word not in synonyms:
#     #     synonyms[word] = shuffled_cards()
#     #
#     # synonyms[word].append(synonym)
#
# for word in synonyms:
#     print(f"{word} - {', '.join(synonyms[word])}")
