number = float(input())
while 1 > number < 100:
    number = float(input())
else:
    print(f"The number {number} is between 1 and 100")

# if you break the loop using break , it will not enter this else statement
# if the while loop condition returns False without using break , else statement will be executed
