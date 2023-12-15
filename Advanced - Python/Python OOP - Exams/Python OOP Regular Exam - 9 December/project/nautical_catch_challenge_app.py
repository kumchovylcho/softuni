from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers = []
        self.fish_list = []

    @property
    def valid_divers(self):
        return {
            "FreeDiver": FreeDiver,
            "ScubaDiver": ScubaDiver
        }

    @property
    def valid_fishes(self):
        return {
            "DeepSeaFish": DeepSeaFish,
            "PredatoryFish": PredatoryFish
        }

    @staticmethod
    def get_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

        return None

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.valid_divers:
            return f"{diver_type} is not allowed in our competition."

        diver = self.get_object(diver_name, "name", self.divers)
        if diver:
            return f"{diver_name} is already a participant."

        diver = self.valid_divers[diver_type](diver_name)
        self.divers.append(diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.valid_fishes:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self.get_object(fish_name, "name", self.fish_list)
        if fish:
            return f"{fish_name} is already permitted."

        fish = self.valid_fishes[fish_type](fish_name, points)
        self.fish_list.append(fish)

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.get_object(diver_name, "name", self.divers)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = self.get_object(fish_name, "name", self.fish_list)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            elif not is_lucky:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_recovered = 0
        for diver in self.divers:
            if not diver.has_health_issue:
                continue

            diver.update_health_status()
            diver.renew_oxy()
            divers_recovered += 1

        return f"Divers recovered: {divers_recovered}"

    def diver_catch_report(self, diver_name: str):
        diver = self.get_object(diver_name, "name", self.divers)

        output = [f"**{diver_name} Catch Report**", ]
        for fish in diver.catch:
            output.append(fish.fish_details())

        return "\n".join(output)

    def competition_statistics(self):
        output = ["**Nautical Catch Challenge Statistics**", ]

        sorted_divers = sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        for diver in sorted_divers:
            if diver.has_health_issue:
                continue

            output.append(diver.__str__())

        return "\n".join(output)
