number_of_students = int(input())
total_lectures = int(input())
bonus = int(input())
max_bonus_points = 0
biggest_attendance = 0

for student in range(1, number_of_students + 1):
    attendance_each_student = int(input())
    total_bonus = attendance_each_student / total_lectures * (5 + bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        biggest_attendance = attendance_each_student

print(f"Max Bonus: {round(max_bonus_points)}.")
print(f"The student has attended {biggest_attendance} lectures.")
