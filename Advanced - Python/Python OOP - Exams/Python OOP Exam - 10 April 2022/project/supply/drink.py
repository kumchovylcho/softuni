from project.supply.supply import Supply


class Drink(Supply):

    def __init__(self, name: str, energy=15):
        super().__init__(name, energy)

    def details(self):
        return f"{Drink.__name__}: {self.name}, {self.energy}"
