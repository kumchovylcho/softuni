from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def drive(self, kilometers: int):
        if self.fuel >= kilometers * Motorcycle.DEFAULT_FUEL_CONSUMPTION:
            self.fuel -= kilometers * Motorcycle.DEFAULT_FUEL_CONSUMPTION
