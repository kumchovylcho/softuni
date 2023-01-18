from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_aquariums = {
            "FreshwaterAquarium": FreshwaterAquarium,
            "SaltwaterAquarium": SaltwaterAquarium
        }
        if aquarium_type not in valid_aquariums:
            return "Invalid aquarium type."
        self.aquariums.append(valid_aquariums[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        valid_decorations = {
            "Ornament": Ornament,
            "Plant": Plant
        }
        if decoration_type not in valid_decorations:
            return "Invalid decoration type."
        create_object = valid_decorations[decoration_type]()
        self.decorations_repository.add(create_object)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."
        if aquarium:
            aquarium = aquarium[0]
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_types = {
            "FreshwaterFish": FreshwaterFish,
            "SaltwaterFish": SaltwaterFish
        }
        if fish_type not in valid_types:
            return f"There isn't a fish of type {fish_type}."
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        if aquarium:
            aquarium = aquarium[0]
            if aquarium.capacity == len(aquarium.fish):
                return "Not enough capacity."
            if fish_type[:-4] not in type(aquarium).__name__:
                return "Water not suitable."
            create_fish = valid_types[fish_type](fish_name, fish_species, price)
            aquarium.add_fish(create_fish)
            return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        if aquarium:
            aquarium = aquarium[0]
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        if aquarium:
            aquarium = aquarium[0]
            fish_price = sum(x.price for x in aquarium.fish)
            decorations_price = sum(x.price for x in aquarium.decorations)
            return f"The value of Aquarium {aquarium_name} is {fish_price + decorations_price:.2f}."

    def report(self):
        result = []
        [result.append(str(x)) for x in self.aquariums]
        return '\n'.join(result)
