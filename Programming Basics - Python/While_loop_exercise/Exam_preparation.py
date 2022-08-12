number_of_poor_grades = int(input())
poor_grades = number_of_poor_grades
score_of_grades = 0
number_of_problems = 0
last_problem = ""
is_over = False
name_of_task = input()
while name_of_task != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        poor_grades -= 1
        number_of_problems += 1
        score_of_grades += current_grade
        if poor_grades == 0:
            is_over = True
            break
    else:
        score_of_grades += current_grade
        number_of_problems += 1
    last_problem = name_of_task
    name_of_task = input()
if name_of_task == "Enough":
    average_score = score_of_grades / number_of_problems
    print(f"Average score: {average_score:.2f}\nNumber of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")
if is_over:
    print(f"You need a break, {number_of_poor_grades} poor grades.")
