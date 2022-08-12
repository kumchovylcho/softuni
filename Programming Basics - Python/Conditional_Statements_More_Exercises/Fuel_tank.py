type_of_fuel = input().lower()
litres_in_tank = int(input())
if type_of_fuel == "diesel":
    if litres_in_tank >= 25:
        print(f"You have enough {type_of_fuel}.")
    else:
        print(f"Fill your tank with {type_of_fuel}!")
elif type_of_fuel == "gasoline":
    if litres_in_tank >= 25:
        print(f"You have enough {type_of_fuel}.")
    else:
        print(f"Fill your tank with {type_of_fuel}!")
elif type_of_fuel == "gas":
    if litres_in_tank >= 25:
        print(f"You have enough {type_of_fuel}.")
    else:
        print(f"Fill your tank with {type_of_fuel}!")
else:
    print(f"Invalid fuel!")
