best_player = ""
most_goals = 0
name_of_player = input()
while name_of_player != "END":
    number_of_goals = int(input())
    if number_of_goals > most_goals:
        best_player = name_of_player
        most_goals = number_of_goals
    if number_of_goals >= 10:
        break
    name_of_player = input()
print(f"{best_player} is the best player!")
if most_goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
