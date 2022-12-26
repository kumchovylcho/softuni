class Flower:

    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = int(water_requirements)
        self.is_happy = False

    def water(self, water_quantity: int):
        if water_quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"


# class Flower:
#     is_happy = False
#
#     def __init__(self, name, water_requirements: int):
#         self.name = name
#         self.water_requirements = int(water_requirements)
#
#     def water(self, water_amount):
#         if water_amount >= self.water_requirements:
#             Flower.is_happy = True
#
#     def status(self):
#         if Flower.is_happy:
#             return f"{self.name} is happy"
#         return f"{self.name} is not happy"
