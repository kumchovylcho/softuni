company_info = dict()

command = input()
while command != "End":
    command = command.split(" -> ")

    company = command[0]
    employee_id = command[1]

    if company not in company_info:
        company_info[company] = []
        company_info[company].append(employee_id)

    elif company in company_info:
        if employee_id not in company_info[company]:
            company_info[company].append(employee_id)

    command = input()


for company in company_info:
    print(company)
    for student_id in company_info[company]:
        print(f"-- {student_id}")


