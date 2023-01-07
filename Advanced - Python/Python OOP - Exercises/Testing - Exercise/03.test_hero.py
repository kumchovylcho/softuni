from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Bro", 1, 100, 100)
        self.enemy_hero = Hero("Sister", 1, 50, 50)

    def test_successful_initialization(self):
        self.assertEqual("Bro", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_hero_battle_with_same_username(self):
        expected = "You cannot fight yourself"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(expected, str(ex.exception))

    def test_if_health_is_lower_or_equal_to_0(self):
        expected = "Your health is lower than or equal to 0. You need to rest"
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(expected, str(ve.exception))

    def test_if_enemy_hero_has_hp_lower_or_equal_to_0(self):
        expected = f"You cannot fight {self.enemy_hero.username}. He needs to rest"
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(expected, str(ve.exception))

    def test_if_both_players_health_reaches_zero_or_lower(self):
        self.hero.damage = 9999
        self.enemy_hero.damage = 9999
        expected = "Draw"
        actual = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected, actual)

    def test_if_hero_kills_enemy_player(self):
        self.hero.damage = 2000
        self.hero.health = 9999
        expected = "You win"
        actual = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected, actual)

    def test_if_hero_gains_stats_after_a_win(self):
        self.hero.health = 1000
        self.hero.damage = 1000
        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy_hero.damage + 5
        expected_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)
        self.assertEqual("You win", result)

    def test_if_hero_looses_battle_and_enemy_gains_stats(self):
        self.enemy_hero.health = 500
        self.enemy_hero.damage = 800
        self.enemy_hero.level = 20
        expected_lvl = self.enemy_hero.level + 1
        expected_health = self.enemy_hero.health - self.hero.damage + 5
        expected_dmg = self.enemy_hero.damage + 5
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_lvl, self.enemy_hero.level)
        self.assertEqual(expected_health, self.enemy_hero.health)
        self.assertEqual(expected_dmg, self.enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_str_method(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected, self.hero.__str__())


if __name__ == "__main__":
    main()