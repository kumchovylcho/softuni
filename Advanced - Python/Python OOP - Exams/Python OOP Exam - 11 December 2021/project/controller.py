from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    @property
    def get_valid_cars(self):
        return {
            "MuscleCar": MuscleCar,
            "SportsCar": SportsCar
            }

    def __find_car_model(self, car_model: str):
        for car in self.cars:
            if car.model == car_model:
                return car

    def __find_driver_name(self, name: str):
        for driver in self.drivers:
            if driver.name == name:
                return driver

    def __find_race_name(self, name: str):
        for race in self.races:
            if race.name == name:
                return race

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if self.__find_car_model(model):
            raise Exception(f"Car {model} is already created!")

        if car_type in self.get_valid_cars:
            self.cars.append(self.get_valid_cars[car_type](model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.__find_driver_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.__find_race_name(race_name):
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if all(car_type == type(x).__name__ and x.is_taken for x in self.cars) or \
                all(car_type != x.__class__.__name__ for x in self.cars):
            raise Exception(f"Car {car_type} could not be found!")

        free_cars = [c for c in self.cars if not c.is_taken and type(c).__name__ == car_type]
        if driver.car and free_cars:
            current_car = free_cars[-1]

            old_car = driver.car
            old_car.is_taken = False

            driver.car = current_car
            current_car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {driver.car.model}."

        if not driver.car and free_cars:
            current_car = free_cars[-1]

            driver.car = current_car
            driver.car.is_taken = True

            return f"Driver {driver_name} chose the car {driver.car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_name(race_name)
        driver = self.__find_driver_name(driver_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_3 = []
        for driver in sorted(race.drivers, key=lambda x: -x.car.speed_limit)[:3]:
            fastest_3.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
            driver.number_of_wins += 1

        return '\n'.join(fastest_3)


controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in controller.drivers]
