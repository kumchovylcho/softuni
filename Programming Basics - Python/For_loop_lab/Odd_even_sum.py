numbers = int(input())
counter = 0
even = 0
odd = 0
for number in range(1, numbers + 1):
    current_number = int(input())
    counter += 1
    if counter % 2 == 0:
        even += current_number
    else:
        odd += current_number
if even == odd:
    print(f"Yes\nSum = {even}")
else:
    diff = abs(even - odd)
    print(f"No\nDiff = {diff}")
