vips = set()
regulars = set()
all_guests = set()
number_of_guests = int(input())
for _ in range(number_of_guests):
    guest = input()
    all_guests.add(guest)
user_that_have_come = input()
while user_that_have_come != "END":
    if user_that_have_come in all_guests:
        if user_that_have_come[0].isdigit():
            vips.add(user_that_have_come)
        elif not user_that_have_come[0].isdigit():
            regulars.add(user_that_have_come)
        all_guests.discard(user_that_have_come)
    user_that_have_come = input()
print(len(all_guests))
for reservation in sorted(all_guests):
    print(reservation)


