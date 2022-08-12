budget = float(input())
price_per_kg_of_flour = float(input())
price_for_pack_of_eggs = price_per_kg_of_flour * 0.75
price_for_one_liter_milk = price_per_kg_of_flour * 1.25
breads = 0
colored_eggs = 0
while budget >= 0:
    budget -= price_per_kg_of_flour + price_for_pack_of_eggs + (price_for_one_liter_milk / 4)
    if budget < 0:
        budget += price_per_kg_of_flour + price_for_pack_of_eggs + (price_for_one_liter_milk / 4)
        break
    colored_eggs += 3
    breads += 1
    if breads % 3 == 0:
        colored_eggs -= breads - 2
print(f"You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
