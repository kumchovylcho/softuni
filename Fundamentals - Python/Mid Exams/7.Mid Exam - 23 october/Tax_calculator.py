taxed_vehicles = input().split(">>")
total_taxes = 0
for vehicles in taxed_vehicles:
    car_type, tax_years, kilometers_traveled = [item if item[0].isalpha() else int(item) for item in vehicles.split()]
    initial_tax = 0
    if car_type == 'family':
        initial_tax += 50
        initial_tax -= tax_years * 5
        initial_tax += (kilometers_traveled // 3000) * 12

    elif car_type == 'heavyDuty':
        initial_tax += 80
        initial_tax -= tax_years * 8
        initial_tax += (kilometers_traveled // 9000) * 14

    elif car_type == 'sports':
        initial_tax += 100
        initial_tax -= tax_years * 9
        initial_tax += (kilometers_traveled // 2000) * 18
    if not initial_tax:
        print("Invalid car type.")
    else:
        total_taxes += initial_tax
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")