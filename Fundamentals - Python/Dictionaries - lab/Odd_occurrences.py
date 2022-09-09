words = [word.lower() for word in input().split()]

odd_occurrences = dict()

for word in words:
    odd_occurrences[word] = odd_occurrences.get(word, 0) + 1

[print(f"{word}", end=" ") for word in odd_occurrences if odd_occurrences[word] % 2 != 0]


# words = [word.lower() for word in input().split()]
#
# odd_occurrences = dict()
#
# for word in words:
#     if word not in odd_occurrences:
#         odd_occurrences[word] = 1
#
#     elif word in odd_occurrences:
#         odd_occurrences[word] += 1
#
# for word in odd_occurrences:
#     if odd_occurrences[word] % 2 != 0:
#         print(f"{word}", end=" ")
