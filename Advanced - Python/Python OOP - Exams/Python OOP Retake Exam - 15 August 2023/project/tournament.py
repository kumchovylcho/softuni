import re

from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    def __init__(self,
                 name: str,
                 capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not list(re.finditer(r'^[a-zA-Z0-9]+$', value)):
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    @property
    def valid_equipments(self):
        return {"KneePad": KneePad,
                "ElbowPad": ElbowPad,
                }

    @property
    def valid_teams(self):
        return {"OutdoorTeam": OutdoorTeam,
                "IndoorTeam": IndoorTeam,
                }

    @staticmethod
    def find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

        return None

    @staticmethod
    def find_equipment_type(e_type: str, collection: list, only_last=True):
        found_equipments = []
        for obj in collection:
            if obj.__class__.__name__ == e_type:
                found_equipments.append(obj)

        if found_equipments:
            if only_last:
                return found_equipments[-1]

            return found_equipments

        return []

    def add_equipment(self, equipment_type: str):
        if not self.valid_equipments.get(equipment_type):
            raise Exception("Invalid equipment type!")

        self.equipment.append(self.valid_equipments[equipment_type]())

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if not self.valid_teams.get(team_type):
            raise Exception("Invalid team type!")

        if len(self.teams) + 1 > self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(self.valid_teams[team_type](name=team_name,
                                                      country=country,
                                                      advantage=advantage,
                                                      ))

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self.find_object(team_name, "name", self.teams)
        equipment = self.find_equipment_type(equipment_type, self.equipment)

        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")

        team.budget -= equipment.price
        self.equipment.remove(equipment)
        team.equipment.append(equipment)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.find_object(team_name, "name", self.teams)

        if not team:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)

        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipments = self.find_equipment_type(equipment_type, self.equipment, only_last=False)

        for equipment in equipments:
            equipment.increase_price()

        return f"Successfully changed {len(equipments)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = self.find_object(team_name1, "name", self.teams)
        team_2 = self.find_object(team_name2, "name", self.teams)

        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_1_points = sum(p.protection for p in team_1.equipment) + team_1.advantage
        team_2_points = sum(p.protection for p in team_2.equipment) + team_2.advantage

        winner = None
        if team_2_points > team_1_points:
            winner = team_2

        elif team_1_points > team_2_points:
            winner = team_1

        if winner:
            winner.win()
            return f"The winner is {winner.name}."

        return "No winner in this game."

    def get_statistics(self):
        result = [
            f"Tournament: {self.name}",
            f"Number of Teams: {len(self.teams)}",
            "Teams:",
        ]

        sorted_statistics = sorted(self.teams, key=lambda t: (-t.wins))

        for team in sorted_statistics:
            result.append(team.get_statistics())

        return "\n".join(result)
