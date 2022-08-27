count_of_synonyms = int(input())
synonyms = dict()

for item in range(count_of_synonyms):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = list()

    synonyms[word].append(synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
