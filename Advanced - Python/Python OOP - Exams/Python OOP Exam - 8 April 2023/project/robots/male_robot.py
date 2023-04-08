from project_oop.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.initial_weight)

    @property
    def initial_weight(self):
        return 9

    def eating(self):
        self.weight += 3