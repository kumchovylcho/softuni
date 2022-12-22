from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def from_stars(stars_count: int):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def status(self):
        self.guests, free_rooms, taken_rooms = 0, [], []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(room.number)
                self.guests += room.guests
            elif not room.is_taken:
                free_rooms.append(room.number)
        output = [f"Hotel {self.name} has {self.guests} total guests",
                  f"Free rooms: {', '.join(str(x) for x in free_rooms)}",
                  f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}"]
        return '\n'.join(output)
