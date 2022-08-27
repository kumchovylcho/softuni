miner_resources = dict()

minerals = input()
while minerals != "stop":
    quantity = int(input())

    if minerals in miner_resources:
        miner_resources[minerals] += quantity
    elif minerals not in miner_resources:
        miner_resources[minerals] = quantity

    minerals = input()

[print(f"{mineral} -> {miner_resources[mineral]}") for mineral in miner_resources]
