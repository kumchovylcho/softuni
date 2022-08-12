lost_fights = int(input())
price_of_helmet = float(input())
price_of_sword = float(input())
price_of_shield = float(input())
price_of_armor = float(input())
money_spent = 0
shield_breaker_count = 0
for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        money_spent += price_of_helmet
    if fight % 3 == 0:
        money_spent += price_of_sword
    if fight % 2 == 0 and fight % 3 == 0:
        money_spent += price_of_shield
        shield_breaker_count += 1
        if shield_breaker_count % 2 == 0:
            money_spent += price_of_armor
print(f"Gladiator expenses: {money_spent:.2f} aureus")
