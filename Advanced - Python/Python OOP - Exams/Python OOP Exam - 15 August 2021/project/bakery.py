from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def get_menu(self):
        food_menu = {key.name: key for key in self.food_menu}
        food_menu.update({key.name: key for key in self.drinks_menu})
        return food_menu

    def add_food(self, food_type: str, name: str, price: float):
        valid_food_types = {
            "Bread": Bread,
            "Cake": Cake
        }
        for x in self.food_menu:
            if x.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type in valid_food_types:
            create_food = valid_food_types[food_type](name, price)
            self.food_menu.append(create_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        valid_drink_types = {
            "Tea": Tea,
            "Water": Water
        }
        for x in self.drinks_menu:
            if x.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type in valid_drink_types:
            create_drink = valid_drink_types[drink_type](name, portion, brand)
            self.drinks_menu.append(create_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        valid_tables = {
            "InsideTable": InsideTable,
            "OutsideTable": OutsideTable
        }
        for x in self.tables_repository:
            if x.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type in valid_tables:
            create_table = valid_tables[table_type](table_number, capacity)
            self.tables_repository.append(create_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for x in self.tables_repository:
            if not x.is_reserved and x.capacity >= number_of_people:
                x.reserve(number_of_people)
                return f"Table {x.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            food_in_menu = [f"Table {table_number} ordered:"]
            food_not_in_menu = [f"{self.name} does not have in the menu:"]
            current_menu = self.get_menu()
            for food_name in args:
                if food_name in current_menu:
                    table.order_food(current_menu[food_name])
                    food_in_menu.append(f"{current_menu[food_name]}")
                else:
                    food_not_in_menu.append(food_name)
            return '\n'.join(food_in_menu + food_not_in_menu)
        return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"

        table = table[0]
        drink_in_menu = [f"Table {table_number} ordered:"]
        drink_not_in_menu = [f"{self.name} does not have in the menu:"]
        current_menu = self.get_menu()
        for drink_name in args:
            if drink_name in current_menu:
                table.order_drink(current_menu[drink_name])
                drink_in_menu.append(f"{current_menu[drink_name]}")
            else:
                drink_not_in_menu.append(drink_name)
        return '\n'.join(drink_in_menu + drink_not_in_menu)

    def leave_table(self, table_number: int):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            bill = table.get_bill()
            self.total_income += bill
            table.clear()
            return f"Table: {table_number}\n" \
                   f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = []
        for x in self.tables_repository:
            result.append(x.free_table_info())
        return '\n'.join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
