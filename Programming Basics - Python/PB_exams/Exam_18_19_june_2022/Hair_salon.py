money_earned = 0
purpose_of_the_day = int(input())
enough_money = False
type_of_haircut = input()
while type_of_haircut != "closed":
    if type_of_haircut == "haircut":
        type_of_person = input()
        if type_of_person == "mens":
            money_earned += 15
        elif type_of_person == "ladies":
            money_earned += 20
        elif type_of_person == "kids":
            money_earned += 10
    elif type_of_haircut == "color":
        coloring = input()
        if coloring == "touch up":
            money_earned += 20
        elif coloring == "full color":
            money_earned += 30
    if money_earned >= purpose_of_the_day:
        enough_money = True
        break
    type_of_haircut = input()

if enough_money:
    print(f"You have reached your target for the day!")
elif not enough_money:
    diff = abs(purpose_of_the_day - money_earned)
    print(f"Target not reached! You need {diff}lv. more.")
print(f"Earned money: {money_earned}lv.")
