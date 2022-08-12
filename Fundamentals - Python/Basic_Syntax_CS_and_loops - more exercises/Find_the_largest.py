number = input()
largest_digit = []
for digit in number:
    digit = int(digit)
    largest_digit.append(digit)
largest_digit.sort()
print(*largest_digit[::-1], sep="")
