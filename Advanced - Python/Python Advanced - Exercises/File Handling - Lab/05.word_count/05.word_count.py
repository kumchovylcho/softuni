def count_words_in_file(words_file, input_text_file):
    count_words = {}

    with open(words_file, "r") as words:
        with open(input_text_file, "r") as input_text:

            all_words = words.readlines()[0].split()
            for word in input_text:
                word = word.replace("-", "").replace(".", "").replace("!", "").replace("?", "").replace(",", "").split()
                for current_word in word:
                    current_word = current_word.lower()
                    if current_word in all_words:
                        count_words[current_word] = count_words.get(current_word, 0) + 1

    return dict(sorted(count_words.items(), key=lambda x: -x[1]))


def save_result_on_new_file(words: dict):
    with open('result.txt', 'w') as res:
        for key, value in words.items():
            res.write(f"{key} - {value}\n")


result = count_words_in_file('words.txt', 'input.txt')
save_result_on_new_file(result)