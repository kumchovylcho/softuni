balance = float(input())
current_balance = balance
game_prices = {
    'OutFall 4': 39.99,
    'CS: OG': 15.99,
    'Zplinter Zell': 19.99,
    'Honored 2': 59.99,
    'RoverWatch': 29.99,
    'RoverWatch Origins Edition': 39.99
}

command = input()
while command != "Game Time":
    if command not in game_prices:
        print("Not Found")
        command = input()
        continue
    elif command in game_prices:
        if current_balance < game_prices[command]:
            print("Too Expensive")
            command = input()
            continue
        else:
            print(f"Bought {command}")
            current_balance -= game_prices[command]
    if current_balance <= 0:
        print("Out of money!")
        break

    command = input()

total_spent = balance - current_balance
money_remaining = balance - total_spent

if current_balance:
    print(f"Total spent: ${total_spent:.2f}. Remaining: ${money_remaining:.2f}")