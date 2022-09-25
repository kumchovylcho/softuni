number_of_cars = int(input())
cars_information = {}

for car in range(number_of_cars):
    current_car, mileage, fuel = [string if string[0].isalpha() else int(string) for string in input().split("|")]
    cars_information[current_car] = cars_information.get(current_car, {'mileage': mileage, 'fuel': fuel})


command = input()
while command != "Stop":
    command = command.split(" : ")
    operation = command[0]
    car = command[1]

    if operation == "Drive":
        distance, fuel = int(command[2]), int(command[3])
        if cars_information[car]['fuel'] >= fuel:
            cars_information[car]['fuel'] -= fuel
            cars_information[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_information[car]['mileage'] >= 100000:
                del cars_information[car]
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")

    elif operation == "Refuel":
        fuel = int(command[2])
        amount_refueled = 0
        if cars_information[car]['fuel'] + fuel >= 75:
            amount_refueled = 75 - cars_information[car]['fuel']
        elif cars_information[car]['fuel'] + fuel < 75:
            amount_refueled = fuel
        cars_information[car]['fuel'] += amount_refueled
        print(f"{car} refueled with {amount_refueled} liters")

    elif operation == "Revert":
        reverted_kilometers = int(command[2])
        if cars_information[car]['mileage'] - reverted_kilometers >= 10000:
            cars_information[car]['mileage'] -= reverted_kilometers
            print(f"{car} mileage decreased by {reverted_kilometers} kilometers")
        elif cars_information[car]['mileage'] - reverted_kilometers < 10000:
            cars_information[car]['mileage'] = 10000

    command = input()

for remaining_cars in cars_information:
    print(f"{remaining_cars} -> Mileage: {cars_information[remaining_cars]['mileage']} kms, "
          f"Fuel in the tank: {cars_information[remaining_cars]['fuel']} lt.")
