from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.missions = {"successful": 0,
                         "not successful": 0
                         }

    @property
    def astronaut_types(self):
        return {"Biologist": Biologist,
                "Geodesist": Geodesist,
                "Meteorologist": Meteorologist
                }

    def __find_astronaut_name(self, name: str):
        return self.astronaut_repository.find_by_name(name)

    def __find_planet_name(self, name: str):
        return self.planet_repository.find_by_name(name)

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.__find_astronaut_name(name):
            return f"{name} is already added."

        if astronaut_type not in self.astronaut_types:
            raise Exception("Astronaut type is not valid!")

        create_astronaut = self.astronaut_types[astronaut_type](name)
        self.astronaut_repository.add(create_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.__find_planet_name(name):
            return f"{name} is already added."

        create_planet = Planet(name)
        create_planet.items += items.split(", ")
        self.planet_repository.add(create_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut_object = self.__find_astronaut_name(name)
        if not astronaut_object:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut_object)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.__find_planet_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        astronauts = [a for a in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)]
        if all(a.oxygen <= 30 for a in astronauts):
            raise Exception("You need at least one astronaut to explore the planet!")

        top_five_astronauts = astronauts[:5]
        for astro in top_five_astronauts:
            while astro.oxygen > 0 and planet.items:
                astro.backpack.append(planet.items.pop())
                astro.breathe()

        if planet.items:
            self.missions["not successful"] += 1
            return "Mission is not completed."

        self.missions["successful"] += 1
        return f"Planet: {planet_name} was explored. {len([a for a in top_five_astronauts if a.backpack])}" \
               f" astronauts participated in collecting items."

    def report(self):
        output = [f"{self.missions['successful']} successful missions!",
                  f"{self.missions['not successful']} missions were not completed!",
                  "Astronauts' info:",
                  ]

        for astro in self.astronaut_repository.astronauts:
            output.append(f"Name: {astro.name}")
            output.append(f"Oxygen: {astro.oxygen}")

            if astro.backpack:
                output.append(f"Backpack items: {', '.join(astro.backpack)}")
            elif not astro.backpack:
                output.append(f"Backpack items: none")

        return '\n'.join(output)
