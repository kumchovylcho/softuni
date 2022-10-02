cards = input().split()
shuffle = int(input())

length = len(cards)
mid = length // 2

for i in range(shuffle):
    shuffled_cards = []
    for p in range(0, mid):
        shuffled_cards.append(cards[p])
        shuffled_cards.append(cards[mid])
        mid += 1
    cards = shuffled_cards
    mid = length // 2

print(cards)