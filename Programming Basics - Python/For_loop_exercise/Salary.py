number_of_open_tabs = int(input())
salary = int(input())
salary_left = salary
for tab in range(1, number_of_open_tabs + 1):
    current_tab = input()
    if current_tab == "Facebook":
        salary_left -= 150
    elif current_tab == "Instagram":
        salary_left -= 100
    elif current_tab == "Reddit":
        salary_left -= 50
    if salary_left <= 0:
        break
if salary_left <= 0:
    print(f"You have lost your salary.")
else:
    print(salary_left)
