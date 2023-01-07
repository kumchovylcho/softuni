from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):

    def setUp(self) -> None:
        self.factory = PaintFactory("Nothing", 100)

    def test_successful_initialization(self):
        self.assertEqual("Nothing", self.factory.name)
        self.assertEqual(100, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.products)

    def test_add_ingredients_not_enough_space(self):
        self.factory.capacity = 0
        with self.assertRaises(ValueError) as ve:
            self.factory.add_ingredient("white", 1)
        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_add_wrong_ingredient(self):
        with self.assertRaises(TypeError) as te:
            self.factory.add_ingredient("bomba", 1)
        expected = f"Ingredient of type bomba not allowed in {self.factory.__class__.__name__}"
        self.assertEqual(expected, str(te.exception))

    def test_successful_add_ingredient(self):
        expected = {"red": 1}
        self.factory.add_ingredient("red", 1)
        self.assertEqual(expected, self.factory.ingredients)

    def test_remove_ingredient_value_error_quantity_less_than_zero(self):
        self.factory.add_ingredient("red", 1)
        with self.assertRaises(ValueError) as ve:
            self.factory.remove_ingredient("red", 2)
        expected = "Ingredients quantity cannot be less than zero"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_ingredient_when_giving_non_existent_product(self):
        expected = "'No such ingredient in the factory'"
        with self.assertRaises(KeyError) as ke:
            self.factory.remove_ingredient("piramparamparo", 1)
        self.assertEqual(expected, str(ke.exception))

    def test_successful_remove_quantity_from_ingredient(self):
        self.factory.add_ingredient("red", 1)
        self.factory.remove_ingredient("red", 1)
        self.assertEqual({"red": 0}, self.factory.ingredients)


if __name__ == "__main__":
    main()
