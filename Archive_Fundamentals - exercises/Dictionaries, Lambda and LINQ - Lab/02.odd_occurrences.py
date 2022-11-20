occurrences = input().lower().split()
odd_occurrences = {'odd': []}
for word in occurrences:
    if occurrences.count(word) % 2 != 0:
        if word not in odd_occurrences['odd']:
            odd_occurrences['odd'].append(word)
print(', '.join(odd_occurrences['odd']))