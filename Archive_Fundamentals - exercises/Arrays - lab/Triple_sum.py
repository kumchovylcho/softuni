numbers = [int(x) for x in input().split()]
triple_sum = True

for ind in range(len(numbers)):
    for num in numbers[ind+1:]:
        sum_ = numbers[ind] + num
        if sum_ in numbers:
            print(f"{numbers[ind]} + {num} == {sum_}")
            triple_sum = False
if triple_sum:
    print("No")