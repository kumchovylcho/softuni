from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self):
        self.plantation = Plantation(100)

    def test_successful_initialization(self):
        self.assertEqual(100, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_below_zero_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_successfully_hire_worker(self):
        self.assertEqual("Tamer successfully hired.", self.plantation.hire_worker("Tamer"))
        self.assertEqual(["Tamer"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

        self.plantation.hire_worker("Tamer_2")
        self.assertEqual(["Tamer", "Tamer_2"], self.plantation.workers)
        self.assertEqual(2, len(self.plantation.workers))

    def test_hire_worker_with_same_name_twice_value_error(self):
        self.plantation.hire_worker("Tamer")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Tamer")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test__len__(self):
        self.plantation.plants = {"Tamer": ["test"], "Tamer_2": ["test_2"]}
        self.assertEqual(2, len(self.plantation))

        self.plantation.plants = {}
        self.assertEqual(0, len(self.plantation))

    def test_planting_worker_not_in_workers_list(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Tamer", "something")
        self.assertEqual("Worker with name Tamer is not hired!", str(ve.exception))

    def test_not_enough_space_in_plantation(self):
        self.plantation.size = 2
        self.plantation.workers = ["Tamer"]
        self.plantation.plants = {"Tamer": ["plant_1", "plant_2"]}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Tamer", "some_plant")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_successful_add_plant(self):
        self.plantation.workers = ["Tamer"]
        self.plantation.plants = {"Tamer": ["rose"]}

        actual = self.plantation.planting("Tamer", "rose_2")
        self.assertEqual("Tamer planted rose_2.", actual)

        self.assertEqual({"Tamer": ["rose", "rose_2"]}, self.plantation.plants)
        self.assertEqual(2, len(self.plantation.plants["Tamer"]))

    def test_first_time_plant_with_worker_not_existing(self):
        self.plantation.workers = ["Tamer"]

        actual = self.plantation.planting("Tamer", "rose")
        self.assertEqual("Tamer planted it's first rose.", actual)
        self.assertEqual({"Tamer": ["rose"]}, self.plantation.plants)
        self.assertEqual(1, len(self.plantation.plants))

    def test__str__(self):
        self.plantation.workers = ["Tamer", "Tamer_2"]
        self.plantation.plants = {"Tamer": ["rose", "rose_2"]}

        expected = "Plantation size: 100\n" \
                   "Tamer, Tamer_2\n" \
                   "Tamer planted: rose, rose_2"
        self.assertEqual(expected, str(self.plantation))

    def test__repr__(self):
        self.plantation.workers = ["Tamer", "Tamer_2"]

        expected = "Size: 100\n" \
                   "Workers: Tamer, Tamer_2"
        self.assertEqual(expected, self.plantation.__repr__())


if __name__ == "__main__":
    main()