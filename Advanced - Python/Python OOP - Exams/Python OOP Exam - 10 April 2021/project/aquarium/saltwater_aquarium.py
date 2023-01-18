from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):

    def __init__(self, name: str):
        super().__init__(name, capacity=25)