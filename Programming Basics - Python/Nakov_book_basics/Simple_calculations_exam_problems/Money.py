number_of_bitcoins = int(input())
number_of_chinese_money = float(input())
commission = float(input()) / 100
bitcoins_into_leva = number_of_bitcoins * 1168
chinese_money_to_dollars = number_of_chinese_money * 0.15
dollars_to_leva = chinese_money_to_dollars * 1.76
leva_to_euro = (bitcoins_into_leva + dollars_to_leva) / 1.95
leva_to_euro -= leva_to_euro * commission
print(f"{leva_to_euro:.2f}")