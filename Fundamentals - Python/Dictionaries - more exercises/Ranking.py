exams_info = {
    'password': {},
    'submissions': {}
}

course_password = input()
while course_password != "end of contests":
    course, password = [string for string in course_password.split(":")]
    exams_info['password'][course] = exams_info['password'].get(course, password)
    course_password = input()

user_submission = input()
while user_submission != "end of submissions":
    course, password, name, points = [int(string) if string.isdigit() else string
                                      for string in user_submission.split("=>")]
    if course in exams_info['password'] and password in exams_info['password'][course]:
        exams_info['submissions'][name] = exams_info['submissions'].get(name, {})
        exams_info['submissions'][name][course] = exams_info['submissions'][name].get(course, 0)
        if exams_info['submissions'][name][course] < points:
            exams_info['submissions'][name][course] = points

    user_submission = input()

max_score = 0
current_student = 0
name_with_highest_points = ""
for student_name in exams_info['submissions']:
    for exam_points in exams_info['submissions'][student_name]:
        current_student += exams_info['submissions'][student_name][exam_points]
    if current_student > max_score:
        max_score = current_student
        name_with_highest_points = student_name
    current_student = 0
print(f"Best candidate is {name_with_highest_points} with total {max_score} points.")

print("Ranking:")
for names in sorted(exams_info['submissions']):
    print(names)
    for language, points in sorted(exams_info['submissions'][names].items(), key=lambda item: -item[1]):
        print(f"#  {language} -> {points}")
