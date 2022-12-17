class Glass:
    content = 0
    capacity = 250

    def fill(self, fill_amount):
        if self.content + fill_amount <= self.capacity:
            self.content += fill_amount
            return f"Glass filled with {fill_amount} ml"
        return f"Cannot add {fill_amount} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{self.capacity - self.content} ml left"
