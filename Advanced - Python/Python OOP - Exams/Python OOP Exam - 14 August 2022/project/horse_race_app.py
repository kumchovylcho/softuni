from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    @property
    def valid_horses(self):
        return {
            "Appaloosa": Appaloosa,
            "Thoroughbred": Thoroughbred
            }

    def __find_horse_race_type(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race

    def __find_horse_name(self, name: str):
        for horse in self.horses:
            if horse.name == name:
                return horse

    def __find_jockey_name(self, name: str):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey

    def __find_horse_by_type_and_look_for_not_taken_one(self, horse_type: str):
        return [x for x in self.horses if x.__class__.__name__ == horse_type and not x.is_taken]

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = self.__find_horse_name(horse_name)
        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.valid_horses:
            create_horse = self.valid_horses[horse_type](horse_name, horse_speed)
            self.horses.append(create_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = self.__find_jockey_name(jockey_name)
        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        create_jockey = Jockey(jockey_name, age)
        self.jockeys.append(create_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race = self.__find_horse_race_type(race_type)
        if race:
            raise Exception(f"Race {race_type} has been already created!")

        create_race = HorseRace(race_type)
        self.horse_races.append(create_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_name(jockey_name)
        horse = self.__find_horse_by_type_and_look_for_not_taken_one(horse_type)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse_to_be_added = horse[-1]
        jockey.horse = horse_to_be_added
        jockey.horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse_to_be_added.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_horse_race_type(race_type)
        jockey = self.__find_jockey_name(jockey_name)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_horse_race_type(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        fastest_jockey = [x for x in sorted(race.jockeys, key=lambda x: -x.horse.speed)][0]

        return f"The winner of the {race_type} race, with a speed of {fastest_jockey.horse.speed}km/h is" \
               f" {fastest_jockey.name}! Winner's horse: {fastest_jockey.horse.name}."
