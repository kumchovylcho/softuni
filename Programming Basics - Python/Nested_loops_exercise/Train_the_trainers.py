total_grades_counter = 0
total_score = 0
people_in_jury = int(input())
name_of_presentation = input()
while name_of_presentation != "Finish":
    score = 0
    for presentation in range(1, people_in_jury + 1):
        grades = float(input())
        score += grades
        total_grades_counter += 1
        total_score += grades
    average_for_current_presentation = score / people_in_jury
    print(f"{name_of_presentation} - {average_for_current_presentation:.2f}.")
    name_of_presentation = input()
average_of_all_presentations = total_score / total_grades_counter
print(f"Student's final assessment is {average_of_all_presentations:.2f}.")
