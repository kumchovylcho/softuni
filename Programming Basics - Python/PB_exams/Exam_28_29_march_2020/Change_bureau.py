number_of_bitcoins = int(input())
number_of_chinese_money = float(input())
commission = float(input()) / 100
bitcoin = 1168
one_chinese_money_to_dollars = 0.15
one_dollar_to_leva = 1.76
one_euro_to_leva = 1.95
bitcon_sum = number_of_bitcoins * bitcoin
chinese_sum = number_of_chinese_money * one_chinese_money_to_dollars
dollars = chinese_sum * one_dollar_to_leva
total = bitcon_sum + dollars
total = total / one_euro_to_leva
after_commission = total - (total * commission)
print(f"{after_commission:.2f}")