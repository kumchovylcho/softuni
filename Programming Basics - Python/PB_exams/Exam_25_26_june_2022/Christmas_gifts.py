kids = 0
adults = 0
money_for_toys = 0
money_for_sweaters = 0
years_old_for_every_person = input()
while years_old_for_every_person != "Christmas":
    years_old_for_every_person = int(years_old_for_every_person)
    if years_old_for_every_person <= 16:
        kids += 1
        money_for_toys += 5
    elif years_old_for_every_person > 16:
        adults += 1
        money_for_sweaters += 15
    years_old_for_every_person = input()
print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")
