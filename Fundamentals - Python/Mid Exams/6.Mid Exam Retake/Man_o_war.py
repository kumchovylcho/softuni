def fire(war_ship_sections, target_section, dmg_output, is_sunken):
    if 0 <= target_section < len(war_ship_sections):
        war_ship_sections[target_section] -= dmg_output
        if war_ship_sections[target_section] <= 0:
            is_sunken = True
            print("You won! The enemy ship has sunken.")
    return war_ship_sections, is_sunken


def defend(pirate_ship_sections, start_index, end_index, dmg_received, is_sunken):
    if 0 <= start_index < len(pirate_ship_sections) and 0 <= end_index < len(pirate_ship_sections):
        for ship in range(start_index, end_index + 1):
            pirate_ship_sections[ship] -= dmg_received
            if pirate_ship_sections[ship] <= 0:
                is_sunken = True
                print("You lost! The pirate ship has sunken.")
                break
    return pirate_ship_sections, is_sunken


def repair(pirate_ship_sections, target_section, health, max_hp):
    if 0 <= target_section < len(pirate_ship_sections):
        if pirate_ship_sections[target_section] + health > max_hp:
            pirate_ship_sections[target_section] = max_hp
        else:
            pirate_ship_sections[target_section] += health
    return pirate_ship_sections


def status(pirate_ship_sections, max_hp):
    min_section_health = max_hp * 0.2
    sections_to_repair = [ship for ship in pirate_ship_sections if ship < min_section_health]
    print(f"{len(sections_to_repair)} sections need repair.")
    return pirate_ship_sections


pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))

max_health = int(input())

commands = input()

sink = False
while commands != "Retire":
    action, *data = [item if item.isalpha() else int(item) for item in commands.split()]

    if action == "Fire":
        war_ship, sink = fire(war_ship, data[0], data[1], sink)
    elif action == "Defend":
        pirate_ship, sink = defend(pirate_ship, data[0], data[1], data[2], sink)
    elif action == "Repair":
        pirate_ship = repair(pirate_ship, data[0], data[1], max_health)
    elif action == "Status":
        pirate_ship = status(pirate_ship, max_health)
    if sink:
        break

    commands = input()
if not sink:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")


# def attack_warship(warship_position, damage_dealt):
#     global is_sunken
#     if 0 <= warship_position < len(status_of_warships):
#         status_of_warships[warship_position] -= damage_dealt
#         if status_of_warships[warship_position] <= 0:
#             print("You won! The enemy ship has sunken.")
#             is_sunken = True
#     return is_sunken
#
#
# def defending_pirate_ships(start_position, ending_position, damage_taken):
#     global is_sunken
#     if 0 <= start_position < len(status_of_pirate_ships) and 0 <= ending_position < len(status_of_pirate_ships):
#         status_of_pirate_ships[start_position:ending_position + 1] = [ship - damage_taken for ship in status_of_pirate_ships[start_position:ending_position + 1]]
#         sunken_pirate_ships_checker = [ship for ship in status_of_pirate_ships[start_position:ending_position + 1] if ship <= 0]
#         if sunken_pirate_ships_checker:
#             is_sunken = True
#             print("You lost! The pirate ship has sunken.")
#     return is_sunken
#
#
# def repair_ship(ship_index, hp_repaired):
#     if 0 <= ship_index < len(status_of_pirate_ships):
#         status_of_pirate_ships[ship_index] += hp_repaired
#         if status_of_pirate_ships[ship_index] > max_pirate_ship_HP:
#             status_of_pirate_ships[ship_index] = max_pirate_ship_HP
#
#
# def status_checker():
#     low_hp_math = max_pirate_ship_HP * 0.2
#     ships_to_repair = [ship for ship in status_of_pirate_ships if ship < low_hp_math]
#     print(f"{len(ships_to_repair)} sections need repair.")
#
#
# status_of_pirate_ships = [int(ship) for ship in input().split(">")]
# status_of_warships = [int(ship) for ship in input().split(">")]
# max_pirate_ship_HP = int(input())
# is_sunken = False
# command = input()
# while command != "Retire":
#     command = command.split()
#     event = command[0]
#     if event == "Fire":
#         index = int(command[1])
#         damage = int(command[2])
#         attack_warship(index, damage)
#     elif event == "Defend":
#         start_index = int(command[1])
#         ending_index = int(command[2])
#         damage = int(command[3])
#         defending_pirate_ships(start_index, ending_index, damage)
#     elif event == "Repair":
#         index = int(command[1])
#         hp_repair = int(command[2])
#         repair_ship(index, hp_repair)
#     elif event == "Status":
#         status_checker()
#     if is_sunken:
#         break
#     command = input()
#
#
# if status_of_pirate_ships and status_of_warships and command == "Retire":
#     print(f"Pirate ship status: {sum(status_of_pirate_ships)}")
#     print(f"Warship status: {sum(status_of_warships)}")
