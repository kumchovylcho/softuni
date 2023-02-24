class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, animal):
        get_species = {"mammal": self.mammals, "fish": self.fishes, "bird": self.birds}
        if species in get_species:
            get_species[species].append(animal)

        self.__animals += 1

    def get_info(self, species):
        species_representation = {"mammal": "Mammals", "fish": "Fishes", "bird": "Birds"}
        get_species = {"mammal": self.mammals, "fish": self.fishes, "bird": self.birds}

        if species in species_representation:
            return f"{species_representation[species]} in {self.name}: {', '.join(get_species[species])}\n" \
                   f"Total animals: {self.__animals}"


# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     @property
#     def get_species(self):
#         return {"mammal": self.mammals,
#                 "fish": self.fishes,
#                 "bird": self.birds
#                 }
#
#     @property
#     def species_representation(self):
#         return {"mammal": "Mammals",
#                 "fish": "Fishes",
#                 "bird": "Birds"
#                 }
#
#     def add_animal(self, species, animal):
#         if species in self.get_species:
#             self.get_species[species].append(animal)
#
#         self.__animals += 1
#
#     def get_info(self, species):
#         return f"{self.species_representation[species]} in {self.name}: {', '.join(self.get_species[species])}\nTotal animals: {self.__animals}"


zoo_name = input()
num = int(input())
zoo = Zoo(zoo_name)

for _ in range(num):
    type_animal, animal = input().split()
    zoo.add_animal(type_animal, animal)

print(zoo.get_info(input()))


# class Zoo:
#     __animals = 0
#
#     def __init__(self, zoo_name):
#         self.name = zoo_name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ""
#         if species == "mammal":
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == "fish":
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
#         elif species == "bird":
#             result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
#
#         result += f"Total animals: {Zoo.__animals}"
#         return result
#
#
# name_of_zoo = input()
# zoo = Zoo(name_of_zoo)
# number_of_animals = int(input())
#
# for count_of_animal in range(number_of_animals):
#     current_animal = input().split()
#     specie = current_animal[0]
#     name = current_animal[1]
#     zoo.add_animal(specie, name)
#
# info = input()
# print(zoo.get_info(info))
