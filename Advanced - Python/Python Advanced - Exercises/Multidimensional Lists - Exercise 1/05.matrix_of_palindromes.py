from string import ascii_lowercase
rows, cols = [int(x) for x in input().split()]
alphabet = list(ascii_lowercase)
for row in range(rows):
    for col in range(cols):
        result = f"{alphabet[row]}{alphabet[row + col]}{alphabet[row]}"
        print(result, end=' ')
    print()
