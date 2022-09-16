rules = {
    "drink toddy": 14,
    "drink coke": 18,
    "drink beer": 21,
    "drink whisky": 110
}
age = int(input())
for key, value in rules.items():
    if age <= value:
        print(key)
        break


# person_age = int(input())
# if person_age <= 14:
#     print("drink toddy")
# elif person_age <= 18:
#     print("drink coke")
# elif person_age <= 21:
#     print("drink beer")
# elif person_age > 21:
#     print("drink whisky")


