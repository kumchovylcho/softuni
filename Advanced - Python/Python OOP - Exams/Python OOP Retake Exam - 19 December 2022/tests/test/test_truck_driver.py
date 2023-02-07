from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver("Tamer", 1.20)

    def test_successful_initialization(self):
        self.assertEqual("Tamer", self.driver.name)
        self.assertEqual(1.20, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0.0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_cannot_be_lower_than_zero_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual("Tamer went bankrupt.", str(ve.exception))

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_add_cargo_offer_same_cargo_location_exception_error(self):
        self.driver.available_cargos["varna"] = 10
        self.driver.available_cargos["burgas"] = 20
        self.driver.available_cargos["ruse"] = 30

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("varna", 1)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_successful_add_cargo_offer(self):
        offers = (("varna", 10), ("burgas", 20), ("ruse", 30))
        for location, miles in offers:
            actual_msg = self.driver.add_cargo_offer(location, miles)
            self.assertEqual(f"Cargo for {miles} to {location} was added as an offer.", actual_msg)

        self.assertEqual({"varna": 10, "burgas": 20, "ruse": 30}, self.driver.available_cargos)
        self.assertEqual(3, len(self.driver.available_cargos))

    def test_drive_best_cargo_offer_no_offers_value_error(self):
        self.assertEqual("There are no offers available.", self.driver.drive_best_cargo_offer())

    def test_drive_best_cargo_offer(self):
        offers = (("varna", 10), ("burgas", 40))
        for location, miles in offers:
            self.driver.add_cargo_offer(location, miles)

        actual_msg = self.driver.drive_best_cargo_offer()

        self.assertEqual("Tamer is driving 40 to burgas.", actual_msg)
        self.assertEqual(48, self.driver.earned_money)
        self.assertEqual(40, self.driver.miles)

    def test_check_for_activities(self):
        self.driver.earned_money = 100_000

        self.driver.check_for_activities(10000)
        self.assertEqual(88250, self.driver.earned_money)

        self.driver.earned_money = 100_000

        self.driver.check_for_activities(1500)
        self.assertEqual(99335, self.driver.earned_money)

        self.driver.earned_money = 100_000

        self.driver.check_for_activities(1000)
        self.assertEqual(99875, self.driver.earned_money)

        self.driver.earned_money = 100_000

        self.driver.check_for_activities(250)
        self.assertEqual(99980, self.driver.earned_money)

    def test__repr__(self):
        self.assertEqual("Tamer has 0 miles behind his back.", str(self.driver))


if __name__ == "__main__":
    main()