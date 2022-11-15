parking = set()
number_of_operations = int(input())
for car in range(number_of_operations):
    command, car_plate = input().split(", ")
    if command == 'IN':
        parking.add(car_plate)
    elif command == 'OUT':
        parking.discard(car_plate)
if parking:
    print('\n'.join(parking))
elif not parking:
    print("Parking Lot is Empty")