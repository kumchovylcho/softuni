cards = input().split()
shuffles = int(input())

# minus 1 because i am working without the first and the last card
middle = len(cards) // 2 - 1

shuffled_deck = cards[1:-1]
for i in range(shuffles):
    left_part = shuffled_deck[:middle]
    right_part = shuffled_deck[middle:]

    new_deck = []
    for j in range(len(left_part)):
        new_deck.append(right_part[j])
        new_deck.append(left_part[j])

    shuffled_deck = new_deck

result = [cards[0], *shuffled_deck, cards[-1]]
print(result)




# cards = input().split()
# shuffle = int(input())
#
# length = len(cards)
# mid = length // 2
#
# for i in range(shuffle):
#     shuffled_cards = []
#     for p in range(0, mid):
#         shuffled_cards.append(cards[p])
#         shuffled_cards.append(cards[mid])
#         mid += 1
#     cards = shuffled_cards
#     mid = length // 2
#
# print(cards)