travel_route = input().split("||")
fuel_amount = int(input())
ammo_amount = int(input())
for command in travel_route:
    command = command.split()
    operation = command[0]
    if operation == "Travel":
        light_years = int(command[1])
        if light_years > fuel_amount:
            print("Mission failed.")
            break
        elif light_years <= fuel_amount:
            fuel_amount -= light_years
            print(f"The spaceship travelled {light_years} light-years.")
    elif operation == "Enemy":
        enemy_armour = int(command[1])
        if ammo_amount >= enemy_armour:
            print(f"An enemy with {enemy_armour} armour is defeated.")
            ammo_amount -= enemy_armour
        elif ammo_amount < enemy_armour:
            fuel_amount = fuel_amount - (enemy_armour * 2)
            if fuel_amount < 0:
                print(f"Mission failed.")
                break
            else:
                print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
    elif operation == "Repair":
        added_fuel = int(command[1])
        fuel_amount += added_fuel
        ammo_amount += added_fuel * 2
        print(f"Ammunitions added: {added_fuel * 2}.")
        print(f"Fuel added: {added_fuel}.")
    elif operation == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
