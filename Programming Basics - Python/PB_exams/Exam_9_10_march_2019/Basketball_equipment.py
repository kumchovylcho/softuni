year_tax_for_training = int(input())
basketball_shoes = year_tax_for_training * 0.6
basketball_clothes = basketball_shoes * 0.8
basketball_ball = basketball_clothes / 4
basketball_accessory = basketball_ball / 5
total_price = year_tax_for_training + basketball_shoes + basketball_clothes + basketball_ball + basketball_accessory
print(f"{total_price:.2f}")
