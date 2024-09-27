def draw_cards(*args, **kwargs):
    print_mapper = {
        "monster": {"print_symbol": "***", "print_msg": "Monster cards:", "sort_by": "desc"},
        "spell": {"print_symbol": "$$$", "print_msg": "Spell cards:", "sort_by": "asc"}
    }
    cards = {}

    for card_name, card_type in args:
        cards[card_type] = cards.get(card_type, []) + [card_name]

    for card_name, card_type in kwargs.items():
        cards[card_type] = cards.get(card_type, []) + [card_name]


    output = []
    for name, collection in cards.items():
        if not collection:
            continue

        sorted_collection = sorted(collection) if print_mapper[name]["sort_by"] == "asc" else sorted(collection, reverse=True)
        output.append(print_mapper[name]["print_msg"])
        for card in sorted_collection:
            output.append(f"  {print_mapper[name]['print_symbol']}{card}")

    return "\n".join(output)


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print()
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print()
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))