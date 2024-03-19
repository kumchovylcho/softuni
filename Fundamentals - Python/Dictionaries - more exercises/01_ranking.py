contest_passwords = {}
submissions = {}

contest = input()
while contest != "end of contests":
    contest_name, password = contest.split(":")
    contest_passwords[contest_name] = password

    contest = input()

submission = input()
while submission != "end of submissions":
    contest_name, password, username, points = [int(x) if x.isdigit() else x for x in submission.split("=>")]

    if contest_name not in contest_passwords or contest_passwords[contest_name] != password:
        submission = input()
        continue

    submissions[username] = submissions.get(username, {})
    submissions[username][contest_name] = submissions[username].get(contest_name, 0)
    submissions[username][contest_name] = max(submissions[username][contest_name], points)

    submission = input()

best_user, total_points = "", 0
for user, contest_points in submissions.items():
    current_points = sum(contest_points.values())
    if current_points > total_points:
        total_points = current_points
        best_user = user

print(f"Best candidate is {best_user} with total {total_points} points.")
print("Ranking:")
for user in sorted(submissions):
    print(user)
    for contest_name, points in sorted(submissions[user].items(), key=lambda point: (-point[1])):
        print(f"#  {contest_name} -> {points}")




# exams_info = {
#     'password': {},
#     'submissions': {}
# }
#
# course_password = input()
# while course_password != "end of contests":
#     course, password = [string for string in course_password.split(":")]
#     exams_info['password'][course] = exams_info['password'].get(course, password)
#     course_password = input()
#
# user_submission = input()
# while user_submission != "end of submissions":
#     course, password, name, points = [int(string) if string.isdigit() else string
#                                       for string in user_submission.split("=>")]
#     if course in exams_info['password'] and password in exams_info['password'][course]:
#         exams_info['submissions'][name] = exams_info['submissions'].get(name, {})
#         exams_info['submissions'][name][course] = exams_info['submissions'][name].get(course, 0)
#         if exams_info['submissions'][name][course] < points:
#             exams_info['submissions'][name][course] = points
#
#     user_submission = input()
#
# max_score = 0
# current_student = 0
# name_with_highest_points = ""
# for student_name in exams_info['submissions']:
#     for exam_points in exams_info['submissions'][student_name]:
#         current_student += exams_info['submissions'][student_name][exam_points]
#     if current_student > max_score:
#         max_score = current_student
#         name_with_highest_points = student_name
#     current_student = 0
# print(f"Best candidate is {name_with_highest_points} with total {max_score} points.")
#
# print("Ranking:")
# for names in sorted(exams_info['submissions']):
#     print(names)
#     for language, points in sorted(exams_info['submissions'][names].items(), key=lambda item: -item[1]):
#         print(f"#  {language} -> {points}")
