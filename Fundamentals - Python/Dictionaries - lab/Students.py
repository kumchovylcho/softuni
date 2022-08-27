courses = dict()

fill_in_students = input()
while ":" in fill_in_students:
    fill_in_students = fill_in_students.split(":")

    student_course = fill_in_students[2]
    student_ID = fill_in_students[1]
    student_name = fill_in_students[0]

    if student_course not in courses:
        courses[student_course] = dict()

    courses[student_course][student_name] = student_ID
    fill_in_students = input()

fill_in_students = fill_in_students.replace("_", " ")

if fill_in_students in courses:
    for id in courses[fill_in_students]:
        print(f"{id} - {courses[fill_in_students][id]}")
