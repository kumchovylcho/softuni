number = int(input())
n = 1
lst = []
while number > 0:
    electron = 2*n**2
    lst.append(min(number, electron))
    number -= lst[-1]
    n += 1

print(lst)


# electrons = int(input())
# list_with_filled_shells = []
#
# for electron in range(1, electrons + 1):
#     result = 2 * (electron ** 2)
#     if result > electrons:
#         list_with_filled_shells.append(electrons)
#         electrons -= electrons
#         break
#     electrons -= result
#     list_with_filled_shells.append(result)
#     if electrons <= 0:
#         break
#
# print(list_with_filled_shells)