energy = 100
coins = 100
commands_for_the_day = input().split("|")
for command in commands_for_the_day:
    list_with_commands = command.split("-")
    event = list_with_commands[0]
    coin = int(list_with_commands[1])
    if event == "rest":
        rest_points = coin
        if energy + rest_points > 100:
            print(f"You gained {abs(100 - energy)} energy.")
            energy = 100
        else:
            energy += rest_points
            print(f"You gained {rest_points} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += coin
            print(f"You earned {coin} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        ingredient = event
        price = coin
        if coins >= price:
            coins -= price
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            exit()

print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
