food_and_quantity = input().split()
bakery = {}

for x in range(0, len(food_and_quantity), 2):
    key = food_and_quantity[x]
    value = food_and_quantity[x + 1]
    bakery[key] = int(value)

print(bakery)
