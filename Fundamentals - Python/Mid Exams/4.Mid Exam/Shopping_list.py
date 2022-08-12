products = input().split("!")


def urgent(item):
    if item not in products:
        products.insert(0, item)


def unnecessary(item):
    if item in products:
        products.remove(item)


def correct(old_item, new_item):
    if old_item in products:
        index = products.index(old_item)
        products.insert(index, new_item)
        del products[index + 1]


def rearrange(item):
    if item in products:
        products.remove(item)
        products.insert(len(products), item)


command = input()
while command != "Go Shopping!":
    command = command.split()
    event = command[0]
    product = command[1]
    if event == "Urgent":
        urgent(product)
    elif event == "Unnecessary":
        unnecessary(product)
    elif event == "Correct":
        old_item = command[1]
        new_item = command[2]
        correct(old_item, new_item)
    elif event == "Rearrange":
        rearrange(product)
    command = input()

print(*products, sep=", ")
