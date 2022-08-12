number_of_tournirs_played = int(input())
starter_points_in_ranklist = int(input())
points = starter_points_in_ranklist
W = 0
F = 0
SF = 0
for tournirs in range(number_of_tournirs_played):
    current_state_of_tournir = input().lower()
    if current_state_of_tournir == "w":
        points += 2000
        W += 1
    elif current_state_of_tournir == "f":
        points += 1200
        F += 1
    elif current_state_of_tournir == "sf":
        points += 720
        SF += 1
final_points = points
average_points = (final_points - starter_points_in_ranklist) // number_of_tournirs_played
percent_won_tournirs = (W / number_of_tournirs_played) * 100
print(f"Final points: {final_points}\nAverage points: {average_points}\n{percent_won_tournirs:.2f}%")
