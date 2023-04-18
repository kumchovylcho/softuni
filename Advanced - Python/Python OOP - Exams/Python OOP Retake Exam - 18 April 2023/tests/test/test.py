from tests.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):

    def setUp(self):
        self.robot = Robot("1", "Military", 10, 0)

    def test_successful_initialization(self):
        self.assertEqual("1", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(0, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_wrong_category_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "fish"

        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_setter_price_lower_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_unsuccessful_robot_upgrade(self):
        self.robot.hardware_upgrades = ["swim", "live", "torpedo"]

        actual = self.robot.upgrade("swim", 20)
        expected = "Robot 1 was not upgraded."

        self.assertEqual(actual, expected)

    def test_successfully_upgrade_robot(self):
        actual_1 = self.robot.upgrade("swim", 10)
        expected_1 = f'Robot 1 was upgraded with swim.'

        self.assertEqual(["swim"], self.robot.hardware_upgrades)
        self.assertEqual(actual_1, expected_1)
        self.assertEqual(1, len(self.robot.hardware_upgrades))
        self.assertEqual(15, self.robot.price)


        actual_2 = self.robot.upgrade("smarter", 10)
        expected_2 = f'Robot 1 was upgraded with smarter.'

        self.assertEqual(["swim", "smarter"], self.robot.hardware_upgrades)
        self.assertEqual(actual_2, expected_2)
        self.assertEqual(2, len(self.robot.hardware_upgrades))
        self.assertEqual(30, self.robot.price)

    def test_unsuccessful_robot_update_with_existent_software_updates(self):
        self.robot.software_updates = [1, 2, 3]

        actual = self.robot.update(3, 5)
        expected = "Robot 1 was not updated."

        self.assertEqual(actual, expected)

    def test_unsuccessful_robot_update_with_empty_software_updates(self):
        actual = self.robot.update(3, 11)
        expected = "Robot 1 was not updated."

        self.assertEqual(actual, expected)

    def test_successful_update_robot(self):
        actual_1 = self.robot.update(1, 1)
        expected_1 = f'Robot 1 was updated to version 1.'

        self.assertEqual(1, len(self.robot.software_updates))
        self.assertEqual([1], self.robot.software_updates)
        self.assertEqual(actual_1, expected_1)
        self.assertEqual(9, self.robot.available_capacity)


        actual_2 = self.robot.update(2, 2)
        expected_2 = f'Robot 1 was updated to version 2.'

        self.assertEqual(2, len(self.robot.software_updates))
        self.assertEqual([1, 2], self.robot.software_updates)
        self.assertEqual(actual_2, expected_2)
        self.assertEqual(7, self.robot.available_capacity)

    def test__gt__self_robot_more_expensive(self):
        robot_2 = Robot("1", "Military", 10, 0)

        self.robot.price = 1

        actual = self.robot > robot_2
        expected = 'Robot with ID 1 is more expensive than Robot with ID 1.'

        self.assertEqual(actual, expected)

    def test__gt__self_robot_same_value_as_other_robot(self):
        robot_2 = Robot("1", "Military", 10, 0)

        actual = self.robot > robot_2
        expected = 'Robot with ID 1 costs equal to Robot with ID 1.'

        self.assertEqual(actual, expected)

    def test__gt__self_robot_lower_price_than_other_robot(self):
        robot_2 = Robot("1", "Military", 10, 1)

        actual = self.robot > robot_2
        expected = 'Robot with ID 1 is cheaper than Robot with ID 1.'

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    main()