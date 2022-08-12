number_of_students_on_exam = int(input())
two_to_three = 0
three_to_four = 0
four_to_five = 0
five_or_more = 0
all_grades = 0
for student in range(1, number_of_students_on_exam + 1):
    grade_from_exam = float(input())
    if 2.00 <= grade_from_exam <= 2.99:
        two_to_three += 1
    elif 3.00 <= grade_from_exam <= 3.99:
        three_to_four += 1
    elif 4.00 <= grade_from_exam <= 4.99:
        four_to_five += 1
    else:
        five_or_more += 1
    all_grades += grade_from_exam
total_grades = two_to_three + three_to_four + four_to_five + five_or_more
average_grade = all_grades / total_grades
top_students = five_or_more / total_grades * 100
between_four_and_five = four_to_five / total_grades * 100
between_three_and_four = three_to_four / total_grades * 100
fail = two_to_three / total_grades * 100
print(f"Top students: {top_students:.2f}%\nBetween 4.00 and 4.99: {between_four_and_five:.2f}%\nBetween 3.00 and 3.99: {between_three_and_four:.2f}%")
print(f"Fail: {fail:.2f}%\nAverage: {average_grade:.2f}")
