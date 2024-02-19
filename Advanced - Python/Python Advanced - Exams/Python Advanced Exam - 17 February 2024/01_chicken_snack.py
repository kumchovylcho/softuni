from collections import deque

amount_of_money = [int(x) for x in input().split()]
food_prices = deque([int(x) for x in input().split()])

bought_food = 0

while amount_of_money and food_prices:
    money = amount_of_money.pop()
    food_price = food_prices.popleft()

    if money >= food_price:
        bought_food += 1
        change = money - food_price
        if amount_of_money:
            amount_of_money[-1] += change

if bought_food >= 4:
    print(f"Gluttony of the day! Henry ate {bought_food} foods.")
elif 1 < bought_food < 4:
    print(f"Henry ate: {bought_food} foods.")
elif bought_food == 1:
    print(f"Henry ate: {bought_food} food.")
elif not bought_food:
    print("Henry remained hungry. He will try next weekend again.")