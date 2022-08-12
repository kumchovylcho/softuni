number_of_days = int(input())
liters = 0
temperature = 0
for day in range(1, number_of_days + 1):
    liters_rakia = float(input())
    temperature_of_the_rakia = float(input())
    liters += liters_rakia
    temperature += liters_rakia * temperature_of_the_rakia
average_temperature = temperature / liters
print(f"Liter: {liters:.2f}")
print(f"Degrees: {average_temperature:.2f}")
if average_temperature < 38:
    print("Not good, you should baking!")
elif 38 <= average_temperature <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
