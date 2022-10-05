lessons = input().split(", ")


def add(lesson_tittle):
    if lesson_tittle not in lessons:
        lessons.append(lesson_tittle)


def insert(lesson_tittle, index_to_position):
    if lesson_tittle not in lessons:
        lessons.insert(index_to_position, lesson_tittle)


def remove(lesson_tittle):
    if lesson_tittle in lessons:
        lessons.remove(lesson_tittle)
    if f"{lesson_tittle}-Exercise" in lessons:
        lessons.remove(f"{lesson_tittle}-Exercise")


def swap(lesson_1, lesson_2):
    if lesson_1 in lessons and lesson_2 in lessons:
        first_lesson = lessons.index(lesson_1)
        second_lesson = lessons.index(lesson_2)
        lessons[first_lesson], lessons[second_lesson] = lessons[second_lesson], lessons[first_lesson]
        if lesson_2 and f"{lesson_2}-Exercise" in lessons:
            index_of_lesson_2 = lessons.index(lesson_2) + 1
            lessons.insert(index_of_lesson_2, f"{lesson_2}-Exercise")
            lessons.pop(lessons.index(f"{lesson_2}-Exercise", lessons.index(f"{lesson_2}-Exercise") + 1))
        if lesson_1 and f"{lesson_1}-Exercise" in lessons:
            index_of_lesson_1 = lessons.index(lesson_1) + 1
            lessons.insert(index_of_lesson_1, f"{lesson_1}-Exercise")
            lessons.pop(lessons.index(f"{lesson_1}-Exercise", lessons.index(f"{lesson_1}-Exercise") + 1))


def exercise(lesson_title):
    if lesson_title in lessons:
        if f"{lesson_title}-Exercise" not in lessons:
            current_lesson_index = lessons.index(lesson_title) + 1
            lessons.insert(current_lesson_index, f"{lesson_title}-Exercise")
    elif lesson_title not in lessons:
        lessons.append(lesson_title)
        lessons.append(f"{lesson_title}-Exercise")


command = input()
while command != "course start":
    command = command.split(":")
    operation = command[0]
    lesson_title = command[1]
    if operation == "Add":
        add(lesson_title)
    elif operation == "Insert":
        index = int(command[2])
        insert(lesson_title, index)
    elif operation == "Remove":
        remove(lesson_title)
    elif operation == "Swap":
        lesson_title_1 = command[1]
        lesson_title_2 = command[2]
        swap(lesson_title_1, lesson_title_2)
    elif operation == "Exercise":
        exercise(lesson_title)
    command = input()


for count, lesson in enumerate(lessons, 1):
    print(f"{count}.{lesson}")