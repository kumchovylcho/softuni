from tests.trip import Trip
from unittest import (TestCase,
                      main
                      )


class TestTrip(TestCase):

    def setUp(self) -> None:
        self.trip = Trip(budget=100,
                         travelers_number=10,
                         is_family=True
                         )

    def test_successful_initialization(self):
        self.assertEqual(self.trip.budget,
                         100
                         )

        self.assertEqual(self.trip.travelers,
                         10
                         )

        self.assertEqual(self.trip.is_family,
                         True
                         )

        self.assertEqual(self.trip.booked_destinations_paid_amounts,
                         {}
                         )

    def test_travelers_less_than_1_throw_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual(str(ve.exception),
                         'At least one traveler is required!'
                         )

    def test_is_family_with_True_and_more_than_2_travellers_should_set_to_True(self):
        self.assertEqual(self.trip.is_family,
                         True
                         )

    def test_is_family_with_True_and_less_than_2_travellers_should_set_to_False(self):
        self.trip.travelers = 1
        self.trip.is_family = True

        self.assertEqual(self.trip.is_family,
                         False
                         )

    def test_book_a_trip_with_wrong_destination(self):
        response = self.trip.book_a_trip("exit")

        self.assertEqual(response,
                         'This destination is not in our offers, please choose a new one!'
                         )

    def test_book_a_trip_with_valid_destination_and_not_enough_budget(self):
        response = self.trip.book_a_trip("Bulgaria")
        self.trip.is_family = True

        self.assertEqual(response,
                         'Your budget is not enough!'
                         )

    def test_book_a_trip_with_valid_destination_and_enough_budget(self):
        self.trip.budget = 10_000
        self.trip.is_family = True
        response = self.trip.book_a_trip("Bulgaria")

        self.assertEqual(response,
                         f'Successfully booked destination Bulgaria! Your budget left is 5500.00'
                         )

        self.assertEqual(self.trip.budget,
                         5500
                         )

        self.assertEqual({"Bulgaria": 4500},
                         self.trip.booked_destinations_paid_amounts
                         )

    def test_book_a_trip_with_valid_destination_and_enough_budget_and_not_family(self):
        self.trip.budget = 10_000
        self.trip.is_family = False
        response = self.trip.book_a_trip("Bulgaria")

        self.assertEqual(response,
                         'Successfully booked destination Bulgaria! Your budget left is 5000.00'
                         )

        self.assertEqual(self.trip.budget,
                         5000
                         )

        self.assertEqual({"Bulgaria": 5000},
                         self.trip.booked_destinations_paid_amounts
                         )

    def test_booking_status_with_empty_destinations(self):
        response = self.trip.booking_status()

        self.assertEqual(response,
                         'No bookings yet. Budget: 100.00'
                         )

    def test_booking_status_with_booked_destinations(self):
        self.trip.budget = 100_000

        self.trip.book_a_trip("Bulgaria")
        self.trip.book_a_trip("New Zealand")

        response = self.trip.booking_status()

        expected = """Booked Destination: Bulgaria
Paid Amount: 4500.00
Booked Destination: New Zealand
Paid Amount: 67500.00
Number of Travelers: 10
Budget Left: 28000.00"""

        self.assertEqual(response, expected)


if __name__ == '__main__':
    main()


