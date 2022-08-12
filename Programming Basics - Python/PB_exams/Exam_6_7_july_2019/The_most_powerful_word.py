from math import floor
vowel_letters = "A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Y", "y"
points = 0
current_points = 0
most_powerful_word = ""
word = input()
while word != "End of words":
    current_points = 0
    for letter in word:
        current_points += ord(letter)
    if word[0] in vowel_letters:
        current_points *= len(word)
    else:
        current_points = floor(current_points / len(word))
    if current_points > points:
        most_powerful_word = word
        points = current_points
    word = input()
print(f"The most powerful word is {most_powerful_word} - {points}")
