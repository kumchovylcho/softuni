targets = [int(target) for target in input().split()]


def shooting(position, strike_damage):
    if 0 <= position < len(targets):
        targets[position] -= strike_damage
        if targets[position] <= 0:
            targets.pop(position)


def add_target(position, target_value):
    if 0 <= position < len(targets):
        targets.insert(position, target_value)
    elif position >= len(targets) or position < 0:
        print("Invalid placement!")


def strike(position, radius_of_strike):
    from_current_position_to_0 = position - radius_of_strike     # if the result is less than zero, strike will miss
    from_current_position_to_len_targets = position + radius_of_strike  # if the result is more than len(targets) , strike will miss
    if from_current_position_to_0 >= 0 and from_current_position_to_len_targets < len(targets):
        del targets[from_current_position_to_0:from_current_position_to_len_targets + 1]
    elif from_current_position_to_0 < 0 or from_current_position_to_len_targets >= len(targets):
        print("Strike missed!")


command = input()
while command != "End":
    command = command.split()
    event = command[0]
    index = int(command[1])
    if event == "Shoot":
        strike_power = int(command[2])
        shooting(index, strike_power)
    elif event == "Add":
        new_target = int(command[2])
        add_target(index, new_target)
    elif event == "Strike":
        radius_of_the_strike = int(command[2])
        strike(index, radius_of_the_strike)
    command = input()

print(*targets, sep="|")
