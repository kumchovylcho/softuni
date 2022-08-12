capacity_of_trunk = float(input())
suit_case_counter = 0
space = 0
suit_cases = input()
while suit_cases != "End":
    suit_case_counter += 1
    suit_cases = float(suit_cases)
    space += suit_cases
    if suit_case_counter % 3 == 0:
        space += suit_cases * 0.10
    if space >= capacity_of_trunk:
        if capacity_of_trunk != space:
            suit_case_counter -= 1
        break
    suit_cases = input()
if space <= capacity_of_trunk:
    print(f"Congratulations! All suitcases are loaded!\nStatistic: {suit_case_counter} suitcases loaded.")
else:
    print(f"No more space!\nStatistic: {suit_case_counter} suitcases loaded.")
