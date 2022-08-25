class Vehicle:

    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money, owner):
        if money >= self.price and self.owner is None:
            money_change = money - self.price
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money_change:.2f}"
        elif money < self.price:
            return "Sorry, not enough money"
        elif self.owner is not None:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        elif self.owner is None:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        elif self.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price}"
