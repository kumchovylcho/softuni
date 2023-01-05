class Shop:

    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, 10)

    def add_item(self, item_name: str):
        if item_name in self.items and self.items[item_name] >= self.capacity:
            return "Not enough capacity in the shop"
        self.items[item_name] = self.items.get(item_name, 0) + 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            if self.items[item_name] <= 0:
                self.items.pop(item_name)
            return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


# class Shop:
#
#     def __init__(self, name: str, type: str, capacity: int):
#         self.name = name
#         self.type = type
#         self.capacity = int(capacity)
#         self.items = {}
#
#     @staticmethod
#     def small_shop(name: str, type: str):
#         return Shop(name, type, 10)
#
#     def add_item(self, item_name: str):
#         if sum(self.items.values()) < self.capacity:
#             self.items[item_name] = self.items.get(item_name, 0) + 1
#             return f"{item_name} added to the shop"
#         return "Not enough capacity in the shop"
#
#     def remove_item(self, item_name: str, amount: int):
#         if item_name not in self.items or self.items[item_name] - amount < 0:
#             return f"Cannot remove {amount} {item_name}"
#         self.items[item_name] -= amount
#         if self.items[item_name] <= 0:
#             del self.items[item_name]
#         return f"{amount} {item_name} removed from the shop"
#
#     def __repr__(self):
#         return f"{self.name} of type {self.type} with capacity {self.capacity}"
