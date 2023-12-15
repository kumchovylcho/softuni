from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN = 540

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)

    def miss(self, time_to_catch: int):
        calculated_value = round(self.oxygen_level - (time_to_catch * 0.3))

        if calculated_value < 0:
            self.oxygen_level = 0

        elif calculated_value >= 0:
            self.oxygen_level = calculated_value

        if self.oxygen_level == 0:
            self.update_health_status()

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN