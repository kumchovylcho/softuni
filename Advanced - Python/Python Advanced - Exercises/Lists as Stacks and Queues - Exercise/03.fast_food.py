from collections import deque


class FastFood:

    def __init__(self, daily_food: int, food_orders: list):
        self.daily_food = daily_food
        self.food_orders = deque(food_orders)

    def check_if_order_can_be_completed(self):
        return True if self.food_orders[0] <= self.daily_food else False

    def remove_order(self):
        self.daily_food -= self.food_orders.popleft()


food_limit = int(input())
orders = [int(x) for x in input().split()]

food_shop = FastFood(food_limit, orders)
print(max(food_shop.food_orders))
while food_shop.daily_food and food_shop.food_orders:
    if food_shop.check_if_order_can_be_completed():
        food_shop.remove_order()
        continue
    break
if not food_shop.food_orders:
    print("Orders complete")
if food_shop.food_orders:
    print(f"Orders left: {' '.join(str(x) for x in food_shop.food_orders)}")


# quantity_of_food = int(input())
# food_orders = [int(order) for order in input().split()][::-1]
# biggest_order = max(food_orders)
# for index in range(len(food_orders) - 1, -1, -1):
#     if quantity_of_food >= food_orders[index]:
#         quantity_of_food -= food_orders[index]
#         food_orders.pop()
#     elif quantity_of_food < food_orders[index]:
#         break
# print(biggest_order)
# if not food_orders:
#     print("Orders complete")
# elif food_orders:
#     food_orders = [str(order) for order in food_orders][::-1]
#     print(f"Orders left: {' '.join(food_orders)}")
