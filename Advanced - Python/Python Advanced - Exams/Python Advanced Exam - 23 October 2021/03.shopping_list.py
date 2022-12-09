def shopping_list(budget, **kwargs):
    output = []
    if budget < 100:
        return "You do not have enough budget."
    for item, (price, quantity) in kwargs.items():
        current_item_price = price * quantity
        if budget >= current_item_price and len(output) < 5:
            budget -= current_item_price
            output.append(f"You bought {item} for {current_item_price:.2f} leva.")
    return '\n'.join(output)
