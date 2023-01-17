from project.people.child import Child
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.room_cost
            total_consumption += room.expenses
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result, rooms_to_remove = [], []
        for room in self.rooms:
            if room.room_cost + room.expenses > room.budget:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                rooms_to_remove.append(self.rooms.index(room))
                continue
            room.budget -= room.expenses + room.room_cost
            result.append(f"{room.family_name} paid"
                          f" {room.expenses + room.room_cost:.2f}$"
                          f" and have {room.budget:.2f}$ left.")
        if rooms_to_remove:
            for _ in range(len(self.rooms) - 1, -1, -1):
                self.rooms.pop(rooms_to_remove.pop())
        return '\n'.join(result)

    def status(self):
        result = []
        total_population = sum(people.members_count for people in self.rooms)
        result.append(f"Total population: {total_population}")
        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members."
                          f" Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            for kid, info in enumerate(room.children, 1):
                result.append(f"--- Child {kid} monthly cost: {info.get_monthly_expense():.2f}$")
            result.append(f"--- Appliances monthly cost: {sum(r.get_monthly_expense() for r in room.appliances):.2f}$")
        return '\n'.join(result)


# everland = Everland()
#
# def test_one():
#     young_couple = YoungCouple("Johnsons", 150, 205)
#
#     child1 = Child(5, 1, 2, 1)
#     child2 = Child(3, 2)
#     young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
#     everland.add_room(young_couple)
#     everland.add_room(young_couple_with_children)
#
#     print(everland.get_monthly_consumptions())
#     print(everland.pay())
#     print(everland.status())
#
#
# if __name__ == "__main__":
#     test_one()
