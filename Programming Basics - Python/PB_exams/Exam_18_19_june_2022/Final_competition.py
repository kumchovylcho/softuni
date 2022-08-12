number_of_dancers = int(input())
points_from_jury = float(input())
season = input()
location = input()
money_earned = 0
if location == "Bulgaria":
    money_earned = points_from_jury * number_of_dancers
    if season == "summer":
        money_earned *= 0.95
    else:
        money_earned *= 0.92
else:
    money_earned = (points_from_jury * number_of_dancers) * 1.5
    if season == "summer":
        money_earned *= 0.90
    else:
        money_earned *= 0.85
money_earned_after_charity = money_earned * 0.25
money_given_to_charity = money_earned - money_earned_after_charity
money_for_dancers = (money_earned - money_given_to_charity) / number_of_dancers
print(f"Charity - {money_given_to_charity:.2f}")
print(f"Money per dancer - {money_for_dancers:.2f}")
