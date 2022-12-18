from project.food import Food


class Fruit(Food):

    def __init__(self, name: str, expiration_date: str):
        self.name = name
        self.expiration_date = expiration_date
