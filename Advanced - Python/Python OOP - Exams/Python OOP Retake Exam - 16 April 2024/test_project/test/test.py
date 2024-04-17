from unittest import TestCase, main

from test_project.restaurant import Restaurant


class TestRestaurant(TestCase):

    def setUp(self) -> None:
        self.restaurant = Restaurant("Tamer", 10)

    def test_success_initialization(self):
        self.assertEqual("Tamer", self.restaurant.name)
        self.assertEqual(10, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_unsuccessful_initialization(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = ""
        self.assertEqual("Invalid name!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -1
        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_successfully_add_waiter(self):
        response = self.restaurant.add_waiter("Tamer")
        self.assertEqual(1, len(self.restaurant.waiters))
        self.assertEqual([{"name": "Tamer"}], self.restaurant.waiters)
        self.assertEqual(response, "The waiter Tamer has been added.")

    def test_add_waiter_when_waiter_already_exists(self):
        self.restaurant.add_waiter("Tamer")
        response = self.restaurant.add_waiter("Tamer")
        self.assertEqual("The waiter Tamer already exists!", response)

    def test_add_waiter_when_no_more_places(self):
        for i in range(10):
            self.restaurant.add_waiter(str(i))

        response = self.restaurant.add_waiter("Tamer")
        self.assertEqual("No more places!", response)

    def test_successfully_remove_waiter(self):
        self.restaurant.add_waiter("Tamer")
        self.assertEqual(1, len(self.restaurant.waiters))
        response = self.restaurant.remove_waiter("Tamer")
        self.assertEqual("The waiter Tamer has been removed.", response)
        self.assertEqual(0, len(self.restaurant.waiters))

    def test_remove_waiter_that_doesnt_exist(self):
        response = self.restaurant.remove_waiter("Tamer")
        self.assertEqual("No waiter found with the name Tamer.", response)

    def test_get_total_earnings(self):
        self.restaurant.waiters = [
            {"name": "Tamer", "total_earnings": 100},
            {"name": "Tamer2", "total_earnings": 50},
        ]
        response = self.restaurant.get_total_earnings()
        self.assertEqual(150, response)

    def test_waiters_without_min_or_max_earnings(self):
        self.restaurant.waiters = [
            {"name": "Tamer", "total_earnings": 100},
            {"name": "Tamer2", "total_earnings": 50},
        ]

        response = self.restaurant.get_waiters()
        self.assertEqual(2, len(response))

    def test_waiters_with_min_earnings(self):
        self.restaurant.waiters = [
            {"name": "Tamer", "total_earnings": 100},
            {"name": "Tamer2", "total_earnings": 50},
        ]

        response = self.restaurant.get_waiters(min_earnings=60)
        self.assertEqual(1, len(response))
        self.assertEqual([{"name": "Tamer", "total_earnings": 100}], response)

    def test_waiters_with_max_earnings(self):
        self.restaurant.waiters = [
            {"name": "Tamer", "total_earnings": 100},
            {"name": "Tamer2", "total_earnings": 50},
        ]

        response = self.restaurant.get_waiters(max_earnings=60)
        self.assertEqual(1, len(response))
        self.assertEqual([{"name": "Tamer2", "total_earnings": 50}], response)


if __name__ == '__main__':
    main()