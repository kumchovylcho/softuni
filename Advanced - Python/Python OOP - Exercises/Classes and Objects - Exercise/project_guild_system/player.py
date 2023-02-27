class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost

        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = [f"Name: {self.name}",
                  f"Guild: {self.guild}",
                  f"HP: {self.hp}",
                  f"MP: {self.mp}"
                  ]

        [result.append(f"==={skill} - {mana_cost}") for skill, mana_cost in self.skills.items()]

        return '\n'.join(result)


# class Player:
#
#     def __init__(self, name: str, hp: int, mp: int):
#         self.name = name
#         self.hp = int(hp)
#         self.mp = int(mp)
#         self.skills = {}
#         self.guild = "Unaffiliated"
#
#     def add_skill(self, skill_name: str, mana_cost: int):
#         if skill_name in self.skills:
#             return "Skill already added"
#         self.skills[skill_name] = mana_cost
#         return f"Skill {skill_name} added to the collection of the player {self.name}"
#
#     def player_info(self):
#         output = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
#         for key, value in self.skills.items():
#             output.append(f"==={key} - {value}")
#         return '\n'.join(output)


# class Player:
#
#     def __init__(self, name: str, hp: int, mp: int):
#         self.name = name
#         self.hp = int(hp)
#         self.mp = int(mp)
#         self.skills = {}
#         self.guild = "Unaffiliated"
#
#     def add_skill(self, skill_name: str, mana_cost: int):
#         if skill_name not in self.skills:
#             self.skills[skill_name] = int(mana_cost)
#             return f"Skill {skill_name} added to the collection of the player {self.name}"
#         return f"Skill already added"
#
#     def player_info(self):
#         output = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
#         for key, value in self.skills.items():
#             output += f"==={key} - {value}\n"
#         return output

