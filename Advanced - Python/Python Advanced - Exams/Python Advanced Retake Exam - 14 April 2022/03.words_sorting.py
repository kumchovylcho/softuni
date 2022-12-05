def words_sorting(*args):
    all_words = {}
    for word in args:
        all_words[word] = all_words.get(word, sum([ord(letter) for letter in word]))
    output = ""
    if sum(all_words.values()) % 2 != 0:
        for key, value in sorted(all_words.items(), key=lambda x: (-x[1])):
            output += f"{key} - {value}\n"
    else:
        for key, value in sorted(all_words.items(), key=lambda x: (x[0])):
            output += f"{key} - {value}\n"
    return output
