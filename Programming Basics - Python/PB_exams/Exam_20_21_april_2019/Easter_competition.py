best_baker = ""
most_points = 0
current_points = 0
number_of_easter_breads = int(input())
for easter_breads in range(1, number_of_easter_breads + 1):
    current_points = 0
    name_of_the_baker = input()
    score_of_easter_bread = input()
    while score_of_easter_bread != "Stop":
        if score_of_easter_bread == "Stop":
            break
        current_points += int(score_of_easter_bread)
        score_of_easter_bread = input()
    print(f"{name_of_the_baker} has {current_points} points.")

    if current_points > most_points:
        most_points = current_points
        best_baker = name_of_the_baker
        print(f"{name_of_the_baker} is the new number 1!")
print(f"{best_baker} won competition with {most_points} points!")
