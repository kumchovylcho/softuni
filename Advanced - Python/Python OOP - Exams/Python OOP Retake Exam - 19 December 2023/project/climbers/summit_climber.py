from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 150)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        difficulty_multiplier = 2.5 if peak.difficulty_level == "Extreme" else 1.3
        self.strength -= 30 * difficulty_multiplier
        self.conquered_peaks.append(peak.name)