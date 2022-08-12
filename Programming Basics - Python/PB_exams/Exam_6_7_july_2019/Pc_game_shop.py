hearthstone = 0
fortnite = 0
overwatch = 0
others = 0
number_of_sold_games = int(input())
for sold_games in range(1, number_of_sold_games + 1):
    name_of_the_game = input()
    if name_of_the_game == "Hearthstone":
        hearthstone += 1
    elif name_of_the_game == "Fornite":
        fortnite += 1
    elif name_of_the_game == "Overwatch":
        overwatch += 1
    else:
        others += 1
all_games = hearthstone + fortnite + overwatch + others
percent_hearthstone = hearthstone / all_games * 100
percent_fortnite = fortnite / all_games * 100
percent_overwatch = overwatch / all_games * 100
percent_other_games = others / all_games * 100
print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fortnite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_other_games:.2f}%")
