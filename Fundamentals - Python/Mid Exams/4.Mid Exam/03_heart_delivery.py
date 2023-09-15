numbers = [int(x) for x in input().split("@")]
current_house = 0

jump = input()
while jump != "Love!":
    jump_length = int(jump.split()[-1])
    current_house += jump_length

    if current_house >= len(numbers):
        current_house = 0

    if not numbers[current_house]:
        print(f"Place {current_house} already had Valentine's day.")
        jump = input()
        continue

    numbers[current_house] -= 2
    if not numbers[current_house]:
        print(f"Place {current_house} has Valentine's day.")

    jump = input()


print(f"Cupid's last position was {current_house}.")

if numbers.count(0) == len(numbers):
    print("Mission was successful.")

else:
    failed_places = len(numbers) - numbers.count(0)
    print(f"Cupid has failed {failed_places} places.")

################################################################################################

# neighborhood = [int(x) for x in input().split("@")]
# cupid_house = 0
# current_jump = input()
# while current_jump != "Love!":
#     _, jump_power = [int(x) if x.isdigit() else x for x in current_jump.split()]
#     cupid_house += jump_power
#     if cupid_house >= len(neighborhood):
#         cupid_house = 0
#     if neighborhood[cupid_house] > 0:
#         neighborhood[cupid_house] -= 2
#         if neighborhood[cupid_house] == 0:
#             print(f"Place {cupid_house} has Valentine's day.")
#     elif neighborhood[cupid_house] == 0:
#         print(f"Place {cupid_house} already had Valentine's day.")
#     current_jump = input()
# print(f"Cupid's last position was {cupid_house}.")
# if all(True if house == 0 else False for house in neighborhood):
#     print("Mission was successful.")
# elif any(True if house > 0 else False for house in neighborhood):
#     print(f"Cupid has failed {len(neighborhood) - neighborhood.count(0)} places.")

################################################################################################

# def jump_on_houses(current_jump, last_house_jumped):
#     last_house_jumped += current_jump
#     if last_house_jumped >= len(neighborhood):
#         last_house_jumped = 0
#     if 0 <= last_house_jumped < len(neighborhood):
#         if neighborhood[last_house_jumped] >= 2:
#             neighborhood[last_house_jumped] -= 2
#             if neighborhood[last_house_jumped] == 0:
#                 print(f"Place {last_house_jumped} has Valentine's day.")
#         elif neighborhood[last_house_jumped] == 0:
#             print(f"Place {last_house_jumped} already had Valentine's day.")
#     return last_house_jumped
#
#
# neighborhood = [int(num) for num in input().split("@")]
# last_house = 0
# jump = input()
# while jump != "Love!":
#     jump = jump.split()
#     jump = int(jump[1])
#     last_house = jump_on_houses(jump, last_house)
#     jump = input()
#
# print(f"Cupid's last position was {last_house}.")
#
# cupid_fails = 0
# for hearts in neighborhood:
#     if hearts != 0:
#         cupid_fails += 1
#
# if not cupid_fails:
#     print("Mission was successful.")
# elif cupid_fails:
#     print(f"Cupid has failed {cupid_fails} places.")
