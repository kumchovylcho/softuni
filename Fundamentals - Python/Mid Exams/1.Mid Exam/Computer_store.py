total_price_without_taxes = 0
all_taxes = 0
part_prices = input()
while part_prices != "special" and part_prices != "regular":
    part_prices = float(part_prices)
    if part_prices < 0:
        print("Invalid price!")
        part_prices = input()
        continue
    total_price_without_taxes += part_prices
    all_taxes += part_prices * 0.2
    part_prices = input()

total_price = total_price_without_taxes + all_taxes
if part_prices == "special":
    total_price *= 0.9

if total_price == 0:
    print("Invalid order!")

elif total_price:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {all_taxes:.2f}$\n-----------")
    print(f"Total price: {total_price:.2f}$")

