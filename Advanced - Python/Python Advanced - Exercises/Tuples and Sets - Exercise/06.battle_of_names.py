number_of_names = int(input())
even_sum = set()
odd_sum = set()
for row in range(1, number_of_names + 1):
    name = input()
    result = sum(ord(letter) for letter in name) // row
    if result % 2 == 0:
        even_sum.add(result)
    elif result % 2 != 0:
        odd_sum.add(result)
if sum(even_sum) == sum(odd_sum):
    print(*odd_sum.union(even_sum), sep=', ')
elif sum(odd_sum) > sum(even_sum):
    print(*odd_sum.difference(even_sum), sep=', ')
elif sum(even_sum) > sum(odd_sum):
    print(*odd_sum.symmetric_difference(even_sum), sep=', ')