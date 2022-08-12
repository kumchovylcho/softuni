a1 = int(input())
a2 = int(input())
n = int(input())
third_symbol_limit = int(n / 2) - 1
second_symbol = 0
third_symbol = 0
for first_letter in range(a1, a2):
    first_symbol = chr(first_letter)
    fourth_symbol = first_letter
    for second_letter in range(1, n):
        second_symbol = second_letter
        for third_letter in range(1, third_symbol_limit + 1):
            third_symbol = third_letter
            if first_letter % 2 != 0 and (second_symbol + third_symbol + fourth_symbol) % 2 != 0:
                print(f"{first_symbol}-{second_symbol}{third_symbol}{fourth_symbol}")