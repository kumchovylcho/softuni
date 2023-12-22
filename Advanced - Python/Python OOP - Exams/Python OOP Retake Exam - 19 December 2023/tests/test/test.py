from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):

    def setUp(self) -> None:
        self.robot = ClimbingRobot("Mountain", "metal", 100, 100)

    def test_successful_initialization(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("metal", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(100, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_bad_category_type_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Not in allowed"

        self.assertEqual(str(ve.exception), "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']")

    def test_get_used_capacity(self):
        self.robot.installed_software = [{"capacity_consumption": 50}, {"capacity_consumption": 50}]

        expected = 100
        actual = self.robot.get_used_capacity()
        self.assertEqual(expected, actual)

    def test_get_available_capacity(self):
        self.robot.installed_software = [{"capacity_consumption": 50}, {"capacity_consumption": 40}]

        expected = 10
        actual = self.robot.get_available_capacity()
        self.assertEqual(expected, actual)

    def test_get_used_memory(self):
        self.robot.installed_software = [{"memory_consumption": 50}, {"memory_consumption": 50}]

        expected = 100
        actual = self.robot.get_used_memory()
        self.assertEqual(expected, actual)

    def test_get_available_memory(self):
        self.robot.installed_software = [{"memory_consumption": 50}, {"memory_consumption": 40}]

        expected = 10
        actual = self.robot.get_available_memory()
        self.assertEqual(expected, actual)

    def test_successfully_install_software(self):
        software_to_be_installed = {"name": "windows", "capacity_consumption": 10, "memory_consumption": 10}
        expected_install_software = [{"name": "windows", "capacity_consumption": 10, "memory_consumption": 10}]

        response_msg = self.robot.install_software(software_to_be_installed)
        self.assertEqual(expected_install_software, self.robot.installed_software)
        self.assertEqual("Software 'windows' successfully installed on Mountain part.",
                         response_msg
                         )
        self.assertEqual(90, self.robot.get_available_capacity())
        self.assertEqual(10, self.robot.get_used_capacity())

    def test_unsuccessful_installed_software(self):
        software_to_be_installed = {"name": "windows", "capacity_consumption": 110, "memory_consumption": 110}
        expected_install_software = []
        response_msg = self.robot.install_software(software_to_be_installed)

        self.assertEqual(expected_install_software, self.robot.installed_software)
        self.assertEqual("Software 'windows' cannot be installed on Mountain part.",
                         response_msg
                         )

    def test_not_available_capacity_on_installation(self):
        software_to_be_installed = {"name": "windows", "capacity_consumption": 90, "memory_consumption": 10}
        self.robot.install_software(software_to_be_installed)

        response_msg = self.robot.install_software(software_to_be_installed)
        expected = "Software 'windows' cannot be installed on Mountain part."
        self.assertEqual(response_msg, expected)
        self.assertEqual([{"name": "windows", "capacity_consumption": 90, "memory_consumption": 10}], self.robot.installed_software)

    def test_not_available_memory_on_installation(self):
        software_to_be_installed = {"name": "windows", "capacity_consumption": 10, "memory_consumption": 90}
        self.robot.install_software(software_to_be_installed)

        response_msg = self.robot.install_software(software_to_be_installed)
        expected = "Software 'windows' cannot be installed on Mountain part."
        self.assertEqual(response_msg, expected)
        self.assertEqual([{"name": "windows", "capacity_consumption": 10, "memory_consumption": 90}], self.robot.installed_software)
if __name__ == '__main__':
    main()