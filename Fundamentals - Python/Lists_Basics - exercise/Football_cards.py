team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
changes = input()
changes_split = changes.split(" ")
for change in changes_split:
    if change[0] == "A":
        if int(change[2:]) in team_a:
            team_a.remove(int(change[2:]))
    elif change[0] == "B":
        if int(change[2:]) in team_b:
            team_b.remove(int(change[2:]))
    if len(team_a) < 7 or len(team_b) < 7:
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if len(team_a) < 7 or len(team_b) < 7:
    print("Game was terminated")
