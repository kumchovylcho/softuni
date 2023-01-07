from unittest import TestCase, main


class CatTests(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Test")

    def test_cat_size_increase_after_eating(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_if_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)

    def test_cannot_eat_if_already_fed_catch_error(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cant_go_sleep_if_not_fed_catch_error(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == "__main__":
    main()