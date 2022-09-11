register_information = dict()


def register_check(name, license_plate):
    if name in register_information:
        print(f"ERROR: already registered with plate number {license_plate}")

    elif name not in register_information:
        register_information[name] = license_plate
        print(f"{name} registered {license_plate} successfully")


def unregister(name):
    if name not in register_information:
        print(f"ERROR: user {name} not found")

    elif name in register_information:
        del register_information[name]
        print(f"{name} unregistered successfully")


def registered_users():
    for user in register_information:
        print(f"{user} => {register_information[user]}")


def registration():
    number_of_commands = int(input())
    for _ in range(number_of_commands):
        register = input().split()

        registration = register[0]
        username = register[1]

        if registration == "register":
            license_plate = register[2]
            register_check(username, license_plate)

        elif registration == "unregister":
            unregister(username)

    registered_users()


registration()


# parking_lot = {}
#
# number_of_commands = int(input())
# for command in range(number_of_commands):
#     customer_info = input().split()
#
#     register_unregister, username = customer_info[0], customer_info[1]
#
#     if register_unregister == "register":
#         license_plate = customer_info[2]
#
#         if username not in parking_lot:
#             parking_lot[username] = {'license plate': license_plate}
#             print(f"{username} registered {license_plate} successfully")
#
#         elif username in parking_lot:
#             print(f"ERROR: already registered with plate number {license_plate}")
#
#     elif register_unregister == "unregister":
#         if username not in parking_lot:
#             print(f"ERROR: user {username} not found")
#
#         elif username in parking_lot:
#             print(f"{username} unregistered successfully")
#             del parking_lot[username]
#
# for key, value in parking_lot.items():
#     print(f"{key} => {parking_lot[key]['license plate']}")
