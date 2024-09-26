def accommodate(*args, **kwargs):
    sorted_rooms = sorted(kwargs.items(), key=lambda room: (room[1], int(room[0].split("_")[1])))
    accommodations = {}

    for group in args:
        for room, capacity in sorted_rooms:
            if room in accommodations:
                continue

            if group == capacity or capacity > group:
                accommodations[room] = group
                break

    output = []
    if not accommodations:
        output.append("No accommodations were completed!")
    else:
        output.append(f"A total of {len(accommodations)} accommodations were completed!")
        for room_number, accommodated_guests in sorted(accommodations.items(), key=lambda room: int(room[0].split("_")[1])):
            output.append(f"<Room {room_number.split('_')[1]} accommodates {accommodated_guests} guests>")

    total_guests = sum(args)
    total_accommodated_guests = sum(accommodations.values())
    if total_guests != total_accommodated_guests:
        output.append(f"Guests with no accommodation: {total_guests - total_accommodated_guests}")

    if len(kwargs) != len(accommodations):
        output.append(f"Empty rooms: {len(kwargs) - len(accommodations)}")

    return "\n".join(output)


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print()
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print()
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))