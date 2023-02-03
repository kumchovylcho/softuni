from string import punctuation


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()


def count_characters_and_symbols(collection: list):
    with open('result.txt', 'w') as res:

        for line, sentence in enumerate(collection, 1):
            character, symbol = 0, 0
            for letter in sentence:
                if letter.isspace():
                    continue
                if letter in punctuation:
                    symbol += 1
                elif letter.isalpha():
                    character += 1

            res.write(f"Line {line}: {sentence} ({character})({symbol})\n")


data = read_file('text.txt')
count_characters_and_symbols(data)