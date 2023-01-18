from unittest import TestCase, main
from project.train.train import Train


class TestTrain(TestCase):

    def setUp(self) -> None:
        self.train = Train("Tamer", 10)

    def test_successful_initialization(self):
        self.assertEqual("Tamer", self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_train_with_full_capacity_value_error(self):
        self.train.capacity = 1
        self.train.passengers.append("2")
        with self.assertRaises(ValueError) as ve:
            self.train.add("3")
        self.assertEqual("Train is full", str(ve.exception))

    def test_train_with_same_passenger_value_error(self):
        self.train.add("Tamer")
        with self.assertRaises(ValueError) as ve:
            self.train.add("Tamer")
        self.assertEqual("Passenger Tamer Exists", str(ve.exception))

    def test_successful_add_passenger(self):
        actual = self.train.add("Tamer")
        self.assertEqual(["Tamer"], self.train.passengers)
        self.assertEqual("Added passenger Tamer", actual)

    def test_remove_passenger_that_doesnt_exist_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Tamer")
        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_successful_remove_passenger(self):
        self.train.add("Tamer")
        self.assertEqual(["Tamer"], self.train.passengers)
        self.train.remove("Tamer")
        self.assertEqual([], self.train.passengers)
        self.train.add("Tamer")
        self.assertEqual("Removed Tamer", self.train.remove("Tamer"))


if __name__ == "__main__":
    main()