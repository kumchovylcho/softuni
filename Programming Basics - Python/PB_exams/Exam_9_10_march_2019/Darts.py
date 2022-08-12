points = 301
old_points = points
unsuccessful_shots = 0
successful_shots = 0
name_of_the_player = input()
hit_spot = input()
while hit_spot != "Retire":
    old_points = points
    points_given = int(input())
    if hit_spot == "Single":
        points -= points_given
    elif hit_spot == "Double":
        points -= points_given * 2
    elif hit_spot == "Triple":
        points -= points_given * 3
    if points < 0:
        points = old_points
        hit_spot = input()
        unsuccessful_shots += 1
        continue
    successful_shots += 1
    if points == 0:
        break
    hit_spot = input()
if points == 0:
    print(f"{name_of_the_player} won the leg with {successful_shots} shots.")
else:
    print(f"{name_of_the_player} retired after {unsuccessful_shots} unsuccessful shots.")
