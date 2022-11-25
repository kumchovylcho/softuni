import re
pattern = r'([A-Z]{2}[0-9]{4}[A-Z]{2})'
parking = {}
number_of_cars = int(input())
for _ in range(number_of_cars):
    command, *info = input().split()
    if command == "register":
        user, plate = info[0], info[1]
        matches = re.findall(pattern, plate)
        if user in parking:
            print(f"ERROR: already registered with plate number {parking[user]}")
        elif not matches:
            print(f"ERROR: invalid license plate {plate}")
        elif plate in parking.values():
            print(f"ERROR: license plate {plate} is busy")
        else:
            print(f"{user} registered {plate} successfully")
            parking[user] = plate
    elif command == "unregister":
        user = info[0]
        if user not in parking:
            print(f"ERROR: user {user} not found")
        elif user in parking:
            del parking[user]
            print(f"user {user} unregistered successfully")
for key, value in parking.items():
    print(f"{key} => {value}")