def accommodate_new_pets(capacity: int,
                         max_weight: float,
                         *pets
                         ):
    pet_types_counter = {}
    has_space = True

    for pet_type, pet_weight in pets:
        if capacity <= 0:
            has_space = False
            continue

        if pet_weight > max_weight:
            continue

        capacity -= 1

        pet_types_counter[pet_type] = pet_types_counter.get(pet_type, 0) + 1

    accommodate_msg = f"All pets are accommodated! Available capacity: {capacity}."
    if not has_space:
        accommodate_msg = "You did not manage to accommodate all pets!"

    sorted_by_names = sorted(pet_types_counter)

    result = [accommodate_msg,
              "Accommodated pets:",]
    [result.append(f"{pet}: {pet_types_counter[pet]}") for pet in sorted_by_names]

    return "\n".join(result)
