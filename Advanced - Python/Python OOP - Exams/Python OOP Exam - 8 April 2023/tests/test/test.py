from tests.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer("Tamer", 25, 100)

    def test_successful_initialization(self):
        self.assertEqual("Tamer", self.player.name)
        self.assertEqual(25, self.player.age)
        self.assertEqual(100, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_with_less_than_or_equal_to_2_symbols_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Ta"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_less_than_18_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_successful_add_tournament_names(self):
        self.player.add_new_win("big")
        self.assertEqual(["big"], self.player.wins)

        self.player.add_new_win("and")
        self.assertEqual(["big", "and"], self.player.wins)

        self.player.add_new_win("shiny")
        self.assertEqual(["big", "and", "shiny"], self.player.wins)

        self.assertEqual(3, len(self.player.wins))

    def test_add_existing_tournament_name(self):
        self.player.add_new_win("big")

        self.assertEqual("big has been already added to the list of wins!",
                         self.player.add_new_win("big"))

    def test__lt__(self):
        big_and_shiny = TennisPlayer("Shiny", 25, 105)

        expected = 'Shiny is a top seeded player and he/she is better than Tamer'
        actual = self.player < big_and_shiny

        self.assertEqual(expected, actual)

    def test__lt__self_player_with_more_points(self):
        big_and_shiny = TennisPlayer("Shiny", 25, 99)

        expected = 'Tamer is a better player than Shiny'
        actual = self.player < big_and_shiny

        self.assertEqual(expected, actual)

    def test__str__(self):
        tournaments = ["big", "and", "shiny"]

        for name in tournaments:
            self.player.add_new_win(name)

        expected = f"Tennis Player: Tamer\n" \
                   f"Age: 25\n" \
                   f"Points: 100.0\n" \
                   f"Tournaments won: big, and, shiny"

        self.assertEqual(expected, str(self.player))

if __name__ == "__main__":
    main()