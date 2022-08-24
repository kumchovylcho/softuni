class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [word for word in self.products if word[0] == first_letter]

    def __repr__(self):
        show_result = "Items in the {} catalogue:\n" \
                      "{}".format(self.name, '\n'.join(sorted(self.products)))
        return show_result


