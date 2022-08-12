fruit = input()
set = input()
ordered_sets = int(input())
small_watermelon = 56 * 2
small_mango = 36.66 * 2
small_pineapple = 42.10 * 2
small_raspberry = 20 * 2
big_watermelon = 28.70 * 5
big_mango = 19.60 * 5
big_pineapple = 24.80 * 5
big_raspberry = 15.20 * 5
total = 0
if fruit == "Watermelon" and set == "small":
    total = small_watermelon * ordered_sets
elif fruit == "Watermelon" and set == "big":
    total = big_watermelon * ordered_sets
elif fruit == "Mango" and set == "small":
    total = small_mango * ordered_sets
elif fruit == "Mango" and set == "big":
    total = big_mango * ordered_sets
elif fruit == "Pineapple" and set == "small":
    total = small_pineapple * ordered_sets
elif fruit == "Pineapple" and set == "big":
    total = big_pineapple * ordered_sets
elif fruit == "Raspberry" and set == "small":
    total = small_raspberry * ordered_sets
elif fruit == "Raspberry" and set == "big":
    total = big_raspberry * ordered_sets
if 400 <= total <= 1000:
    total = total - (total * 0.15)
elif total > 1000:
    total *= 0.50
print(f"{total:.2f} lv.")