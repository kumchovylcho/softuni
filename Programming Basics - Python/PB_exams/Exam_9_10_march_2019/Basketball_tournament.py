team_desi = 0
team_desi_wins = 0
team_desi_loses = 0
team_2 = 0
matches_counter = 0
name_of_tournament = input()
while name_of_tournament != "End of tournaments":
    number_of_matches = int(input())
    for match in range(1, number_of_matches + 1):
        team_desi = 0
        team_2 = 0
        team_one = int(input())
        team_two = int(input())
        if team_one > team_two:
            team_desi += team_one
            team_desi_wins += 1
            diff = abs(team_desi - team_two)
            print(f"Game {match} of tournament {name_of_tournament}: win with {diff} points.")
        elif team_two > team_one:
            team_desi_loses += 1
            team_2 += team_two
            diff = abs(team_2 - team_one)
            print(f"Game {match} of tournament {name_of_tournament}: lost with {diff} points.")
        matches_counter += 1
    name_of_tournament = input()
matches_won = team_desi_wins / matches_counter * 100
matches_lost = team_desi_loses / matches_counter * 100
print(f"{matches_won:.2f}% matches win")
print(f"{matches_lost:.2f}% matches lost")
