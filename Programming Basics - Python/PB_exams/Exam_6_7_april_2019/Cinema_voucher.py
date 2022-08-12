price_of_voucher = int(input())
price_of_voucher_left = price_of_voucher
number_of_products = 0
number_of_tickets = 0
product = input()
while product != "End":
    if len(product) > 8:
        price_of_voucher_left -= ord(product[0]) + ord(product[1])
        if price_of_voucher_left < 0:
            break
        number_of_tickets += 1
    elif len(product) <= 8:
        price_of_voucher_left -= ord(product[0])
        if price_of_voucher_left < 0:
            break
        number_of_products += 1
    product = input()
print(f"{number_of_tickets}\n{number_of_products}")
