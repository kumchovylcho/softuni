from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self):
        difficulty_level = ""

        if 1500 <= self.elevation <= 2500:
            difficulty_level = "Advanced"
        elif self.elevation > 2500:
            difficulty_level = "Extreme"

        return difficulty_level
