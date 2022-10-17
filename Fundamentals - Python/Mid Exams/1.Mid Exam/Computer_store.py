part_prices_without_tax = 0
command = input()
while command != "special" and command != "regular":
    current_part_price = float(command)
    if current_part_price < 0:
        print("Invalid price!")
        command = input()
        continue
    part_prices_without_tax += current_part_price
    command = input()
taxes = part_prices_without_tax * 0.2
total_price = part_prices_without_tax + (part_prices_without_tax * 0.2)
if not part_prices_without_tax:
    print("Invalid order!")
if command == "special":
    total_price *= 0.9
if (command == "special" or command == "regular") and part_prices_without_tax:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {part_prices_without_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$\n-----------")
    print(f"Total price: {total_price:.2f}$")


# total_price_without_taxes = 0
# all_taxes = 0
# part_prices_without_tax = input()
# while part_prices_without_tax != "special" and part_prices_without_tax != "regular":
#     part_prices_without_tax = float(part_prices_without_tax)
#     if part_prices_without_tax < 0:
#         print("Invalid price!")
#         part_prices_without_tax = input()
#         continue
#     total_price_without_taxes += part_prices_without_tax
#     all_taxes += part_prices_without_tax * 0.2
#     part_prices_without_tax = input()
#
# total_price = total_price_without_taxes + all_taxes
# if part_prices_without_tax == "special":
#     total_price *= 0.9
#
# if total_price == 0:
#     print("Invalid order!")
#
# elif total_price:
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {total_price_without_taxes:.2f}$")
#     print(f"Taxes: {all_taxes:.2f}$\n-----------")
#     print(f"Total price: {total_price:.2f}$")
#
