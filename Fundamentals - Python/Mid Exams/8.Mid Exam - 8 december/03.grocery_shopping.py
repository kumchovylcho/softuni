products = input().split("|")
command = input()
while command != "Shop!":
    task, *data = [x for x in command.split("%")]
    if task == "Important":
        product = data[0]
        if product in products:
            products.remove(product)
        products.insert(0, product)
    elif task == "Add":
        product = data[0]
        if product not in products:
            products.append(product)
        elif product in products:
            print("The product is already in the list.")
    elif task == "Swap":
        product_one, product_two = data
        if product_one in products and product_two in products:
            index_product_one = products.index(product_one)
            index_product_two = products.index(product_two)
            products[index_product_one], products[index_product_two] = products[index_product_two], products[index_product_one]
        elif product_one not in products:
            print(f"Product {product_one} missing!")
        elif product_two not in products:
            print(f"Product {product_two} missing!")
    elif task == "Remove":
        product = data[0]
        if product in products:
            products.remove(product)
        elif product not in products:
            print(f"Product {product} isn't in the list.")
    elif task == "Reversed":
        products = products[::-1]
    command = input()
for position, item in enumerate(products, 1):
    print(f"{position}. {item}")