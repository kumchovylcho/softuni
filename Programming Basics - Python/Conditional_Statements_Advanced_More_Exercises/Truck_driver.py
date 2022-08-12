season = input()
km_per_month = float(input())
salary = 0
if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        salary = 0.75
    elif 5000 < km_per_month <= 10000:
        salary = 0.95
elif season == "Summer":
    if km_per_month <= 5000:
        salary = 0.90
    elif 5000 < km_per_month <= 10000:
        salary = 1.10
else:
    if km_per_month <= 5000:
        salary = 1.05
    elif 5000 < km_per_month <= 10000:
        salary = 1.25
if 10000 < km_per_month <= 20000:
    salary = 1.45
total = (salary * km_per_month) * 4
after_tax = total * 0.90
print(f"{after_tax:.2f}")
