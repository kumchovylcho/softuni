people, capacity = int(input()), int(input())

courses = people // capacity
people -= capacity * courses

if people:
    courses += 1

print(courses)