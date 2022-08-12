budget = int(input())
money_left = budget
command = input()
while command != "End":
    product_price = int(command)
    money_left -= product_price
    if money_left < 0:
        break
    command = input()
if money_left < 0:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")
