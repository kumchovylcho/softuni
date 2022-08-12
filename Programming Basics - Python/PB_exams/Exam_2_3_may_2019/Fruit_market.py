price_strawberry = float(input())
kgs_of_bananas = float(input())
kgs_of_oranges = float(input())
kgs_of_raspberry = float(input())
kgs_of_strawberry = float(input())
price_raspberry = price_strawberry / 2
price_orange = price_raspberry * 0.6
price_banana = price_raspberry * 0.2
total = (price_strawberry * kgs_of_strawberry) + (price_banana * kgs_of_bananas) + (price_orange * kgs_of_oranges) + (price_raspberry * kgs_of_raspberry)
print(f"{total:.2f}")
