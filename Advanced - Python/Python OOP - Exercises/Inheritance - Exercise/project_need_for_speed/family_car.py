from project.car import Car


class FamilyCar(Car):

    def drive(self, kilometers: int):
        if self.fuel >= kilometers * Car.DEFAULT_FUEL_CONSUMPTION:
            self.fuel -= kilometers * Car.DEFAULT_FUEL_CONSUMPTION
