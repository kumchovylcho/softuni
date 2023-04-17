coins_1_leva = int(input())
coins_2_leva = int(input())
banknotes_5_leva = int(input())

goal = int(input())


for one in range(coins_1_leva + 1):
    for two in range(coins_2_leva + 1):
        for three in range(banknotes_5_leva + 1):
            if (one * 1) + (two * 2) + (three * 5) != goal:
                continue

            result = f'{one} * 1 lv. + {two} * 2 lv. + {three} * 5 lv. = {goal} lv.'
            print(result)
