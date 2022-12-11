def stock_availability(items, *args):
    if args[0] == 'delivery' and args[1:]:
        items_to_deliver = args[1:]
        items = items + list(items_to_deliver)
    elif args[0] == 'sell' and not args[1:]:
        items.pop(0)
    elif args[0] == 'sell' and str(args[1]).isdigit():
        count_of_sold_items = args[1]
        items = items[count_of_sold_items:]
    elif args[0] == 'sell' and len(args[1:]) >= 1:
        for item in args[1:]:
            while item in items:
                items.remove(item)
    return items
