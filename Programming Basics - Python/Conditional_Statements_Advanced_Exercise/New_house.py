type_flower = input()
number_of_flowers = int(input())
budget = int(input())
price = 0
if type_flower == "Roses":
    price = 5 * number_of_flowers
    if number_of_flowers > 80:
        price *= 0.90
elif type_flower == "Dahlias":
    price = 3.80 * number_of_flowers
    if number_of_flowers > 90:
        price *= 0.85
elif type_flower == "Tulips":
    price = 2.80 * number_of_flowers
    if number_of_flowers > 80:
        price *= 0.85
elif type_flower == "Narcissus":
    price = 3 * number_of_flowers
    if number_of_flowers < 120:
        price *= 1.15
elif type_flower == "Gladiolus":
    price = 2.50 * number_of_flowers
    if number_of_flowers < 80:
        price *= 1.20
diff = abs(budget - price)
if price <= budget:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
