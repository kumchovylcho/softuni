numbers_of_visitors = int(input())
back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_shake = 0
protein_bar = 0
for visitor in range(1, numbers_of_visitors + 1):
    activity = input()
    if activity == "Back":
        back_count += 1
    elif activity == "Chest":
        chest_count += 1
    elif activity == "Legs":
        legs_count += 1
    elif activity == "Abs":
        abs_count += 1
    elif activity == "Protein shake":
        protein_shake += 1
    else:
        protein_bar += 1
percent_work_out_people = ((back_count + chest_count + legs_count + abs_count) / numbers_of_visitors) * 100
percent_people_bought_protein = ((protein_shake + protein_bar) / numbers_of_visitors) * 100
print(f"{back_count} - back\n{chest_count} - chest\n{legs_count} - legs\n{abs_count} - abs\n{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar\n{percent_work_out_people:.2f}% - work out\n{percent_people_bought_protein:.2f}% - protein")
