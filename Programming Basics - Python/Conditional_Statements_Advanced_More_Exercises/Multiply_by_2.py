numbers = float(input())
while numbers >= 0:
    result = numbers * 2
    print(f"Result: {result:.2f}")
    numbers = float(input())
if numbers < 0:
    print("Negative digit!")
