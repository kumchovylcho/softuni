class Shop:

    def __init__(self, pile_of_clothes: list, capacity_for_one_rack: int):
        self.pile_of_clothes = pile_of_clothes
        self.racks_needed = 1
        self.capacity_for_one_rack = capacity_for_one_rack
        self.current_rack = 0

    def check_for_remaining_clothes(self):
        return True if self.pile_of_clothes else False

    def check_reached_capacity(self):
        if self.current_rack == self.capacity_for_one_rack and self.check_for_remaining_clothes():
            return True

    def check_current_rack_greater_capacity(self):
        if self.current_rack > self.capacity_for_one_rack:
            return True

    def take_cloth(self):
        return self.pile_of_clothes.pop()

    def add_cloth_to_current_rack(self, cloth: int):
        self.current_rack += cloth

    def add_new_rack_and_reset_current_rack(self):
        self.current_rack = 0
        self.racks_needed += 1


box_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
fashion_boutique = Shop(box_of_clothes, rack_capacity)

while fashion_boutique.pile_of_clothes:
    current_cloth = fashion_boutique.take_cloth()
    fashion_boutique.add_cloth_to_current_rack(current_cloth)

    if fashion_boutique.check_reached_capacity():
        fashion_boutique.add_new_rack_and_reset_current_rack()

    elif fashion_boutique.check_current_rack_greater_capacity():
        fashion_boutique.add_new_rack_and_reset_current_rack()
        fashion_boutique.add_cloth_to_current_rack(current_cloth)

print(fashion_boutique.racks_needed)


# clothes = [int(number) for number in input().split()]
# rack_capacity = int(input())
# racks = []
# racks_counter = 0
# for cloth in range(len(clothes) - 1, -1, -1):
#     current_cloth = clothes.pop()
#     racks.append(current_cloth)
#     if sum(racks) == rack_capacity:
#         if clothes:
#             racks = []
#             racks_counter += 1
#     elif sum(racks) > rack_capacity:
#         racks = [current_cloth]
#         racks_counter += 1
# if racks:
#     racks_counter += 1
#
# print(racks_counter)
