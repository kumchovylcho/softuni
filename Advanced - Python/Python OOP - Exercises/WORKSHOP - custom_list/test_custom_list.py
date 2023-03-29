from custom_list import CustomList
from unittest import TestCase, main


class TestCustomList(TestCase):

    def setUp(self) -> None:
        self.list = CustomList()

    def test_successful_append(self):
        self.assertEqual(self.list.append("1"), self.list.list)
        self.assertEqual(self.list.append("2"), self.list.list)
        self.assertEqual(self.list.append("3"), self.list.list)

        self.assertEqual(3, len(self.list.list))
        self.assertEqual(['1', '2', '3'], self.list.list)

    def test_remove_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.list.remove(1)

        self.assertEqual(str(ie.exception), "Index out of range")

    def test_successfully_remove_item(self):
        test_items = ("1", "2", "3")
        for item in test_items:
            self.list.append(item)

        self.assertEqual(self.list.remove(2), "3")
        self.assertEqual(["1", "2"], self.list.list)

    def test_get_item_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.list.get(1)

        self.assertEqual(str(ie.exception), "Index out of range")

    def test_successfully_get_item(self):
        test_items = ("1", "2", "3")
        for item in test_items:
            self.list.append(item)

        self.assertEqual("2", self.list.get(1))

    def test_extend(self):
        test_items = ("1", "2", "3")
        for item in test_items:
            self.list.append(item)

        self.list.list.extend("4")

        self.assertEqual(["1", "2", "3", "4"], self.list.list)
        self.assertEqual(4, len(self.list.list))

    def test_insert_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(1, "idk")

        self.assertEqual(str(ie.exception), "Index out of range")

    def test_successfully_insert_value(self):
        test_items = ["1", "2"]
        for item in test_items:
            self.list.append(item)

        self.list.list.insert(0, "idk")
        self.assertEqual(["idk", '1', '2'], self.list.list)

    def test_pop_from_empty_list_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.list.pop()

        self.assertEqual(str(ve.exception), "List is empty")

    def test_successfully_pop_item(self):
        test_items = ["1", "2"]
        for item in test_items:
            self.list.append(item)

        self.list.pop()

        self.assertEqual(["1"], self.list.list)
        self.assertEqual(1, len(self.list.list))

    def test_clear_list(self):
        test_items = ["1", "2"]
        for item in test_items:
            self.list.append(item)

        self.assertEqual(["1", "2"], self.list.list)

        self.list.clear()

        self.assertEqual([], self.list.list)

    def test_index(self):
        expected_index = None
        actual_index = self.list.index(4)

        self.assertEqual(expected_index, actual_index)


        test_items = ["1", "2"]
        for item in test_items:
            self.list.append(item)

        expected_index = 0
        actual_index = self.list.index("1")

        self.assertEqual(expected_index, actual_index)


    def test_count(self):
        test_items = ["1", "2", "2", "3", 2, 3]
        for item in test_items:
            self.list.append(item)

        expected = 2
        actual = self.list.count("2")

        self.assertEqual(expected, actual)

    def test_reverse(self):
        test_items = [1, 2, 3]
        for item in test_items:
            self.list.append(item)

        expected = self.list.reverse()

        self.assertEqual([3, 2, 1], expected)

    def test_copy(self):
        test_items = [1, 2, 3]
        for item in test_items:
            self.list.append(item)

        expected = [1, 2, 3]
        actual = self.list.copy()

        self.assertEqual(expected, actual)

    def test_size(self):
        test_items = [1, 2, 3]
        for item in test_items:
            self.list.append(item)

        expected = 3
        actual = self.list.size()

        self.assertEqual(expected, actual)

    def test_add_first(self):
        test_items = [1, 2, 3]
        for item in test_items:
            self.list.append(item)

        expected = ["idk", 1, 2, 3]
        self.list.add_first("idk")

        self.assertEqual(expected, self.list.list)

    def test_dictionize_odd_items(self):
        test_items = [1, 2, 3]
        for item in test_items:
            self.list.append(item)

        expected = {1: 2,
                    3: " "}
        actual = self.list.dictionize()

        self.assertEqual(expected, actual)

    def test_dictionize_even_items(self):
        test_items = [1, 2, 3, 4]
        for item in test_items:
            self.list.append(item)

        expected = {1: 2,
                    3: 4}
        actual = self.list.dictionize()

        self.assertEqual(expected, actual)

    def test_move_amount_invalid_index(self):
        test_items = [1, 2, 3, 4]
        for item in test_items:
            self.list.append(item)

        with self.assertRaises(IndexError) as ie:
            self.list.move(4)

        self.assertEqual(str(ie.exception), "Index out of range")

    def test_successful_move(self):
        test_items = [1, 2, 3]
        for item in test_items:
            self.list.append(item)

        expected = [3, 1, 2]
        actual = self.list.move(2)

        self.assertEqual(expected, actual)

    def test_sum(self):
        test_items = [1, "idk", 3]
        for item in test_items:
            self.list.append(item)

        expected = 7
        actual = self.list.sum()

        self.assertEqual(expected, actual)

    def test_overbound(self):
        test_items = [1, "idk", 3]
        for item in test_items:
            self.list.append(item)

        expected = 1
        actual = self.list.overbound()

        self.assertEqual(expected, actual)

    def test_underbound(self):
        test_items = [10, "idk", 3, -2]
        for item in test_items:
            self.list.append(item)

        expected = 3
        actual = self.list.underbound()

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    main()