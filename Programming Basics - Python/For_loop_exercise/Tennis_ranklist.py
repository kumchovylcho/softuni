number_of_tourneys = int(input())
starter_points = int(input())
win = 0
win_counter = 0
finalist = 0
semi_finalist = 0
for tourney in range(1, number_of_tourneys + 1):
    current_stage = input()
    if current_stage == "W":
        win += 2000
        win_counter += 1
    elif current_stage == "F":
        finalist += 1200
    elif current_stage == "SF":
        semi_finalist += 720
total_points = starter_points + win + finalist + semi_finalist
average_points = (total_points - starter_points) // number_of_tourneys
won_tourneys_percentage = win_counter / number_of_tourneys * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{won_tourneys_percentage:.2f}%")
