symbols_counter = {}
text = input()
for letter in text:
    symbols_counter[letter] = symbols_counter.get(letter, 0) + 1
for key, value in sorted(symbols_counter.items()):
    print(f"{key}: {value} time/s")