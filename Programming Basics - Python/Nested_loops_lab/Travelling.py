money_savings = 0
destination = input()
while destination != "End":
    money_needed = float(input())
    while money_savings < money_needed:
        money_to_save = float(input())
        money_savings += money_to_save
    print(f"Going to {destination}!")
    money_savings = 0
    destination = input()

