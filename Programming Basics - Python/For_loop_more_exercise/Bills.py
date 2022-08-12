months_for_average_bill = int(input())
power = 0
water = 0
internet = 0
other = 0
for month in range(1, months_for_average_bill + 1):
    power_bill = float(input())
    power += power_bill
    water += 20
    internet += 15
    other += (power_bill + 20 + 15) * 1.20
average_bill_for_all_months = (power + water + internet + other) / months_for_average_bill
print(f"Electricity: {power:.2f} lv\nWater: {water:.2f} lv\nInternet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv\nAverage: {average_bill_for_all_months:.2f} lv")
