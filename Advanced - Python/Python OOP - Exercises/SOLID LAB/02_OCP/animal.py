from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abstractmethod
    def make_sound(self):
        pass


class Chicken(Animal):

    def make_sound(self):
        return "Cluck!"


class Dog(Animal):

    def make_sound(self):
        return "woof!"


class Cat(Animal):

    def make_sound(self):
        return "Meow!!!"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat('mammal'), Dog('mammal'), Chicken("mammal")]
animal_sound(animals)

