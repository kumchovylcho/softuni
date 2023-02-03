symbols = ["-", ",", ".", "!", "?"]


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()


def show_result(text):
    for row in range(0, len(text), 2):
        for symbol in symbols:
            text[row] = text[row].replace(symbol, "@")

        print(*text[row].split()[::-1], sep=" ")


data = read_file('text.txt')
show_result(data)