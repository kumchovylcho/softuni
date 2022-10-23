list_of_cards = input().split(", ")
number_of_commands = int(input())

for _ in range(number_of_commands):
    cards = input().split(", ")
    command = cards[0]
    if command == "Add":
        current_card = cards[1]
        if current_card in list_of_cards:
            print("Card is already in the deck")
        else:
            list_of_cards.append(current_card)
            print("Card successfully added")
    elif command == "Remove":
        current_card = cards[1]
        if current_card in list_of_cards:
            list_of_cards.remove(current_card)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command == "Remove At":
        index_of_cards = int(cards[1])
        if 0 <= index_of_cards < len(list_of_cards):
            list_of_cards.pop(index_of_cards)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif command == "Insert":
        index_of_cards, card_name = int(cards[1]), cards[2]
        if 0 <= index_of_cards < len(list_of_cards):
            if card_name in list_of_cards:
                print("Card is already added")
            else:
                list_of_cards.insert(index_of_cards, card_name)
                print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(list_of_cards))