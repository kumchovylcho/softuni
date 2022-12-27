class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = float(price)
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
        # if ingredient in self.ingredients:
        #     self.ingredients[ingredient] += quantity
        # elif ingredient not in self.ingredients:
        #     self.ingredients[ingredient] = quantity
        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self):
        self.ordered = True
        show_ingredients = [f"{key}: {str(value)}" for key, value in self.ingredients.items()]
        return f"You've ordered pizza {self.name} prepared with {', '.join(show_ingredients)} and" \
               f" the price will be {int(self.price)}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))


# class PizzaDelivery:
#
#     def __init__(self, name, price: float, ingredients: dict):
#         self.name = name
#         self.price = float(price)
#         self.ingredients = ingredients
#         self.ordered = False
#
#     def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         if ingredient in self.ingredients:
#             self.ingredients[ingredient] += int(quantity)
#             self.price += float(price_per_quantity) * int(quantity)
#         elif ingredient not in self.ingredients:
#             self.ingredients[ingredient] = int(quantity)
#             self.price += int(quantity) * float(price_per_quantity)
#
#     def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         if ingredient not in self.ingredients:
#             return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
#         elif ingredient in self.ingredients and self.ingredients[ingredient] < quantity:
#             return f"Please check again the desired quantity of {ingredient}!"
#         self.ingredients[ingredient] -= int(quantity)
#         self.price -= float(price_per_quantity) * int(quantity)
#
#     def make_order(self):
#         if not self.ordered:
#             all_ingredients = []
#             for key, value in self.ingredients.items():
#                 all_ingredients.append(f"{key}: {value}")
#             self.ordered = True
#             return f"You've ordered pizza {self.name} prepared with {', '.join(all_ingredients)} and the price" \
#                    f" will be {int(self.price)}lv."
#         return f"Pizza {self.name} already prepared, and we can't make any changes!"
