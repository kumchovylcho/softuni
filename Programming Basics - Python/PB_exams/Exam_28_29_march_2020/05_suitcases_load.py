EVERY_THIRD_CASE_PERCENTAGE_INCREASE = 1.1
WEIGHT_INCREASE_PER_THREE_CASES = 3
END_OF_LOADING_COMMAND = "End"

capacity = float(input())
cases_loaded = 0
loaded_weight = capacity

command = input()
while command != END_OF_LOADING_COMMAND and loaded_weight > 0:
    case = float(command)

    cases_loaded += 1
    if cases_loaded % WEIGHT_INCREASE_PER_THREE_CASES == 0:
        case *= EVERY_THIRD_CASE_PERCENTAGE_INCREASE

    loaded_weight -= case

    if loaded_weight < 0:
        cases_loaded -= 1
        print(f"No more space!")
        continue

    command = input()

if loaded_weight >= 0:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {cases_loaded} suitcases loaded.")

########################################################################

# capacity_of_trunk = float(input())
# suit_case_counter = 0
# space = 0
# suit_cases = input()
# while suit_cases != "End":
#     suit_case_counter += 1
#     suit_cases = float(suit_cases)
#     space += suit_cases
#     if suit_case_counter % 3 == 0:
#         space += suit_cases * 0.10
#     if space >= capacity_of_trunk:
#         if capacity_of_trunk != space:
#             suit_case_counter -= 1
#         break
#     suit_cases = input()
# if space <= capacity_of_trunk:
#     print(f"Congratulations! All suitcases are loaded!\nStatistic: {suit_case_counter} suitcases loaded.")
# else:
#     print(f"No more space!\nStatistic: {suit_case_counter} suitcases loaded.")
