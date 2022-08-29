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