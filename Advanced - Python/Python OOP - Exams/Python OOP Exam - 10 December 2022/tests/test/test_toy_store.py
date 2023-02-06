from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_successful_initialization(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
            , self.store.toy_shelf)

    def test_add_toy_shelf_not_in_toy_shelf_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("non existent", "doesnt matter")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_that_already_exists_exception_error(self):
        self.store.toy_shelf["A"] = "something is here"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "something is here")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_key_is_already_taken_exception_error(self):
        self.store.toy_shelf["A"] = "idk"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "doesnt matter")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_successful_add_toy(self):
        actual_1 = self.store.add_toy("A", "Tamer :D")

        self.assertEqual({
            "A": "Tamer :D",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)
        self.assertEqual("Tamer :D", self.store.toy_shelf["A"])
        self.assertEqual("Toy:Tamer :D placed successfully!", actual_1)

        actual_2 = self.store.add_toy("B", "Tamer :D")

        self.assertEqual({
            "A": "Tamer :D",
            "B": "Tamer :D",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)
        self.assertEqual("Tamer :D", self.store.toy_shelf["B"])
        self.assertEqual("Toy:Tamer :D placed successfully!", actual_2)

    def test_remove_toy_shelf_doesnt_exist_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("non existent", "doesnt matter")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_value_different_from_given_parameter_exception_error(self):
        self.store.toy_shelf["A"] = "Tamer :D"

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "different than Tamer :D")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_successful_remove_toy(self):
        self.store.add_toy("A", "Tamer")
        self.store.add_toy("B", "Tamer")

        actual_1 = self.store.remove_toy("A", "Tamer")

        self.assertEqual({
            "A": None,
            "B": "Tamer",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)
        self.assertEqual("Remove toy:Tamer successfully!", actual_1)

        actual_2 = self.store.remove_toy("B", "Tamer")

        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)
        self.assertEqual("Remove toy:Tamer successfully!", actual_2)


if __name__ == "__main__":
    main()
