from unittest import (TestCase,
                      main
                      )

from project.second_hand_car import SecondHandCar


class TestCar(TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar("skoda",
                                 "hatchback",
                                 40_000,
                                 40_000,
                                 )

    def test_successfully_initialize(self):
        self.assertEqual(self.car.model, "skoda")
        self.assertEqual(self.car.car_type, "hatchback")
        self.assertEqual(self.car.mileage, 40_000)
        self.assertEqual(self.car.price, 40_000)
        self.assertEqual(self.car.repairs, [])

    def test_price_of_car_is_lower_than_1_throw_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual(str(ve.exception),
                         'Price should be greater than 1.0!'
                         )

    def test_mileage_of_car_with_less_than_100_throw_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual(str(ve.exception),
                         'Please, second-hand cars only! Mileage must be greater than 100!'
                         )

    def test_set_promotional_price_higher_than_the_actual_price_throw_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(40_001)

        self.assertEqual(str(ve.exception),
                         'You are supposed to decrease the price!'
                         )

    def test_successfully_set_promotional_price(self):
        result = self.car.set_promotional_price(39_000)

        self.assertEqual(self.car.price, 39_000)
        self.assertEqual('The promotional price has been successfully set.',
                         result)

    def test_repair_price_higher_than_half_of_the_car_price_repair_impossible(self):
        result = self.car.need_repair(20_001, "broken head")

        self.assertEqual('Repair is impossible!',
                         result)

    def test_successfully_repair_car(self):
        result = self.car.need_repair(20_000, "broken head")

        self.assertEqual(self.car.price, 60_000)
        self.assertEqual(self.car.repairs, ["broken head"])
        self.assertEqual(result,
                         f'Price has been increased due to repair charges.')

    def test_gt_cars_cannot_be_compared(self):
        other_car = SecondHandCar("skoda",
                                 "coupe",
                                 40_000,
                                 40_000,
                                 )

        result = self.car > other_car
        self.assertEqual(result,
                         'Cars cannot be compared. Type mismatch!')

    def test_successfully_return_gt_boolean(self):
        other_car = SecondHandCar("skoda",
                                  "hatchback",
                                  40_000,
                                  40_000,
                                  )

        result = self.car > other_car
        self.assertEqual(False, result)

        self.car.price = 41_000
        result_2 = self.car > other_car
        self.assertEqual(True, result_2)

    def test_str(self):
        result = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""

        self.assertEqual(self.car.__str__(),
                         result)

if __name__ == "__main__":
    main()