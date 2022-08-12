name_of_student = input()
score_of_grades = 0
current_grade = 1
poor_grades = 0
is_excluded = False
while current_grade <= 12:
    yearly_grade = float(input())
    if 4 <= yearly_grade <= 6:
        current_grade += 1
        score_of_grades += yearly_grade
    else:
        poor_grades += 1
        if poor_grades > 1:
            is_excluded = True
            break
else:
    average_grade = score_of_grades / 12
    print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")
if is_excluded:
    print(f"{name_of_student} has been excluded at {current_grade} grade")
