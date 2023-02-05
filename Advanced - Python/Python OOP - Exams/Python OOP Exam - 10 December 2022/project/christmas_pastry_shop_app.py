from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    @property
    def __get_delicacy_types(self):
        return {"Gingerbread": Gingerbread, "Stolen": Stolen}

    @property
    def __get_booth_types(self):
        return {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    @staticmethod
    def __find_object(item: str or int, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def __find_free_booth_with_enough_capacity(self, number_of_people: int):
        return [x for x in self.booths if not x.is_reserved and x.capacity >= number_of_people]

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy_name = self.__find_object(name, "name", self.delicacies)

        if delicacy_name:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.__get_delicacy_types:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(self.__get_delicacy_types[type_delicacy](name, price))

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        find_booth_number = self.__find_object(booth_number, "booth_number", self.booths)

        if find_booth_number:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.__get_booth_types:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(self.__get_booth_types[type_booth](booth_number, capacity))

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        find_booth = self.__find_free_booth_with_enough_capacity(number_of_people)

        if not find_booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        get_first_booth = find_booth[0]

        get_first_booth.reserve(number_of_people)

        return f"Booth {get_first_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        find_booth_number = self.__find_object(booth_number, "booth_number", self.booths)
        find_delicacy_name = self.__find_object(delicacy_name, "name", self.delicacies)

        if not find_booth_number:
            raise Exception(f"Could not find booth {booth_number}!")

        if not find_delicacy_name:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        find_booth_number.delicacy_orders.append(find_delicacy_name)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_object(booth_number, "booth_number", self.booths)

        bill = booth.price_for_reservation + sum(x.price for x in booth.delicacy_orders)
        self.income += bill

        booth.is_reserved = False
        booth.price_for_reservation = 0
        booth.delicacy_orders = []

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())
