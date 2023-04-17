symbol_n = int(input())
symbol_l = int(input())


for one in range(1, symbol_n + 1):
    for two in range(1, symbol_n + 1):
        for f_letter in range(97, 97 + symbol_l):
            for s_letter in range(97, 97 + symbol_l):
                for digit in range(1, symbol_n + 1):
                    if digit <= one or digit <= two:
                        continue

                    result = f"{one}{two}{chr(f_letter)}{chr(s_letter)}{digit}"
                    print(result, end=" ")