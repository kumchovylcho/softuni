size_of_eggs = input()
color_of_the_eggs = input()
number_of_batch = int(input())
prices = {"Large": {
    "Red": 16,
    "Green": 12,
    "Yellow": 9},
        "Medium": {
    "Red": 13,
    "Green": 9,
    "Yellow": 7},
        "Small": {
        "Red": 9,
        "Green": 8,
        "Yellow": 5}
}
total_price = 0
production_costs = 0.65
if size_of_eggs == "Large" and color_of_the_eggs in prices["Large"]:
    total_price = prices["Large"][color_of_the_eggs] * number_of_batch
elif size_of_eggs == "Medium" and color_of_the_eggs in prices["Medium"]:
    total_price = prices["Medium"][color_of_the_eggs] * number_of_batch
else:
    total_price = prices["Small"][color_of_the_eggs] * number_of_batch
total_price *= production_costs
print(f"{total_price:.2f} leva.")
