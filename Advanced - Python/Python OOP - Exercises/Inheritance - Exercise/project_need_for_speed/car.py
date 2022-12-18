from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def drive(self, kilometers: int):
        if self.fuel >= kilometers * Car.DEFAULT_FUEL_CONSUMPTION:
            self.fuel -= kilometers * Car.DEFAULT_FUEL_CONSUMPTION
