from project.vehicle import Vehicle


class Motorcycle(Vehicle):

    def drive(self, kilometers: int):
        if self.fuel >= kilometers * Vehicle.DEFAULT_FUEL_CONSUMPTION:
            self.fuel -= kilometers * Vehicle.DEFAULT_FUEL_CONSUMPTION
