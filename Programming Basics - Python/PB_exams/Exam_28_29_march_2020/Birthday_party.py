rent_of_hall = float(input())
cake = rent_of_hall * 0.2
drinks = cake - (cake * 0.45)
funny_guy = rent_of_hall // 3
total = rent_of_hall + cake + drinks + funny_guy
print(f"{total}")