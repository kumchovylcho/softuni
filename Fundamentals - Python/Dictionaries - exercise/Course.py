courses_information = dict()


def main():
    command = input()
    while command != "end":
        command = command.split(" : ")

        course = command[0]
        student_name = command[1]
        user_registration(course, student_name)

        command = input()
    print_result()


def user_registration(course, student):
    if course not in courses_information:
        courses_information[course] = []
    courses_information[course].append(student)


def print_result():
    for course in courses_information:
        print(f"{course}: {len(courses_information[course])}")
        for student in courses_information[course]:
            print(f"-- {student}")


main()


# courses_info = {}
#
# courses = input()
# while courses != "end":
#     courses = courses.split(" : ")
#     course_name, student_name = courses[0], courses[1]
#
#     courses_info[course_name] = courses_info.get(course_name,  {})
#     courses_info[course_name][student_name] = student_name
#
#     courses = input()
#
# for key, value in courses_info.items():
#     print(f"{key}: {len(courses_info[key])}")
#     for name in courses_info[key]:
#         print(f"-- {courses_info[key][name]}")
