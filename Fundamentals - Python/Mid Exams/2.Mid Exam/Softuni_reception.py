employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
number_of_students = int(input())
all_employees = employee_1 + employee_2 + employee_3
hours_to_answer_the_questions = 0

while number_of_students > 0:
    hours_to_answer_the_questions += 1
    if hours_to_answer_the_questions % 4 == 0:
        continue
    number_of_students -= all_employees

print(f"Time needed: {hours_to_answer_the_questions}h.")