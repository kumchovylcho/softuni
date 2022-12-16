class Cup:

    def __init__(self, size: int, quantity: int):
        self.size = int(size)
        self.quantity = int(quantity)

    def fill(self, milliliters):
        if self.quantity + milliliters <= self.size:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity
