students_record = {}
number_of_students = int(input())
for student in range(number_of_students):
    name, grade = [float(item) if item[-1].isdigit() else item for item in input().split()]
    students_record[name] = students_record.get(name, []) + [grade]
for key, value in students_record.items():
    average = f"{sum(value) / len(value):.2f}"
    print(f"{key} -> {' '.join(f'{item:.2f}' for item in value)} (avg: {average})")