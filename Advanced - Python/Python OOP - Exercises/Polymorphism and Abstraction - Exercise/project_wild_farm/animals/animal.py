from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, weight: float, food_eaten=0):
        self.food_that_eats = None
        self.name = name
        self.weight = float(weight)
        self.food_eaten = food_eaten
        self.weight_increase_per_piece = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        if type(food) not in self.food_that_eats:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * self.weight_increase_per_piece
        self.food_eaten += food.quantity


class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
