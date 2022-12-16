class Flower:
    is_happy = False

    def __init__(self, name, water_requirements: int):
        self.name = name
        self.water_requirements = int(water_requirements)

    def water(self, water_amount):
        if water_amount >= self.water_requirements:
            Flower.is_happy = True

    def status(self):
        if Flower.is_happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"
