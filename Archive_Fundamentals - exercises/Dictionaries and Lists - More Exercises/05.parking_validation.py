def length_validation(plate_number):       # 90/100
    if len(plate_number) == 8:
        return True
    return False


def front_back_letters(plate_number):
    if plate_number[:2].isupper() and plate_number[-2:].isupper():
        return True
    return False


def middle_numbers(plate_number):
    middle = [digit for digit in plate_number[2:-2] if digit.isdigit()]
    if len(middle) == 4:
        return True
    return False


parking = {}
number_of_cars = int(input())
for _ in range(number_of_cars):
    command, *info = input().split()
    if command == "register":
        user, plate = info[0], info[1]
        if length_validation(plate) and front_back_letters(plate) and middle_numbers(plate):
            errors = []
            if user in parking:
                if plate in parking[user]:
                    errors.append(f"ERROR: already registered with plate number {parking[user]}")
            elif user not in parking and plate in parking.values():
                errors.append(f"ERROR: license plate {plate} is busy")
            if not errors:
                if user not in parking:
                    print(f"{user} registered {plate} successfully")
                    parking[user] = plate
                else:
                    print(f"ERROR: already registered with plate number {parking[user]}")
            elif errors:
                print('\n'.join(errors))
        else:
            print(f"ERROR: invalid license plate {plate}")
    elif command == "unregister":
        user = info[0]
        if user not in parking:
            print(f"ERROR: user {user} not found")
        elif user in parking:
            del parking[user]
            print(f"user {user} unregistered successfully")
for key, value in parking.items():
    print(f"{key} => {value}")