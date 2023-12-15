def softuni_students(*args, **kwargs):
    students = {}
    invalid_students = []
    for course_id, username in args:
        if course_id not in kwargs:
            invalid_students.append(username)
            continue

        students[username] = course_id


    output = []
    sorted_by_username = dict(sorted(students.items()))
    for username, course_id in sorted_by_username.items():
        course_name = kwargs[course_id]
        result = f"*** A student with the username {username} has successfully finished the course {course_name}!"
        output.append(result)

    if invalid_students:
        invalid_students_result = f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"
        output.append(invalid_students_result)

    return "\n".join(output)




print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))

print()

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))

print()

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))