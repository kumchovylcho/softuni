numbers = int(input())
for number in range(numbers):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f"{current_number} is odd!")
        break
else:
    print("All all_numbers are even.")

# if the for loop breaks , then the else statement will NOT be executed
# for loop must iterate until the very end without breaking and that's when else statement will be executed
