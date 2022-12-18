from project.product import Product


class ProductRepository:
    products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for item in self.products:
            if item.name == product_name:
                return item

    def remove(self, product_name):
        for item in self.products:
            if item.name == product_name:
                self.products.remove(item)
                break

    def __repr__(self):
        output = []
        for item in self.products:
            output.append(f"{item.name}: {item.quantity}")
        return '\n'.join(output)
