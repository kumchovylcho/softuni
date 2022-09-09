products = input().split()
bakery = dict()

for item in range(0, len(products), 2):
    bakery[products[item]] = int(products[item + 1])

print(bakery)


# products = input().split()
# bakery = dict()
#
# for item in range(0, len(products), 2):
#     product = products[item]
#     quantity = int(products[item + 1])
#     bakery[product] = quantity
#
# print(bakery)
