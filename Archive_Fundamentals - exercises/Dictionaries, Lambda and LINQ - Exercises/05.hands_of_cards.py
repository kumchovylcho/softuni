cards_power = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
    'S': 4,
    'H': 3,
    'D': 2,
    'C': 1
}
cards = {}
name = input()
while name != "JOKER":
    user_name = name.split(": ")[0]
    current_cards = name.split(f"{user_name}: ")[1].split(", ")
    cards[user_name] = cards.get(user_name, {'cards': [], 'values': []})
    for card in current_cards:
        if card not in cards[user_name]['cards']:
            cards[user_name]['cards'].append(card)
            last_symbol = card[-1]
            multiplier = card[:-1]
            result = cards_power[multiplier] * cards_power[last_symbol]
            cards[user_name]['values'].append(result)
    name = input()
for name, points in cards.items():
    print(f"{name}: {sum(points['values'])}")