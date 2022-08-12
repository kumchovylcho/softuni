budget_for_actors = float(input())
budget_for_actors_left = budget_for_actors
name_of_actor = input()
while name_of_actor != "ACTION":
    if len(name_of_actor) > 15:
        budget_for_actors_left -= budget_for_actors_left * 0.2
    else:
        money_for_actor = float(input())
        budget_for_actors_left -= money_for_actor
    if budget_for_actors_left < 0:
        print(f"We need {abs(budget_for_actors_left):.2f} leva for our actors.")
        break
    name_of_actor = input()
else:
    print(f"We are left with {budget_for_actors_left:.2f} leva.")
