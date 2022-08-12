money_needed_for_vacation = float(input())
current_money = float(input())
spending_counter = 0
days = 0
while current_money < money_needed_for_vacation:
    if spending_counter == 5:
        break
    command = input()
    save_or_spent = float(input())
    days += 1
    if command == "spend":
        spending_counter += 1
        current_money -= save_or_spent
        if current_money < 0:
            current_money = 0
    elif command == "save":
        spending_counter = 0
        current_money += save_or_spent
if spending_counter == 5:
    print(f"You can't save the money.\n{days}")
else:
    print(f"You saved the money for {days} days.")
