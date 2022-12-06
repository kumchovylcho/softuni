def shoot(current_index, power, current_targets):
    if 0 <= current_index < len(current_targets):
        current_targets[current_index] -= power
        if current_targets[current_index] <= 0:
            current_targets.pop(current_index)
    return current_targets


def add(current_index, add_value, current_targets):
    if 0 <= current_index < len(current_targets):
        current_targets.insert(current_index, add_value)
    else:
        print("Invalid placement!")
    return current_targets


def strike(current_index, radius, current_targets):
    start_index = current_index - radius
    end_index = current_index + radius
    if 0 <= start_index < len(current_targets) and 0 <= end_index < len(current_targets):
        current_targets = current_targets[:start_index] + current_targets[end_index + 1:]
    else:
        print("Strike missed!")
    return current_targets


targets = [int(target) for target in input().split()]
call_functions = {
    "Shoot": shoot,
    "Add": add,
    "Strike": strike
}
command = input()
while command != "End":
    task, index, info = [x if x.isalpha() else int(x) for x in command.split()]
    targets = call_functions[task](index, info, targets)
    command = input()
print(*targets, sep='|')


# def shooting(position, strike_damage):
#     if 0 <= position < len(targets):
#         targets[position] -= strike_damage
#         if targets[position] <= 0:
#             targets.pop(position)
#
#
# def add_target(position, target_value):
#     if 0 <= position < len(targets):
#         targets.insert(position, target_value)
#     elif position >= len(targets) or position < 0:
#         print("Invalid placement!")
#
#
# def strike(position, radius_of_strike):
#     from_current_position_to_0 = position - radius_of_strike     # if the result is less than zero, strike will miss
#     from_current_position_to_len_targets = position + radius_of_strike  # if the result is more than len(targets) , strike will miss
#     if from_current_position_to_0 >= 0 and from_current_position_to_len_targets < len(targets):
#         del targets[from_current_position_to_0:from_current_position_to_len_targets + 1]
#     elif from_current_position_to_0 < 0 or from_current_position_to_len_targets >= len(targets):
#         print("Strike missed!")
#
#
# targets = [int(target) for target in input().split()]
# command = input()
# while command != "End":
#     command = command.split()
#     event = command[0]
#     index = int(command[1])
#     if event == "Shoot":
#         strike_power = int(command[2])
#         shooting(index, strike_power)
#     elif event == "Add":
#         new_target = int(command[2])
#         add_target(index, new_target)
#     elif event == "Strike":
#         radius_of_the_strike = int(command[2])
#         strike(index, radius_of_the_strike)
#     command = input()
#
# print(*targets, sep="|")
