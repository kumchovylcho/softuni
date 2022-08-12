charge_of_money = float(input())
coins_left = round(charge_of_money * 100)
number_of_coins = 0
while coins_left > 0:
    if coins_left >= 200:
        coins_left -= 200
    elif coins_left >= 100:
        coins_left -= 100
    elif coins_left >= 50:
        coins_left -= 50
    elif coins_left >= 20:
        coins_left -= 20
    elif coins_left >= 10:
        coins_left -= 10
    elif coins_left >= 5:
        coins_left -= 5
    elif coins_left >= 2:
        coins_left -= 2
    elif coins_left >= 1:
        coins_left -= 1
    number_of_coins += 1
print(number_of_coins)
