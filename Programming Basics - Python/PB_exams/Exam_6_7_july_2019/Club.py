wanted_money_to_reach = float(input())
current_money = 0
name_of_cocktail = input()
while name_of_cocktail != "Party!":
    number_of_cocktails = int(input())
    price = len(name_of_cocktail) * number_of_cocktails
    if price % 2 != 0:
        price *= 0.75
    current_money += price
    if current_money >= wanted_money_to_reach:
        print("Target acquired.")
        break
    name_of_cocktail = input()
if name_of_cocktail == "Party!":
    diff = abs(current_money - wanted_money_to_reach)
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {current_money:.2f} leva.")
