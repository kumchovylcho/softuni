class Heroes:

    def __init__(self):
        self.heroes = {}
        self.max_health = 100
        self.max_mana = 200

    def cast_spell(self, hero_name, mana_needed, spell_name):
        if self.heroes[hero_name]['mana'] >= mana_needed:
            self.heroes[hero_name]['mana'] -= mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {self.heroes[hero_name]['mana']} MP!")
        elif self.heroes[hero_name]['mana'] < mana_needed:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    def take_damage(self, hero_name, damage_taken, attacker_name):
        if self.heroes[hero_name]['hp'] - damage_taken > 0:
            self.heroes[hero_name]['hp'] -= damage_taken
            print(f"{hero_name} was hit for {damage_taken} HP by {attacker_name} and now has"
                  f" {self.heroes[hero_name]['hp']} HP left!")
        elif self.heroes[hero_name]['hp'] - damage_taken <= 0:
            print(f"{hero_name} has been killed by {attacker_name}!")
            del self.heroes[hero_name]

    def recharge(self, hero_name, mana_recharged):
        mana_gain = mana_recharged
        if self.heroes[hero_name]['mana'] + mana_gain > self.max_mana:
            mana_gain = self.max_mana - self.heroes[hero_name]['mana']
            self.heroes[hero_name]['mana'] = self.max_mana
        elif self.heroes[hero_name]['mana'] + mana_gain <= self.max_mana:
            self.heroes[hero_name]['mana'] += mana_gain
        print(f"{hero_name} recharged for {mana_gain} MP!")

    def heal(self, hero_name, heal_received):
        health_gain = heal_received
        if self.heroes[hero_name]['hp'] + health_gain > self.max_health:
            health_gain = self.max_health - self.heroes[hero_name]['hp']
            self.heroes[hero_name]['hp'] = self.max_health
        elif self.heroes[hero_name]['hp'] + health_gain <= self.max_health:
            self.heroes[hero_name]['hp'] += health_gain
        print(f"{hero_name} healed for {health_gain} HP!")


all_heroes = Heroes()
total_heroes = int(input())
for _ in range(total_heroes):
    name, hp, mp = [int(element) if element.isdigit() else element for element in input().split()]
    all_heroes.heroes[name] = all_heroes.heroes.get(name, {'hp': hp, 'mana': mp})

hero_operations = {
    'CastSpell': all_heroes.cast_spell,
    'TakeDamage': all_heroes.take_damage,
    'Recharge': all_heroes.recharge,
    'Heal': all_heroes.heal
}
command = input()
while command != "End":
    method, *data = [int(element) if element.isdigit() else element for element in command.split(" - ")]
    hero_operations[method](*data)
    command = input()
for key, value in all_heroes.heroes.items():
    print(f"{key}  \nHP: {value['hp']}\nMP: {value['mana']}")


# ########################################################################
# number_of_heroes = int(input())
# all_heroes = {}
#
# for every_hero in range(number_of_heroes):
#     hero_name, hp, mp = [string if string.isalpha() else int(string) for string in input().split()]
#     all_heroes[hero_name] = all_heroes.get(hero_name, {'hp': hp, 'mp': mp})
#
# command = input()
# while command != "End":
#     command = command.split(" - ")
#     event = command[0]
#     hero_name = command[1]
#
#     if event == "CastSpell":
#         mp_needed_to_cast, spell_name = int(command[2]), command[3]
#         if all_heroes[hero_name]['mp'] >= mp_needed_to_cast:
#             all_heroes[hero_name]['mp'] -= mp_needed_to_cast
#             print(f"{hero_name} has successfully cast {spell_name} and now has {all_heroes[hero_name]['mp']} MP!")
#         elif all_heroes[hero_name]['mp'] < mp_needed_to_cast:
#             print(f"{hero_name} does not have enough MP to cast {spell_name}!")
#
#     elif event == "TakeDamage":
#         damage_taken, attacker = int(command[2]), command[3]
#         if all_heroes[hero_name]['hp'] - damage_taken > 0:
#             all_heroes[hero_name]['hp'] -= damage_taken
#             print(f"{hero_name} was hit for {damage_taken} HP by {attacker} "
#                   f"and now has {all_heroes[hero_name]['hp']} HP left!")
#         elif all_heroes[hero_name]['hp'] - damage_taken <= 0:
#             del all_heroes[hero_name]
#             print(f"{hero_name} has been killed by {attacker}!")
#
#     elif event == "Recharge":
#         mp_recharge = int(command[2])
#         mana_gained = 0
#         if all_heroes[hero_name]['mp'] + mp_recharge >= 200:
#             mana_gained = 200 - all_heroes[hero_name]['mp']
#         elif all_heroes[hero_name]['mp'] + mp_recharge < 200:
#             mana_gained = mp_recharge
#         all_heroes[hero_name]['mp'] += mana_gained
#         print(f"{hero_name} recharged for {mana_gained} MP!")
#
#     elif event == "Heal":
#         amount_healed = int(command[2])
#         hp_gained = 0
#         if all_heroes[hero_name]['hp'] + amount_healed >= 100:
#             hp_gained = 100 - all_heroes[hero_name]['hp']
#         elif all_heroes[hero_name]['hp'] + amount_healed < 100:
#             hp_gained = amount_healed
#         all_heroes[hero_name]['hp'] += hp_gained
#         print(f"{hero_name} healed for {hp_gained} HP!")
#     command = input()
#
# for alive_heroes in all_heroes:
#     print(alive_heroes)
#     print(f" HP: {all_heroes[alive_heroes]['hp']}")
#     print(f" MP: {all_heroes[alive_heroes]['mp']}")
