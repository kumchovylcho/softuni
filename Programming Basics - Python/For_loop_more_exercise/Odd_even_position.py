import sys
numbers = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
for number in range(1, numbers + 1):
    current_number = float(input())
    if number % 2 == 0:
        even_sum += current_number
        if current_number > even_max:
            even_max = current_number
        if current_number < even_min:
            even_min = current_number
    else:
        odd_sum += current_number
        if current_number > odd_max:
            odd_max = current_number
        if current_number < odd_min:
            odd_min = current_number
if numbers == 1:
    print(f"OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No")
elif numbers == 0:
    print(f"OddSum={odd_sum:.2f},\nOddMin=No,\nOddMax=No,")
    print(f"EvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No")
else:
    print(f"OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},\nEvenMin={even_min:.2f},\nEvenMax={even_max:.2f}")
