from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.cart = ShoppingCart("Tamer", 100.0)

    def test_successful_initialization(self):
        self.assertEqual("Tamer", self.cart.shop_name)
        self.assertEqual(100.0, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_first_letter_of_shop_name_lower_letter_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "tamer"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_contains_numbers_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "Tamer10"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_product_to_cart_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("idk", 100)
        self.assertEqual("Product idk cost too much!", str(ve.exception))

    def test_successful_add_product_to_cart(self):
        actual_1 = self.cart.add_to_cart("idk", 50)
        actual_2 = self.cart.add_to_cart("idk_2", 50)

        self.assertEqual(2, len(self.cart.products))
        self.assertEqual({"idk": 50, "idk_2": 50}, self.cart.products)

        self.assertEqual("idk product was successfully added to the cart!", actual_1)
        self.assertEqual("idk_2 product was successfully added to the cart!", actual_2)

    def test_remove_product_from_car_that_does_not_exist_value_error(self):
        self.cart.products = {"bomba": 1}

        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("idk")

        self.assertEqual("No product with name idk in the cart!", str(ve.exception))

    def test_successful_remove_product_from_cart(self):
        self.cart.products = {"idk": 10, "idk_2": 10}

        actual = self.cart.remove_from_cart("idk")

        self.assertEqual("Product idk was successfully removed from the cart!", actual)
        self.assertEqual({"idk_2": 10}, self.cart.products)
        self.assertEqual(1, len(self.cart.products))

    def test__add__method(self):
        self.cart.products = {"idk": 10}

        self.cart_2 = ShoppingCart("Tamer", 100)
        self.cart_2.products = {"idk_2": 10}

        new_cart = self.cart.__add__(self.cart_2)

        self.assertEqual("TamerTamer", new_cart.shop_name)
        self.assertEqual(200, new_cart.budget)
        self.assertEqual({"idk": 10, "idk_2": 10}, new_cart.products)

    def test_buy_products_not_enough_budget_value_error(self):
        self.cart.products = {"idk": 50, "idk_2": 40, "idk_3": 20}
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 10.00lv!", str(ve.exception))

    def test_successful_buy_products(self):
        self.cart.products = {"idk": 50, "idk_2": 40}

        actual = self.cart.buy_products()

        self.assertEqual("Products were successfully bought! Total cost: 90.00lv.", actual)


if __name__ == "__main__":
    main()