number_of_heroes = int(input())
all_heroes = {}

for every_hero in range(number_of_heroes):
    hero_name, hp, mp = [string if string.isalpha() else int(string) for string in input().split()]
    all_heroes[hero_name] = all_heroes.get(hero_name, {'hp': hp, 'mp': mp})

command = input()
while command != "End":
    command = command.split(" - ")
    event = command[0]
    hero_name = command[1]

    if event == "CastSpell":
        mp_needed_to_cast, spell_name = int(command[2]), command[3]
        if all_heroes[hero_name]['mp'] >= mp_needed_to_cast:
            all_heroes[hero_name]['mp'] -= mp_needed_to_cast
            print(f"{hero_name} has successfully cast {spell_name} and now has {all_heroes[hero_name]['mp']} MP!")
        elif all_heroes[hero_name]['mp'] < mp_needed_to_cast:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif event == "TakeDamage":
        damage_taken, attacker = int(command[2]), command[3]
        if all_heroes[hero_name]['hp'] - damage_taken > 0:
            all_heroes[hero_name]['hp'] -= damage_taken
            print(f"{hero_name} was hit for {damage_taken} HP by {attacker} "
                  f"and now has {all_heroes[hero_name]['hp']} HP left!")
        elif all_heroes[hero_name]['hp'] - damage_taken <= 0:
            del all_heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif event == "Recharge":
        mp_recharge = int(command[2])
        mana_gained = 0
        if all_heroes[hero_name]['mp'] + mp_recharge >= 200:
            mana_gained = 200 - all_heroes[hero_name]['mp']
        elif all_heroes[hero_name]['mp'] + mp_recharge < 200:
            mana_gained = mp_recharge
        all_heroes[hero_name]['mp'] += mana_gained
        print(f"{hero_name} recharged for {mana_gained} MP!")

    elif event == "Heal":
        amount_healed = int(command[2])
        hp_gained = 0
        if all_heroes[hero_name]['hp'] + amount_healed >= 100:
            hp_gained = 100 - all_heroes[hero_name]['hp']
        elif all_heroes[hero_name]['hp'] + amount_healed < 100:
            hp_gained = amount_healed
        all_heroes[hero_name]['hp'] += hp_gained
        print(f"{hero_name} healed for {hp_gained} HP!")
    command = input()

for alive_heroes in all_heroes:
    print(alive_heroes)
    print(f" HP: {all_heroes[alive_heroes]['hp']}")
    print(f" MP: {all_heroes[alive_heroes]['mp']}")
