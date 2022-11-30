def grocery_store(**kwargs):
    sorted_products = []
    for key, value in sorted(kwargs.items(), key=lambda item: (-item[1], -len(item[0]), item[0])):
        sorted_products.append(f"{key}: {value}")
    return '\n'.join(sorted_products)
