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