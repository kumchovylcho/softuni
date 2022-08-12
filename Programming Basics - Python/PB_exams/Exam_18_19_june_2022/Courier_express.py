kg_of_the_package = float(input())
type_of_service = input()
kilometers = int(input())
price_km = 0
price_kg_express = 0
if type_of_service == "standard" or type_of_service == "express":
    if kg_of_the_package < 1:
        price_km = 0.03
        price_kg_express = price_km * 0.8
    elif 1 <= kg_of_the_package < 10:
        price_km = 0.05
        price_kg_express = price_km * 0.4
    elif 10 <= kg_of_the_package < 40:
        price_km = 0.10
        price_kg_express = price_km * 0.05
    elif 40 <= kg_of_the_package < 90:
        price_km = 0.15
        price_kg_express = price_km * 0.02
    elif 90 <= kg_of_the_package < 150:
        price_km = 0.20
        price_kg_express = price_km * 0.01
price_for_transport = kilometers * price_km
extra_for_km = kg_of_the_package * price_kg_express
total_extra = kilometers * extra_for_km + price_for_transport
if type_of_service == "standard":
    total_extra = price_km * kilometers
    print(f"The delivery of your shipment with weight of {kg_of_the_package:.3f} kg. would cost {total_extra:.2f} lv.")
else:
    print(f"The delivery of your shipment with weight of {kg_of_the_package:.3f} kg. would cost {total_extra:.2f} lv.")
