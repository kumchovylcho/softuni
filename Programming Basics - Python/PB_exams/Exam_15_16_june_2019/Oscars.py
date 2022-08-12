name_of_actor = input()
points_from_academy = float(input())
number_of_judges = int(input())
for judge in range(1, number_of_judges + 1):
    name_of_judge = input()
    points_from_judge = float(input())
    points_from_academy += (len(name_of_judge) * points_from_judge) / 2
    if points_from_academy > 1250.5:
        break
if points_from_academy > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {points_from_academy:.1f}!")
else:
    diff = 1250.5 - points_from_academy
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")
