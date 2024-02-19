def cookbook(*args):
    cookbook_data = {}
    for recipe, country, ingredients in args:
        if country not in cookbook_data:
            cookbook_data[country] = {}

        cookbook_data[country][recipe] = ingredients

    output = []
    for country, recipes in sorted(cookbook_data.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{country} cuisine contains {len(cookbook_data[country])} recipes:")

        for recipe, ingredients in sorted(recipes.items()):
            output.append(f"  * {recipe} -> Ingredients: {', '.join(ingredients)}")

    return "\n".join(output)

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))