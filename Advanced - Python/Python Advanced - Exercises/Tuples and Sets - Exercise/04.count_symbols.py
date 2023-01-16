class Symbols:

    def __init__(self, text: str):
        self.text = text
        self.count_symbols = {}

    def read_string(self):
        for symbol in self.text:
            self.add_symbol(symbol)

    def add_symbol(self, letter: str):
        self.count_symbols[letter] = self.count_symbols.get(letter, 0) + 1

    def __repr__(self):
        result = []
        for symbol, occurrence in sorted(self.count_symbols.items()):
            result.append(f"{symbol}: {occurrence} time/s")
        return '\n'.join(result)


symbols = Symbols(input())
symbols.read_string()
print(symbols)


# symbols_counter = {}
# text = input()
# for letter in text:
#     symbols_counter[letter] = symbols_counter.get(letter, 0) + 1
# for key, value in sorted(symbols_counter.items()):
#     print(f"{key}: {value} time/s")