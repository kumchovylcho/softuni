from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = []
        self.peaks = []

    @property
    def valid_climbers(self):
        return {
            "ArcticClimber": ArcticClimber,
            "SummitClimber": SummitClimber
        }

    @property
    def valid_peaks(self):
        return {
            "ArcticPeak": ArcticPeak,
            "SummitPeak": SummitPeak
        }

    @staticmethod
    def get_object(search_value: str, attribute: str, search_collection: list):
        for obj in search_collection:
            if getattr(obj, attribute) == search_value:
                return obj

        return None

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.valid_climbers:
            return f"{climber_type} doesn't exist in our register."

        climber = self.get_object(climber_name, "name", self.climbers)
        if climber:
            return f"{climber_name} has been already registered."

        new_climber = self.valid_climbers[climber_type](climber_name)
        self.climbers.append(new_climber)

        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.valid_peaks:
            return f"{peak_type} is an unknown type of peak."

        new_peak = self.valid_peaks[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        peak = self.get_object(peak_name, "name", self.peaks)
        climber = self.get_object(climber_name, "name", self.climbers)

        peak_items = set(peak.get_recommended_gear())
        climber_items_difference = peak_items.difference(set(gear))

        if len(climber_items_difference):
            climber.is_prepared = False
            sorted_missing_items = sorted(climber_items_difference)
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted_missing_items)}."

        return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self.get_object(climber_name, "name", self.climbers)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = self.get_object(peak_name, "name", self.peaks)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)
        peak.is_conquered = True

        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        conquered_peak_climbers = [c for c in self.climbers if len(c.conquered_peaks)]
        sorted_climbers = sorted(conquered_peak_climbers, key=lambda c: (-len(c.conquered_peaks), c.name))

        total_climbed_peaks = len([p for p in self.peaks if p.is_conquered])
        output = [
            f"Total climbed peaks: {total_climbed_peaks}",
            "**Climber's statistics:**",
        ]

        for climber in sorted_climbers:
            output.append(climber.__str__())

        return "\n".join(output)



# Create an instance of SummitQuestManagerApp
climbing_app = SummitQuestManagerApp()

# Register climbers
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Bob"))
print(climbing_app.register_climber("ExtremeClimber", "Dave"))
print(climbing_app.register_climber("ArcticClimber", "Charlie"))
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Eve"))
print(climbing_app.register_climber("SummitClimber", "Frank"))

# Add peaks to the wish list
print(climbing_app.peak_wish_list("ArcticPeak", "MountEverest", 4000))
print(climbing_app.peak_wish_list("SummitPeak", "K2", 3000))
print(climbing_app.peak_wish_list("ArcticPeak", "Denali", 2500))
print(climbing_app.peak_wish_list("UnchartedPeak", "MysteryMountain", 2000))

# Prepare climbers for climbing
print(climbing_app.check_gear("Alice", "MountEverest", ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]))
print(climbing_app.check_gear("Bob", "K2", ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]))
print(climbing_app.check_gear("Charlie", "Denali", ["Ice axe", "Crampons"]))

# Perform climbing
print(climbing_app.perform_climbing("Alice", "MountEverest"))
print(climbing_app.perform_climbing("Bob", "K2"))
print(climbing_app.perform_climbing("Kelly", "Denali"))
print(climbing_app.perform_climbing("Alice", "K2"))
print(climbing_app.perform_climbing("Alice", "MysteryMountain"))
print(climbing_app.perform_climbing("Eve", "MountEverest"))
print(climbing_app.perform_climbing("Charlie", "MountEverest"))
print(climbing_app.perform_climbing("Frank", "K2"))
print(climbing_app.perform_climbing("Frank", "Denali"))
print(climbing_app.perform_climbing("Frank", "MountEverest"))

# Get statistics
print(climbing_app.get_statistics())
