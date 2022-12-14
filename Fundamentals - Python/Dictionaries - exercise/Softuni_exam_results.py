exams_info = {
    'submissions': {},
    'points': {}

}

command = input()
while command != "exam finished":
    command = command.split("-")
    if "banned" not in command:
        name, language, points = [int(name) if name.isdigit() else name for name in command]

        exams_info['submissions'][language] = exams_info['submissions'].get(language, 0) + 1
        exams_info['points'][name] = exams_info['points'].get(name, points)

        if exams_info['points'][name] < points:
            exams_info['points'][name] = points

    elif "banned" in command:
        name = command[0]
        del exams_info['points'][name]

    command = input()

print(f"Results:")
[print(f"{user} | {exams_info['points'][user]}") for user in exams_info['points']]
print(f"Submissions:")
[print(f"{language} - {exams_info['submissions'][language]}") for language in exams_info['submissions']]


# exam_results = {
#     "submissions":
#         {},
#     "results":
#         {}
# }
#
#
# def main():
#     exam_info = input()
#     while exam_info != "exam finished":
#         exam_info = exam_info.split("-")
#
#         if len(exam_info) == 3:
#             register_student(exam_info[0], exam_info[1], int(exam_info[2]))
#
#         elif len(exam_info) < 3:
#             ban_student(exam_info[0])
#
#         exam_info = input()
#     print_results()
#
#
# def register_student(username, language, points):
#     if language not in exam_results["results"]:
#         exam_results["results"][language] = {username: points}
#         exam_results["submissions"][language] = 1
#
#     elif language in exam_results["results"]:
#         exam_results["submissions"][language] += 1
#         if username in exam_results["results"][language]:
#             if points > exam_results["results"][language][username]:
#                 exam_results["results"][language][username] = points
#
#         elif username not in exam_results["results"][language]:
#             exam_results["results"][language][username] = points
#
#
# def ban_student(username):
#     for language in exam_results["results"]:
#         for name in exam_results["results"][language]:
#             if name == username:
#                 del exam_results["results"][language][name]
#                 break
#
#
# def print_results():
#     print("Results:")
#     for language in exam_results["results"]:
#         for name in exam_results["results"][language]:
#             print(f"{name} | {exam_results['results'][language][name]}")
#
#     print("Submissions:")
#     for language in exam_results["submissions"]:
#         print(f"{language} - {exam_results['submissions'][language]}")
#
#
# main()
#
#
# exam_results = {
#     "submissions":
#         {},
#     "results":
#         {}
# }
#
# exam_info = input()
# while exam_info != "exam finished":
#     exam_info = exam_info.split("-")
#
#     if len(exam_info) == 3:
#         username = exam_info[0]
#         language = exam_info[1]
#         points = int(exam_info[2])
#
#         if language not in exam_results["results"]:
#             exam_results["results"][language] = {username: points}
#             exam_results["submissions"][language] = 1
#
#         elif language in exam_results["results"]:
#             exam_results["submissions"][language] += 1
#             if username in exam_results["results"][language]:
#                 if points > exam_results["results"][language][username]:
#                     exam_results["results"][language][username] = points
#
#             elif username not in exam_results["results"][language]:
#                 exam_results["results"][language][username] = points
#
#     elif len(exam_info) < 3:
#         username = exam_info[0]
#         for language in exam_results["results"]:
#             for name in exam_results["results"][language]:
#                 if name == username:
#                     del exam_results["results"][language][name]
#                     break
#
#     exam_info = input()
#
# print("Results:")
# for language in exam_results["results"]:
#     for name in exam_results["results"][language]:
#         print(f"{name} | {exam_results['results'][language][name]}")
#
# print("Submissions:")
# for language in exam_results["submissions"]:
#     print(f"{language} - {exam_results['submissions'][language]}")
