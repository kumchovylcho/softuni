students_with_grades = dict()


def main():
    pair_of_rows = int(input())
    for pair in range(pair_of_rows):
        student_name = input()
        student_grade = float(input())

        if student_name not in students_with_grades:
            students_with_grades[student_name] = []

        students_with_grades[student_name].append(student_grade)

    average_grade_checker()


def average_grade_checker():
    for student in students_with_grades:
        average_grade = sum(students_with_grades[student]) / len(students_with_grades[student])
        if average_grade >= 4.50:
            print(f"{student} -> {average_grade:.2f}")


main()

#
# student_info = int(input())
# student_grades = {}
#
# for _ in range(student_info):
#     student_name, student_grade = input(), float(input())
#
#     student_grades[student_name] = student_grades.get(student_name, {})
#     student_grades[student_name][student_name + str(student_grade)] = student_grade
#
# for name in student_grades:
#     all_grades = 0
#     for grade in student_grades[name]:
#         all_grades += student_grades[name][grade]
#     if all_grades / len(student_grades[name]) >= 4.50:
#         print(f"{name} -> {all_grades / len(student_grades[name]):.2f}")
