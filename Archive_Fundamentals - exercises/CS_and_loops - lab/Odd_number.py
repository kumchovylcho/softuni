number = int(input())
while number % 2 == 0:
    print("Please write an odd number.")
    number = int(input())
print(f"The number is: {abs(number)}")