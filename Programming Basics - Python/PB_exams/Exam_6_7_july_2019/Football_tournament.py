points = 0
wins = 0
draws = 0
loses = 0
name_of_football_team = input()
played_matches_current_season = int(input())
for game in range(1, played_matches_current_season + 1):
    result = input()
    if result == "W":
        points += 3
        wins += 1
    elif result == "D":
        points += 1
        draws += 1
    else:
        loses += 1
if played_matches_current_season == 0:
    print(f"{name_of_football_team} hasn't played any games during this season.")
else:
    print(f"{name_of_football_team} has won {points} points during this season.")
    print(f"Total stats: \n## W: {wins}\n## D: {draws}\n## L: {loses}")
    win_rate = wins / played_matches_current_season * 100
    print(f"Win rate: {win_rate:.2f}%")
