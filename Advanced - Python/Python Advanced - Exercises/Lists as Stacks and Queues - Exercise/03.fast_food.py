quantity_of_food = int(input())
food_orders = [int(order) for order in input().split()][::-1]
biggest_order = max(food_orders)
for index in range(len(food_orders) - 1, -1, -1):
    if quantity_of_food >= food_orders[index]:
        quantity_of_food -= food_orders[index]
        food_orders.pop()
    elif quantity_of_food < food_orders[index]:
        break
print(biggest_order)
if not food_orders:
    print("Orders complete")
elif food_orders:
    food_orders = [str(order) for order in food_orders][::-1]
    print(f"Orders left: {' '.join(food_orders)}")