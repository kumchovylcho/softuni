words = input().split()
first_word = words[0]
second_word = words[1]

total_sum = 0
shorter_word = min(len(first_word), len(second_word))
longer_word = max(len(first_word), len(second_word))

longest_word = ''
if len(first_word) >= len(second_word):
    longest_word = first_word
elif len(second_word) >= len(first_word):
    longest_word = second_word

for pair in range(shorter_word):
    total_sum += ord(first_word[pair]) * ord(second_word[pair])

if first_word != second_word:
    for longer_word_letter in range(shorter_word, longer_word):
        total_sum += ord(longest_word[longer_word_letter])

print(total_sum)
