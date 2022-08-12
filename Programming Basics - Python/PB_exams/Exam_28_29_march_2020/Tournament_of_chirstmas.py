money_for_charity = 0
total_money = 0
all_won_games = 0
all_lost_games = 0
won_games = 0
lost_games = 0
number_of_tournaments = int(input())
for tournament in range(1, number_of_tournaments + 1):
    name_of_game = input()
    while name_of_game != "Finish":
        result_of_match = input()
        if result_of_match == "win":
            money_for_charity += 20
            won_games += 1
        else:
            lost_games += 1
        name_of_game = input()
    if won_games > lost_games:
        money_for_charity *= 1.10
    all_won_games += won_games
    all_lost_games += lost_games
    total_money += money_for_charity
    won_games = 0
    lost_games = 0
    money_for_charity = 0
if all_won_games > all_lost_games:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
