from abc import ABC, abstractmethod


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(x.comfort for x in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {type(fish).__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        if decoration not in self.decorations:
            self.decorations.append(decoration)

    def feed(self):
        for x in self.fish:
            x.eat()

    def __str__(self):
        result = [f"{self.name}:",
                  f"Fish: {' '.join(f.name for f in self.fish) if self.fish else 'none'}",
                  f"Decorations: {len(self.decorations)}",
                  f"Comfort: {self.calculate_comfort()}"]
        return '\n'.join(result)
