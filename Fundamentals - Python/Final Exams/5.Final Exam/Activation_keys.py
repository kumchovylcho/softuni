activation_key = input()

command = input()
while command != "Generate":
    command = command.split(">>>")

    if command[0] == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")

        elif substring not in activation_key:
            print("Substring not found!")

    elif command[0] == "Flip":
        upper_or_lower_letters = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if upper_or_lower_letters == "Upper":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() \
                             + activation_key[end_index:]

        elif upper_or_lower_letters == "Lower":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() \
                             + activation_key[end_index:]

    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]

    if command[0] != "Contains":
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
