number_of_turns_in_game = int(input())
score = 0
zero_9 = 0
ten_19 = 0
twenty_29 = 0
thirty_39 = 0
forty_50 = 0
invalid = 0
for turn in range(1, number_of_turns_in_game + 1):
    number_in_interval = int(input())
    if 0 <= number_in_interval <= 9:
        score += number_in_interval * 0.2
        zero_9 += 1
    elif 10 <= number_in_interval <= 19:
        score += number_in_interval * 0.3
        ten_19 += 1
    elif 20 <= number_in_interval <= 29:
        score += number_in_interval * 0.4
        twenty_29 += 1
    elif 30 <= number_in_interval <= 39:
        score += 50
        thirty_39 += 1
    elif 40 <= number_in_interval <= 50:
        score += 100
        forty_50 += 1
    else:
        score /= 2
        invalid += 1
percentage_zero_9 = zero_9 / number_of_turns_in_game * 100
percentage_ten_19 = ten_19 / number_of_turns_in_game * 100
percentage_twenty_29 = twenty_29 / number_of_turns_in_game * 100
percentage_thirty_39 = thirty_39 / number_of_turns_in_game * 100
percentage_forty_50 = forty_50 / number_of_turns_in_game * 100
percentage_invalid = invalid / number_of_turns_in_game * 100
print(f"{score:.2f}\nFrom 0 to 9: {percentage_zero_9:.2f}%\nFrom 10 to 19: {percentage_ten_19:.2f}%")
print(f"From 20 to 29: {percentage_twenty_29:.2f}%\nFrom 30 to 39: {percentage_thirty_39:.2f}%")
print(f"From 40 to 50: {percentage_forty_50:.2f}%\nInvalid numbers: {percentage_invalid:.2f}%")
