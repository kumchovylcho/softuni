from project.booths.booth import Booth


class PrivateBooth(Booth):

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        if self.capacity >= number_of_people and not self.is_reserved:
            self.price_for_reservation = number_of_people * 3.5
            self.is_reserved = True
