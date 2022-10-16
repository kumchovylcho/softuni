numbers = input().split(", ")

positive = [num for num in numbers if int(num) >= 0]
negative = [num for num in numbers if int(num) < 0]
even = [num for num in numbers if int(num) % 2 == 0]
odd = [num for num in numbers if int(num) % 2 != 0]


print(f"Positive:", ', '.join(positive))
print(f"Negative:", ', '.join(negative))
print(f"Even:", ', '.join(even))
print(f"Odd:", ', '.join(odd))

