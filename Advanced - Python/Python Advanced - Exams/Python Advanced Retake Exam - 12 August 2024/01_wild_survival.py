from collections import deque


def fight(bee_grp: int, bee_eaters: int) -> (int, int):
    while bee_grp and bee_eaters and bee_grp >= BEE_EATER_MAX_KILL:
        bee_grp -= BEE_EATER_MAX_KILL
        bee_eaters -= 1

    return bee_grp, bee_eaters


def main(bee_groups: deque, bee_eaters: list) -> None:
    while bee_groups and bee_eaters:
        bee_group, bee_eater = fight(bee_groups.popleft(), bee_eaters.pop())

        # if the battle isn't finished and there are leftovers
        if bee_eater > 0 and bee_group < BEE_EATER_MAX_KILL:
            bee_group = 0
            bee_eaters.append(bee_eater)

        if bee_group > 0:
            bee_groups.append(bee_group)

    print("The final battle is over!")

    if not bee_groups and not bee_eaters:
        print("But no one made it out alive!")
    elif bee_groups and not bee_eaters:
        print(f"Bee groups left: {', '.join(str(x) for x in bee_groups)}")
    elif bee_eaters and not bee_groups:
        print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters)}")


BEE_EATER_MAX_KILL = 7

main(
    deque(int(x) for x in input().split()),
    [int(x) for x in input().split()]
)
