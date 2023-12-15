from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("Garata")

    def test_successful_initialization(self):
        self.assertEqual("Garata", self.station.name)
        self.assertEqual(0, len(self.station.arrival_trains))
        self.assertEqual(0, len(self.station.departure_trains))

    def test_value_error_when_name_is_less_than_4_chars(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "123"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_train_arrives_before_other_train(self):
        self.station.arrival_trains.append("vlak")

        response = self.station.train_has_arrived("vlak-1")
        self.assertEqual("There are other trains to arrive before vlak-1.", response)

    def test_successful_train_arrival(self):
        self.station.arrival_trains.append("vlak")

        response = self.station.train_has_arrived("vlak")
        self.assertEqual("vlak is on the platform and will leave in 5 minutes.", response)

        self.assertEqual(1, len(self.station.departure_trains))
        self.assertEqual(0, len(self.station.arrival_trains))

    def test_successful_train_departure(self):
        self.station.departure_trains.append("vlak")

        response = self.station.train_has_left("vlak")

        self.assertEqual(True, response)
        self.assertEqual(0, len(self.station.departure_trains))

    def test_not_successful_train_departure(self):
        self.station.departure_trains.append("vlak")

        response = self.station.train_has_left("vlak-1")

        self.assertEqual(False, response)
        self.assertEqual(1, len(self.station.departure_trains))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("vlak")

        self.assertEqual(1, len(self.station.arrival_trains))

if __name__ == '__main__':
    main()