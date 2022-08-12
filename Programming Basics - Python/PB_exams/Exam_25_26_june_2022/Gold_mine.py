gold_mined = 0
number_of_locations = int(input())
for location in range(1, number_of_locations + 1):
    expected_average_gold = float(input())
    number_of_days_to_mine_on_location = int(input())
    for days_in_location in range(1, number_of_days_to_mine_on_location + 1):
        gold_mined_for_the_day = float(input())
        gold_mined += gold_mined_for_the_day
    gold_mined /= number_of_days_to_mine_on_location
    if gold_mined >= expected_average_gold:
        print(f"Good job! Average gold per day: {gold_mined:.2f}.")
    elif gold_mined < expected_average_gold:
        diff = abs(gold_mined - expected_average_gold)
        print(f"You need {diff:.2f} gold.")
    gold_mined = 0
