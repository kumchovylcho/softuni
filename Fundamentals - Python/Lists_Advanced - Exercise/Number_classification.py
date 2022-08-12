numbers = input().split(", ")

positive = []
negative = []
even = []
odd = []

[positive.append(num) for num in numbers if int(num) >= 0]
[negative.append(num) for num in numbers if int(num) < 0]
[even.append(num) for num in numbers if int(num) % 2 == 0]
[odd.append(num) for num in numbers if int(num) % 2 != 0]

print(f"Positive:", end=" ")
print(*positive, sep=", ")
print(f"Negative:", end=" ")
print(*negative, sep=", ")
print(f"Even:", end=" ")
print(*even, sep=", ")
print(f"Odd:", end=" ")
print(*odd, sep=", ")
