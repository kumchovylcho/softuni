def plant_garden(space: float, *allowed_plants, **plant_requests):
    def find_allowed_plant_by_name(name: str):
        for plant_name, plant_quantity in allowed_plants:
            if plant_name == name:
                return plant_name, plant_quantity
        return None, None


    planted_plants = {}
    ran_out_of_space = False

    for plant in sorted(plant_requests):
        requested_quantity = plant_requests[plant]
        allowed_plant_name, allowed_plant_space_required = find_allowed_plant_by_name(plant)
        if allowed_plant_name is None:
            continue

        if space < allowed_plant_space_required:
            ran_out_of_space = True
            continue

        amount_can_plant = min(requested_quantity, int(space / allowed_plant_space_required))
        planted_plants[plant] = planted_plants.get(plant, 0) + amount_can_plant
        space -= allowed_plant_space_required * amount_can_plant

        if amount_can_plant < requested_quantity:
            ran_out_of_space = True


    output = []
    if not ran_out_of_space:
        output.append(f"All plants were planted! Available garden space: {space:.1f} sq meters.")
    elif ran_out_of_space:
        output.append("Not enough space to plant all requested plants!")

    output.append("Planted plants:")
    for plant in sorted(planted_plants):
        output.append(f"{plant}: {planted_plants[plant]}")

    return "\n".join(output)