class Account:

    def __init__(self, id: int, name, balance=0):
        self.id = int(id)
        self.name = name
        self.balance = int(balance)

    def credit(self, amount: int):
        self.balance += amount
        return self.balance

    def debit(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"
