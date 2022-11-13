class Company:
    def __init__(self):
        self.company = {}

    def check_for_company(self, company_name):
        self.company[company_name] = self.company.get(company_name, [])

    def check_for_user(self, user, company_name):
        if user not in self.company[company_name]:
            self.company[company_name].append(user)


company_users = Company()
current_company = input()
while current_company != "End":
    name_of_company, employee_id = current_company.split(" -> ")
    company_users.check_for_company(name_of_company)
    company_users.check_for_user(employee_id, name_of_company)
    current_company = input()
for key in company_users.company:
    print(key)
    for user_id in company_users.company[key]:
        print(f"-- {user_id}")


# company_info = {}
#
# company_employee = input()
# while company_employee != "End":
#     company_employee = company_employee.split(" -> ")
#     company, employee = company_employee[0], company_employee[1]
#
#     company_info[company] = company_info.get(company, [])
#     if employee not in company_info[company]:
#         company_info[company].append(employee)
#
#     company_employee = input()
#
# for key in company_info:
#     print(key)
#     [print(f"-- {employee}") for employee in company_info[key]]


# company_info = dict()
#
# command = input()
# while command != "End":
#     command = command.split(" -> ")
#
#     company = command[0]
#     employee_id = command[1]
#
#     if company not in company_info:
#         company_info[company] = []
#         company_info[company].append(employee_id)
#
#     elif company in company_info:
#         if employee_id not in company_info[company]:
#             company_info[company].append(employee_id)
#
#     command = input()
#
#
# for company in company_info:
#     print(company)
#     for student_id in company_info[company]:
#         print(f"-- {student_id}")


