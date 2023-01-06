from project.food import Meat, Vegetable, Fruit, Seed
from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_that_eats = [Vegetable, Fruit]
        self.weight_increase_per_piece = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_that_eats = [Meat]
        self.weight_increase_per_piece = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_that_eats = [Vegetable, Meat]
        self.weight_increase_per_piece = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_that_eats = [Meat]
        self.weight_increase_per_piece = 1.00

    def make_sound(self):
        return "ROAR!!!"
