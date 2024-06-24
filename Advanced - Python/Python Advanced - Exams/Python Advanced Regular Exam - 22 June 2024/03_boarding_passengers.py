def boarding_passengers(ship_capacity, *args):
    program_guests = {}

    for group_number, program_name in args:
        if ship_capacity == 0:
            break

        if ship_capacity - group_number < 0:
            continue

        program_guests[program_name] = program_guests.get(program_name, 0) + group_number
        ship_capacity -= group_number

    output = [
        "Boarding details by benefit plan:"
    ]
    sorted_by_guests = sorted(program_guests.items(), key=lambda x: (-x[1], x[0]))
    for program, guests in sorted_by_guests:
        output.append(f"## {program}: {guests} guests")

    all_passengers_boarded = sum(program_guests.values()) == sum(number for number, _ in args)
    if all_passengers_boarded:
        output.append("All passengers are successfully boarded!")
    elif not ship_capacity and not all_passengers_boarded:
        output.append("Boarding unsuccessful. Cruise ship at full capacity.")
    elif ship_capacity and not all_passengers_boarded:
        output.append(f"Partial boarding completed. Available capacity: {ship_capacity}.")

    return "\n".join(output)
