from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    @staticmethod
    def find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)

        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pokemon = self.find_object(pokemon_name, "name", self.pokemons)

        if not pokemon:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

    def trainer_data(self):
        data = [f"Pokemon Trainer {self.name}",
                f"Pokemon count {len(self.pokemons)}"
                ]

        [data.append(f"- {x.pokemon_details()}") for x in self.pokemons]

        return '\n'.join(data)


# from project.pokemon import Pokemon
#
#
# class Trainer:
#
#     def __init__(self, name: str):
#         self.name = name
#         self.pokemons = []
#
#     def add_pokemon(self, pokemon: Pokemon):
#         if pokemon in self.pokemons:
#             return "This pokemon is already caught"
#         self.pokemons.append(pokemon)
#         return f"Caught {pokemon.pokemon_details()}"
#
#     def release_pokemon(self, pokemon_name: str):
#         for item in self.pokemons:
#             if item.name == pokemon_name:
#                 self.pokemons.remove(item)
#                 return f"You have released {pokemon_name}"
#         return "Pokemon is not caught"
#
#     def trainer_data(self):
#         output = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
#         for item in self.pokemons:
#             output.append(f"- {item.pokemon_details()}")
#         return '\n'.join(output)


# from project.pokemon import Pokemon
# # from pokemon import Pokemon
#
#
# class Trainer:
#
#     def __init__(self, name):
#         self.name = name
#         self.pokemons = []
#
#     def add_pokemon(self, current_pokemon: Pokemon):
#         if current_pokemon.name not in [x.name for x in self.pokemons]:
#             self.pokemons.append(current_pokemon)
#             return f"Caught {current_pokemon.pokemon_details()}"
#         return "This pokemon is already caught"
#
#     def release_pokemon(self, pokemon_name):
#         for item in self.pokemons:
#             if item.name == pokemon_name:
#                 self.pokemons.remove(item)
#                 return f"You have released {pokemon_name}"
#         return "Pokemon is not caught"
#
#     def trainer_data(self):
#         output = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
#         for item in self.pokemons:
#             output += f"- {item.pokemon_details()}"
#         return output
