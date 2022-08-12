budget = float(input())
category = input()
number_of_people_in_group = int(input())
for_transport = budget
price = 0
if category == "VIP":
    price = 499.99
    if 1 <= number_of_people_in_group <= 4:
        for_transport *= 0.75
    elif 5 <= number_of_people_in_group <= 9:
        for_transport *= 0.60
    elif 10 <= number_of_people_in_group <= 24:
        for_transport *= 0.50
    elif 25 <= number_of_people_in_group <= 49:
        for_transport *= 0.40
    else:
        for_transport *= 0.25
else:
    price = 249.99
    if 1 <= number_of_people_in_group <= 4:
        for_transport *= 0.75
    elif 5 <= number_of_people_in_group <= 9:
        for_transport *= 0.60
    elif 10 <= number_of_people_in_group <= 24:
        for_transport *= 0.50
    elif 25 <= number_of_people_in_group <= 49:
        for_transport *= 0.40
    else:
        for_transport *= 0.25
total = price * number_of_people_in_group
diff = budget - for_transport
diff_1 = total - diff

if total <= diff:
    print(f"Yes! You have {abs(diff_1):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(diff_1):.2f} leva.")
