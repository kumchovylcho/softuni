from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    air_condition_consumption = 0.9

    def drive(self, distance):
        consumption = (self.fuel_consumption + self.air_condition_consumption) * distance
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    air_condition_consumption = 1.6

    def drive(self, distance):
        consumption = (self.fuel_consumption + self.air_condition_consumption) * distance
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


bmw = Car(60, 5)
print(bmw.fuel_quantity)
bmw.drive(10)
print(bmw.fuel_quantity)
