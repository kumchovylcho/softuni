from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        # Use None because "JUDGE"
        difficulty_level = None

        if 2000 <= self.elevation <= 3000:
            difficulty_level = "Advanced"
        elif self.elevation > 3000:
            difficulty_level = "Extreme"

        return difficulty_level
