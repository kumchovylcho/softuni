from unittest import TestCase, main
from hash_table import HashTable


class TestHashTable(TestCase):

    def setUp(self) -> None:
        self.table = HashTable()

    def test_init(self):
        self.assertEqual(4, len(self.table.table))
        self.assertEqual(0, self.table.item_counter)

    def test_hash(self):
        self.assertTrue(int, self.table.hash('name'))

        keys = ['name', 'name1', 'stock', 'video_card', 'cpu', 'last']
        for key in keys:
            index = self.table.hash(key)

            self.assertTrue(0 <= index < len(self.table.table))

    def test_double_table_space(self):
        self.table['name'] = 'Tamer'

        self.assertEqual(4 ,len(self.table.table))

        self.table.double_table_space()

        self.assertEqual(8, len(self.table.table))

        self.assertIn([['name', 'Tamer']], self.table.table)

    def test_add_successful_key_value(self):
        self.table.add('name', 'Tamer')

        self.assertIn([['name', 'Tamer']], self.table.table)

    def test_add_with_same_key_and_different_value(self):
        self.table['name'] = 'Tamer'

        self.assertIn([['name', 'Tamer']], self.table.table)

        self.table['name'] = "Tomi"

        self.assertIn([['name', 'Tomi']], self.table.table)
        self.assertNotIn([['name', 'Tamer']], self.table.table)

    def test_successful_get(self):
        self.table['name'] = 'Tamer'

        self.assertEqual('Tamer', self.table.get('name'))

    def test_get_with_wrong_key(self):
        with self.assertRaises(KeyError) as ke:
            self.table.get('some_key')

        self.assertEqual(str(ke.exception), "'key does not exist'")


if __name__ == '__main__':
    main()