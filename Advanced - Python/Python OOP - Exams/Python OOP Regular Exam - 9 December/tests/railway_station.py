from collections import deque


class RailwayStation:
    def __init__(self, name: str):
        self.name = name
        self.arrival_trains = deque()
        self.departure_trains = deque()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 3:
            raise ValueError("Name should be more than 3 symbols!")
        self.__name = value

    def new_arrival_on_board(self, train_info: str):
        self.arrival_trains.append(train_info)

    def train_has_arrived(self, train_info: str):
        if self.arrival_trains and self.arrival_trains[0] != train_info:
            return f"There are other trains to arrive before {train_info}."

        self.departure_trains.append(self.arrival_trains.popleft())
        return f"{train_info} is on the platform and will leave in 5 minutes."

    def train_has_left(self, train_info: str):
        if self.departure_trains and self.departure_trains[0] == train_info:
            self.departure_trains.popleft()
            return True
        return False
