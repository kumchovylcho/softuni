start_total = 301
name = input()
count = 0

not_success = 0
current_hit = 0

scores = {
    'single': 1,
    'double': 2,
    'triple': 3
}

roll = input().lower()
while roll != 'retire':
    point = int(input())

    current_hit = scores.get(roll) * point

    if current_hit > start_total:
        not_success += 1

    else:
        start_total -= current_hit
        count += 1

    if start_total == 0:
        break

    roll = input().lower()

if start_total > 0:
    print(f"{name} retired after {not_success} unsuccessful shots.")
else:
    print(f"{name} won the leg with {count} shots.")


# points = 301
# old_points = points
# unsuccessful_shots = 0
# successful_shots = 0
# name_of_the_player = input()
# hit_spot = input()
# while hit_spot != "Retire":
#     old_points = points
#     points_given = int(input())
#     if hit_spot == "Single":
#         points -= points_given
#     elif hit_spot == "Double":
#         points -= points_given * 2
#     elif hit_spot == "Triple":
#         points -= points_given * 3
#     if points < 0:
#         points = old_points
#         hit_spot = input()
#         unsuccessful_shots += 1
#         continue
#     successful_shots += 1
#     if points == 0:
#         break
#     hit_spot = input()
# if points == 0:
#     print(f"{name_of_the_player} won the leg with {successful_shots} shots.")
# else:
#     print(f"{name_of_the_player} retired after {unsuccessful_shots} unsuccessful shots.")
