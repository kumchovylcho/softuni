class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = int(capacity)
        self.items = []
        self.capacity_left = 0

    def add_item(self, item: str):
        if self.__capacity > self.capacity_left:
            self.items.append(item)
            self.capacity_left += 1
        elif self.capacity_left >= self.__capacity:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {Inventory.get_capacity(self) - self.capacity_left}"


