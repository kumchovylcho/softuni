from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 200)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak: BasePeak):
        difficulty_multiplier = 2.0 if peak.difficulty_level == "Extreme" else 1.5
        self.strength -= 20 * difficulty_multiplier
        self.conquered_peaks.append(peak.name)
