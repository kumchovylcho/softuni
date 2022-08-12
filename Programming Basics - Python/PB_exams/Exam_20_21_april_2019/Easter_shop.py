eggs_in_shop = int(input())
command = input()
sold_eggs = 0
while command != "Close":
    if command == "Buy":
        eggs_bought = int(input())
        if eggs_bought <= eggs_in_shop:
            eggs_in_shop -= eggs_bought
            sold_eggs += eggs_bought
        else:
            print(f"Not enough eggs in store!\nYou can buy only {eggs_in_shop}.")
            break
    if command == "Fill":
        eggs_fill = int(input())
        eggs_in_shop += eggs_fill
    command = input()
if command == "Close":
    print(f"Store is closed!\n{sold_eggs} eggs sold.")
