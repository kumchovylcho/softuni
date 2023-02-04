from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter
from project.client import Client


class FoodOrdersApp:

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 1

    def __reset_client_information(self, client):
        client.bill = 0
        client.shopping_cart = []
        client.ordered_meals = {}

    @staticmethod
    def meal_in_menu(meal_names_and_quantities, menu_info):
        for meal in meal_names_and_quantities:
            if meal not in menu_info:
                raise Exception(f"{meal} is not on the menu!")

    @staticmethod
    def enough_quantity(meal_names_and_quantities, menu_info):
        for meal, quantity in meal_names_and_quantities.items():
            if menu_info[meal].quantity < quantity:
                raise Exception(f"Not enough quantity of {menu_info[meal].__class__.__name__}: {meal}!")

    def __get_menu(self):
        return {meal.name: meal for meal in self.menu}

    def __get_or_create_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return new_client

    @property
    def valid_meals(self):
        return "Starter", "MainDish", "Dessert"

    @staticmethod
    def __find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def register_client(self, client_phone_number: str):
        client = self.__find_object(client_phone_number, "phone_number", self.clients_list)
        if client:
            raise Exception("The client has already been registered!")

        create_client = Client(client_phone_number)
        self.clients_list.append(create_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.valid_meals:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join(x.details() for x in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        menu_info = self.__get_menu()
        find_client = self.__get_or_create_client(client_phone_number)

        self.meal_in_menu(meal_names_and_quantities, menu_info)
        self.enough_quantity(meal_names_and_quantities, menu_info)

        for name, qty in meal_names_and_quantities.items():
            menu_info[name].quantity -= qty
            find_client.shopping_cart.append(menu_info[name])

        find_client.bill += sum(menu_info[name].price * qty for name, qty in meal_names_and_quantities.items())
        find_client.ordered_meals.update(meal_names_and_quantities)

        return f"Client {client_phone_number} successfully ordered {', '.join(find_client.ordered_meals)} for {find_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_object(client_phone_number, "phone_number", self.clients_list)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        menu_info = self.__get_menu()
        for name, qty in client.ordered_meals.items():
            menu_info[name].quantity += qty

        self.__reset_client_information(client)
        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_object(client_phone_number, "phone_number", self.clients_list)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        current_receipt = self.receipt_id
        paid_money = client.bill

        client.shopping_cart = []
        client.bill = 0.0

        self.receipt_id += 1
        return f"Receipt #{current_receipt} with total amount of {paid_money:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)
