from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def drive(self, kilometers: int):
        if self.fuel >= kilometers * SportCar.DEFAULT_FUEL_CONSUMPTION:
            self.fuel -= kilometers * SportCar.DEFAULT_FUEL_CONSUMPTION
