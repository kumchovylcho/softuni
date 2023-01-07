from unittest import TestCase, main


class TestList(TestCase):

    def setUp(self):
        self.integer = IntegerList(1, '1', False, [], 2, (), 1.2)

    def test_check_successful_initialization(self):
        expected = [1, 2]
        actual = self.integer.get_data()
        self.assertEqual(expected, actual)

    def test_add_operation_should_add_element_and_return_list(self):
        expected = self.integer.get_data() + [5]
        self.integer.add(5)
        self.assertEqual(expected, self.integer.get_data())

    def test_add_operation_if_you_give_non_integer(self):
        expected = "Element is not Integer"

        with self.assertRaises(ValueError) as ex:
            self.integer.add('5')
        self.assertEqual(expected, str(ex.exception))

    def test_if_index_gets_removed(self):
        expected = 2
        self.assertEqual(expected, self.integer.remove_index(1))

    def test_check_if_index_is_out_of_range(self):
        expected = "Index is out of range"

        with self.assertRaises(IndexError) as ex:
            self.integer.remove_index(8)

        self.assertEqual(expected, str(ex.exception))

    def test_if_get_method_throws_index_error(self):
        expected = "Index is out of range"

        with self.assertRaises(IndexError) as ie:
            self.integer.get(7)

        self.assertEqual(expected, str(ie.exception))

    def test_if_get_method_returns_specific_element(self):
        expected = 1
        actual = self.integer.get(0)
        self.assertEqual(expected, actual)

    def test_if_insert_method_throws_index_error(self):
        expected = "Index is out of range"

        with self.assertRaises(IndexError) as ie:
            self.integer.insert(107, 5)

        self.assertEqual(expected, str(ie.exception))

    def test_if_insert_method_throws_value_error(self):
        expected = "Element is not Integer"

        with self.assertRaises(ValueError) as ve:
            self.integer.insert(1, "S")

        self.assertEqual(expected, str(ve.exception))

    def test_if_insert_method_returns_correct_information(self):
        expected = [3, 1, 2]
        self.integer.insert(0, 3)
        actual = self.integer.get_data()
        self.assertEqual(expected, actual)

    def test_if_get_biggest_method_return_the_biggest_number(self):
        expected = 2
        actual = self.integer.get_biggest()
        self.assertEqual(expected, actual)

    def test_if_get_index_returns_correct_element(self):
        expected = 1
        actual = self.integer.get_index(2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()