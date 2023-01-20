from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.shop = PetShop("Tamer")

    def test_successful_initialization(self):
        self.assertEqual("Tamer", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_quantity_lower_or_equal_than_zero_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("banana", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_successful_add_food(self):
        actual = self.shop.add_food("banana", 10)
        self.assertEqual({"banana": 10}, self.shop.food)
        self.assertEqual("Successfully added 10.00 grams of banana.", actual)
        self.shop.add_food("banana", 10)
        self.assertEqual({"banana": 20}, self.shop.food)

    def test_add_pet_with_the_same_name_raise_exception(self):
        self.shop.add_pet("Tom")
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Tom")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_successful_add_pet(self):
        actual = self.shop.add_pet("Tom")
        self.assertEqual(["Tom"], self.shop.pets)
        self.assertEqual(1, len(self.shop.pets))
        self.assertEqual("Successfully added Tom.", actual)

    def test_name_not_in_pets_list_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("banana", "Tom")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_non_existent_food_name_in_food_list(self):
        self.shop.add_pet("Tom")
        self.assertEqual("You do not have banana", self.shop.feed_pet("banana", "Tom"))

    def test_food_lower_than_100_so_it_adds_food(self):
        self.shop.add_pet("Tom")
        self.shop.add_food("banana", 50)
        actual = self.shop.feed_pet("banana", "Tom")
        self.assertEqual({"banana": 1050.0}, self.shop.food)
        self.assertEqual("Adding food...", actual)

    def test_successful_feed_pet(self):
        self.shop.add_pet("Tom")
        self.shop.add_food("banana", 500)
        actual = self.shop.feed_pet("banana", "Tom")
        self.assertEqual({"banana": 400}, self.shop.food)
        self.assertEqual("Tom was successfully fed", actual)

    def test_repr(self):
        self.shop.add_pet("Tom")
        self.shop.add_pet("Bom")
        expected = "Shop Tamer:\n" \
                   "Pets: Tom, Bom"
        self.assertEqual(expected, str(self.shop))


if __name__ == "__main__":
    main()

