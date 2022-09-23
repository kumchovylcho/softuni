n_number, k_number = int(input()), int(input())
lst = [1]

for _ in range(n_number - 1):
    if len(lst) < k_number:
        lst.append(sum(lst))
    elif len(lst) >= k_number:
        index = len(lst) - k_number
        lst.append(sum(lst[index:k_number + index]))

print(*lst)
