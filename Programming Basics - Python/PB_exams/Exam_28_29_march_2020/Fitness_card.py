owned_money = float(input())
gender = input()
age = int(input())
sport = input()
total = 0
gym = {"men": {
    "Gym": 42,
    "Boxing": 41,
    "Yoga": 45,
    "Zumba": 34,
    "Dances": 51,
    "Pilates": 39},
    "women": {
        "Gym": 35,
        "Boxing": 37,
        "Yoga": 42,
        "Zumba": 31,
        "Dances": 53,
        "Pilates": 37}
       }
if age <= 19:
    if "m" in gender:
        discount = gym["men"][sport] - gym["men"][sport] * 0.2
        if owned_money >= discount:
            total = f"You purchased a 1 month pass for {sport}."
        else:
            money_needed = discount - owned_money
            total = f"You don't have enough money! You need ${money_needed:.2f} more."
    if "f" in gender:
        discount = gym["women"][sport] - gym["women"][sport] * 0.2
        if owned_money >= discount:
            total = f"You purchased a 1 month pass for {sport}."
        else:
            money_needed = discount - owned_money
            total = f"You don't have enough money! You need ${money_needed:.2f} more."
elif "m" in gender:
    if owned_money >= gym["men"][sport]:
        total = f"You purchased a 1 month pass for {sport}."
    else:
        money_needed = gym["men"][sport] - owned_money
        total = f"You don't have enough money! You need ${money_needed:.2f} more."
elif "f" in gender:
    if owned_money >= gym["women"][sport]:
        total = f"You purchased a 1 month pass for {sport}."
    else:
        money_needed = gym["women"][sport] - owned_money
        total = f"You don't have enough money! You need ${money_needed:.2f} more."
print(total)