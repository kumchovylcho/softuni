from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Shrek", "Monster", "Gwa")

    def test_successful_initialization(self):
        self.assertEqual("Shrek", self.mammal.name)
        self.assertEqual("Monster", self.mammal.type)
        self.assertEqual("Gwa", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound_method(self):
        expected = "Shrek makes Gwa"
        self.assertEqual(expected, self.mammal.make_sound())

    def test_get_kingdom(self):
        expected = "animals"
        self.assertEqual(expected, self.mammal.get_kingdom())

    def test_info_method(self):
        expected = "Shrek is of type Monster"
        self.assertEqual(expected, self.mammal.info())


if __name__ == "__main__":
    main()