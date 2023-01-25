from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > Thoroughbred.MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        if self.speed + 3 > Thoroughbred.MAX_SPEED:
            self.speed = Thoroughbred.MAX_SPEED
        else:
            self.speed += 3
