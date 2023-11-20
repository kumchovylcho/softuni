from collections import deque

get_list_of_integers = lambda input_value: [int(x) for x in input_value.split()]

initial_fuel = get_list_of_integers(input())
consumption_index = deque(get_list_of_integers(input()))
fuel_needed = deque(get_list_of_integers(input()))

while initial_fuel and consumption_index and fuel_needed:
    fuel_quantity = initial_fuel.pop()
    consumption = consumption_index.popleft()
    current_fuel = fuel_needed.popleft()

    is_altitude_reached = (fuel_quantity - consumption) >= current_fuel
    if not is_altitude_reached:
        print(f"John did not reach: Altitude {4 - len(fuel_needed)}")
        fuel_needed.appendleft(current_fuel)
        break

    print(f"John has reached: Altitude {4 - len(fuel_needed)}")

if 0 <= len(initial_fuel) < 4 and 0 < len(fuel_needed) < 4:
    altitudes = []
    for i in range(1, 4 - len(fuel_needed) + 1):
        altitudes.append(f"Altitude {i}")

    print("John failed to reach the top.")
    print(f"Reached altitudes:", ", ".join(altitudes))

if len(fuel_needed) == 4:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

if all(not x for x in (initial_fuel, consumption_index, fuel_needed)):
    print("John has reached all the altitudes and managed to reach the top!")