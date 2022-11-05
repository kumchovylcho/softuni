def drive(car_to_drive, distance, fuel_needed):
    upper_border_for_kilometers = 100000
    if cars_collection[car_to_drive]['fuel'] >= fuel_needed:
        cars_collection[car_to_drive]['mileage'] += distance
        cars_collection[car_to_drive]['fuel'] -= fuel_needed
        print(f"{car_to_drive} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        if cars_collection[car_to_drive]['mileage'] >= upper_border_for_kilometers:
            del cars_collection[car_to_drive]
            print(f"Time to sell the {car_to_drive}!")
    else:
        print("Not enough fuel to make that ride")


def refuel(refuel_car, refuel_amount):
    max_fuel_capacity = 75
    liters_refueled = 0
    if cars_collection[refuel_car]['fuel'] + refuel_amount > max_fuel_capacity:
        liters_refueled = max_fuel_capacity - cars_collection[refuel_car]['fuel']
        cars_collection[refuel_car]['fuel'] = max_fuel_capacity
    elif cars_collection[refuel_car]['fuel'] + refuel_amount <= max_fuel_capacity:
        cars_collection[refuel_car]['fuel'] += refuel_amount
        liters_refueled = refuel_amount
    print(f"{refuel_car} refueled with {liters_refueled} liters")


def revert(car_to_revert, reverted_kilometers):
    border_for_mileage = 10000
    if cars_collection[car_to_revert]['mileage'] - reverted_kilometers >= border_for_mileage:
        cars_collection[car_to_revert]['mileage'] -= reverted_kilometers
        print(f"{car_to_revert} mileage decreased by {reverted_kilometers} kilometers")
    elif cars_collection[car_to_revert]['mileage'] - reverted_kilometers < border_for_mileage:
        cars_collection[car_to_revert]['mileage'] = border_for_mileage


cars_collection = {}
number_of_cars = int(input())
for car in range(number_of_cars):
    type_of_car = input()
    current_car, mileage, fuel = [int(item) if item.isdigit() else item for item in type_of_car.split("|")]
    cars_collection[current_car] = cars_collection.get(current_car, {'mileage': mileage, 'fuel': fuel})
command = input()
while command != "Stop":
    operation, car_type, *info = [int(item) if item.isdigit() else item for item in command.split(" : ")]
    if operation == "Drive":
        drive(car_type, *info)
    elif operation == "Refuel":
        refuel(car_type, *info)
    elif operation == "Revert":
        revert(car_type, *info)
    command = input()
for key, value in cars_collection.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")


number_of_cars = int(input())
cars_information = {}

for car in range(number_of_cars):
    current_car, mileage, fuel = [string if string[0].isalpha() else int(string) for string in input().split("|")]
    cars_information[current_car] = cars_information.get(current_car, {'mileage': mileage, 'fuel': fuel})


# command = input()
# while command != "Stop":
#     command = command.split(" : ")
#     operation = command[0]
#     car = command[1]
#
#     if operation == "Drive":
#         distance, fuel = int(command[2]), int(command[3])
#         if cars_information[car]['fuel'] >= fuel:
#             cars_information[car]['fuel'] -= fuel
#             cars_information[car]['mileage'] += distance
#             print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#             if cars_information[car]['mileage'] >= 100000:
#                 del cars_information[car]
#                 print(f"Time to sell the {car}!")
#         else:
#             print("Not enough fuel to make that ride")
#
#     elif operation == "Refuel":
#         fuel = int(command[2])
#         amount_refueled = 0
#         if cars_information[car]['fuel'] + fuel >= 75:
#             amount_refueled = 75 - cars_information[car]['fuel']
#         elif cars_information[car]['fuel'] + fuel < 75:
#             amount_refueled = fuel
#         cars_information[car]['fuel'] += amount_refueled
#         print(f"{car} refueled with {amount_refueled} liters")
#
#     elif operation == "Revert":
#         reverted_kilometers = int(command[2])
#         if cars_information[car]['mileage'] - reverted_kilometers >= 10000:
#             cars_information[car]['mileage'] -= reverted_kilometers
#             print(f"{car} mileage decreased by {reverted_kilometers} kilometers")
#         elif cars_information[car]['mileage'] - reverted_kilometers < 10000:
#             cars_information[car]['mileage'] = 10000
#
#     command = input()
#
# for remaining_cars in cars_information:
#     print(f"{remaining_cars} -> Mileage: {cars_information[remaining_cars]['mileage']} kms, "
#           f"Fuel in the tank: {cars_information[remaining_cars]['fuel']} lt.")
