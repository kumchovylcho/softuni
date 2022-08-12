dish_detergent = int(input())
total_detergent = dish_detergent * 750
detergent_for_plate = 5
detergent_for_pot = 15
counter_for_pots = 0
number_of_plates = 0
numbers_of_pots = 0
no_detergent = False
number_of_dishes = input()
while number_of_dishes != "End":
    number_of_dishes = int(number_of_dishes)
    counter_for_pots += 1
    if counter_for_pots % 3 == 0:
        total_detergent -= number_of_dishes * detergent_for_pot
        numbers_of_pots += number_of_dishes
    else:
        total_detergent -= number_of_dishes * detergent_for_plate
        number_of_plates += number_of_dishes
    if total_detergent < 0:
        no_detergent = True
        break
    number_of_dishes = input()
if no_detergent:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
else:
    print(f"Detergent was enough!")
    print(f"{number_of_plates} dishes and {numbers_of_pots} pots were washed.\nLeftover detergent {total_detergent} ml.")
