def collect(item):
    if item not in items:
        items.append(item)


def drop(item):
    if item in items:
        items.remove(item)


def combine_items(old_item, new_item):
    if old_item in items:
        index = items.index(old_item) + 1
        items.insert(index, new_item)


def renew(item):
    if item in items:
        items.remove(item)
        items.append(item)


items = input().split(", ")
command = input()
while command != "Craft!":
    command = command.split(" - ")
    event = command[0]
    if event == "Collect":
        collect(command[1])
    elif event == "Drop":
        drop(command[1])
    elif event == "Combine Items":
        command = command[1].split(":")
        old_item = command[0]
        new_item = command[1]
        combine_items(old_item, new_item)
    elif event == "Renew":
        renew(command[1])
    command = input()

print(*items, sep=", ")
