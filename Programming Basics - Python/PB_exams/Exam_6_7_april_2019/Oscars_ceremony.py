rent_for_hall = int(input())
statues = rent_for_hall * 0.7
catering = statues * 0.85
sound = catering / 2
total = rent_for_hall + statues + catering + sound
print(f"{total:.2f}")
