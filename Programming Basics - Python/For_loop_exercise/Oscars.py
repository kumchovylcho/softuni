name_of_actor = input()
points_from_academy = float(input())
points = points_from_academy
number_of_judges = int(input())
for judges in range(1, number_of_judges + 1):
    name_of_judge = input()
    points_from_judge = float(input())
    points += (len(name_of_judge) * points_from_judge) / 2
    if points > 1250.5:
        break
if points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {points:.1f}!")
else:
    diff = abs(points - 1250.5)
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")
