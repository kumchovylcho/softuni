def monster(monster, damage_received, hp, count_room):
    hp -= damage_received
    if hp <= 0:
        print(f"You died! Killed by {monster}.")
        print(f"Best room: {count_room}")
    elif hp > 0:
        print(f"You slayed {monster}.")
    return hp


def potion(healing, health):
    if health + healing > 100:
        healing = 100 - health
        health = 100
    elif health + healing <= 100:
        health = health + healing
    print(f"You healed for {healing} hp.")
    print(f"Current health: {health} hp.")
    return health


def chest(coins):
    print(f"You found {coins} bitcoins.")
    return coins


dungeon_rooms = input().split("|")
hp = 100
bitcoins = 0
for count, room in enumerate(dungeon_rooms, 1):
    room = room.split()
    event = room[0]
    currency = int(room[1])
    if event != "potion" and event != "chest":
        hp = monster(event, currency, hp, count)
        if hp <= 0:
            break
    elif event == "potion":
        hp = potion(currency, hp)
    elif event == "chest":
        bitcoins += chest(currency)

if hp > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {hp}")
