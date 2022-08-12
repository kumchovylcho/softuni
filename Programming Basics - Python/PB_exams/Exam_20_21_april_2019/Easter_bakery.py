price_of_flour_per_kg = float(input())
kgs_of_flour = float(input())
kgs_of_sugar = float(input())
cartons_with_eggs = int(input())
packages_with_yeast = int(input())
price_of_sugar_per_kg = price_of_flour_per_kg * 0.75
price_of_carton_eggs = price_of_flour_per_kg * 1.10
price_of_yeast = price_of_sugar_per_kg * 0.20
total = (price_of_flour_per_kg * kgs_of_flour) + (price_of_sugar_per_kg * kgs_of_sugar) + (price_of_carton_eggs * cartons_with_eggs) + (price_of_yeast * packages_with_yeast)
print(f"{total:.2f}")
