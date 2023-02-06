from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    @property
    def __valid_musicians(self):
        return {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    @property
    def __needed_skills_for_musicians(self):
        return {"Rock": {"Drummer": ["play the drums with drumsticks"],
                         "Singer": ["sing high pitch notes"],
                         "Guitarist": ["play rock"]},
                "Metal": {"Drummer": ["play the drums with drumsticks"],
                          "Singer": ["sing low pitch notes"],
                          "Guitarist": ["play metal"]},
                "Jazz": {"Drummer": ["play the drums with drum brushes"],
                         "Singer": ["sing high pitch notes", "sing low pitch notes"],
                         "Guitarist": ["play jazz"]},
                }

    @staticmethod
    def __find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.__valid_musicians:
            raise ValueError("Invalid musician type!")

        find_musician_name = self.__find_object(name, "name", self.musicians)
        if find_musician_name:
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(self.__valid_musicians[musician_type](name, age))

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        find_band_name = self.__find_object(name, "name", self.bands)
        if find_band_name:
            raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        find_concert_by_place = self.__find_object(place, "place", self.concerts)
        if find_concert_by_place:
            if find_concert_by_place.place in [x.place for x in self.concerts]:
                raise Exception(f"{place} is already registered for {find_concert_by_place.genre} concert!")

        create_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(create_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        find_musician_by_name = self.__find_object(musician_name, "name", self.musicians)
        find_band_by_name = self.__find_object(band_name, "name", self.bands)

        if not find_musician_by_name:
            raise Exception(f"{musician_name} isn't a musician!")

        if not find_band_by_name:
            raise Exception(f"{band_name} isn't a band!")

        find_band_by_name.members.append(find_musician_by_name)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        find_band_by_name = self.__find_object(band_name, "name", self.bands)

        if not find_band_by_name:
            raise Exception(f"{band_name} isn't a band!")

        find_musician_by_name = self.__find_object(musician_name, "name", find_band_by_name.members)

        if not find_musician_by_name:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        find_band_by_name.members.remove(find_musician_by_name)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.__find_object(band_name, "name", self.bands)
        concert = self.__find_object(concert_place, "place", self.concerts)

        check_diff_band_members = {x.__class__.__name__ for x in band.members}

        if len(check_diff_band_members) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        all_musicians = []
        for musician, skills in self.__needed_skills_for_musicians[concert.genre].items():
            for band_musician in band.members:
                if band_musician.__class__.__name__ == musician and \
                        all(skill in band_musician.skills for skill in skills):
                    all_musicians.append(band_musician)

        if len(all_musicians) != len(band.members):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."


musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))

print(app.create_band("RockName"))
for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))

print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))
