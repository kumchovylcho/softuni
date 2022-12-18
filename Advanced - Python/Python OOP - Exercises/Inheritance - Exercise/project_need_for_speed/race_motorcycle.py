from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def drive(self, kilometers: int):
        if self.fuel >= kilometers * RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION:
            self.fuel -= kilometers * RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION
