current_money = 0
total_money = 0
number_of_orders = int(input())
for order in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100.00:
        if 1 <= days <= 31:
            if 1 <= capsules_needed_per_day <= 2000:
                current_money += (capsules_needed_per_day * days) * price_per_capsule
                print(f"The price for the coffee is: ${current_money:.2f}")
    total_money += current_money
    current_money = 0
print(f"Total: ${total_money:.2f}")
