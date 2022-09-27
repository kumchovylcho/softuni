text = input()
for symbol in range(len(text)):
    if text[symbol] != ":":
        continue
    print(text[symbol] + text[symbol + 1])