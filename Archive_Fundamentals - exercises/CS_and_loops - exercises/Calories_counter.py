products_with_calories = {
    'cheese': 500,
    'tomato sauce': 150,
    'salami': 600,
    'pepper': 50,
    'total': 0
}

number_of_products = int(input())
for _ in range(number_of_products):
    current_product = input().lower()
    if current_product in products_with_calories:
        products_with_calories['total'] += products_with_calories[current_product]

print(f"Total calories: {products_with_calories['total']}")
