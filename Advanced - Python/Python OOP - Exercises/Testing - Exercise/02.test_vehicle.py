from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(10.0, 150.0)

    def test_successful_initialization(self):
        self.assertEqual(10.0, self.vehicle.fuel)
        self.assertEqual(10.0, self.vehicle.capacity)
        self.assertEqual(150.0, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_method_not_enough_fuel_exception(self):
        expected = "Not enough fuel"
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(800)
        self.assertEqual(expected, str(ex.exception))

    def test_drive_method_lower_fuel_after_driving(self):
        expected = 3.75
        self.vehicle.drive(5)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_refuel_method_refuel_more_than_capacity(self):
        expected = "Too much fuel"
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(200)
        self.assertEqual(expected, str(ex.exception))

    def test_if_refuel_method_adds_fuel(self):
        self.vehicle.drive(1)
        expected = 9.75   # drives 1km and wastes 1.25 fuel then we refuel with 1 liter = 9.75
        self.vehicle.refuel(1)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_str_method(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected, self.vehicle.__str__())


if __name__ == "__main__":
    main()
