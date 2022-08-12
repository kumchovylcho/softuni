type_of_fuel = input()
litres_fuel = float(input())
club_card = input()
gasoline = 2.22 * litres_fuel
diesel = 2.33 * litres_fuel
gas = 0.93 * litres_fuel
discount_gasoline = 0.18
discount_diesel = 0.12
discount_gas = 0.08
discount_20_25_litres = 0.92
discount_more_than_25 = 0.90
total_price = 0
if type_of_fuel == "Gasoline" and club_card == "Yes":
    total_price = gasoline - (discount_gasoline * litres_fuel)
elif type_of_fuel == "Gasoline" and club_card == "No":
    total_price = gasoline
elif type_of_fuel == "Diesel" and club_card == "Yes":
    total_price = diesel - (discount_diesel * litres_fuel)
elif type_of_fuel == "Diesel" and club_card == "No":
    total_price = diesel
elif type_of_fuel == "Gas" and club_card == "Yes":
    total_price = gas - (discount_gas * litres_fuel)
elif type_of_fuel == "Gas" and club_card == "No":
    total_price = gas
if 20 <= litres_fuel <= 25:
    total_price *= discount_20_25_litres
elif litres_fuel > 25:
    total_price *= discount_more_than_25
print(f"{total_price:.2f} lv.")
