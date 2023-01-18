from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):

    def __init__(self):
        super().__init__(comfort=5, price=10)
