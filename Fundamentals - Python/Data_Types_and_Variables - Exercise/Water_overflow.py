times_to_add_water = int(input())
capacity = 255
current_water_level = 0
for water in range(times_to_add_water):
    add_water = int(input())
    current_water_level += add_water
    if current_water_level > capacity:
        current_water_level -= add_water
        print("Insufficient capacity!")
print(current_water_level)
