number_of_loads_to_transport = int(input())
price = 0
microbus = 0
truck = 0
train = 0
all_tons = 0
for load in range(1, number_of_loads_to_transport + 1):
    tons_of_the_load = int(input())
    if tons_of_the_load <= 3:
        price += 200 * tons_of_the_load
        microbus += tons_of_the_load
    elif 4 <= tons_of_the_load <= 11:
        price += 175 * tons_of_the_load
        truck += tons_of_the_load
    else:
        price += 120 * tons_of_the_load
        train += tons_of_the_load
    all_tons += tons_of_the_load
average_price = price / all_tons
microbus_percentage = microbus / all_tons * 100
truck_percentage = truck / all_tons * 100
train_percentage = train / all_tons * 100
print(f"{average_price:.2f}")
print(f"{microbus_percentage:.2f}%")
print(f"{truck_percentage:.2f}%")
print(f"{train_percentage:.2f}%")
