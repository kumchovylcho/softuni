price_for_kg_vegetables = float(input())
price_for_kg_fruits = float(input())
total_kgs_of_vegetables = int(input())
total_kg_of_fruits = int(input())
price_for_vegetables = price_for_kg_vegetables * total_kgs_of_vegetables
price_for_fruits = price_for_kg_fruits * total_kg_of_fruits
total_price = (price_for_vegetables + price_for_fruits) / 1.94
print(total_price)
