from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):

    def setUp(self) -> None:
        self.team = Team("Tamer")

    def test_successful_initialization(self):
        self.assertEqual("Tamer", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_with_numbers_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Tamer123"
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_successfully_add_member(self):
        actual = self.team.add_member(Tamer=25)
        self.assertEqual({"Tamer": 25}, self.team.members)
        self.assertEqual("Successfully added: Tamer", actual)

    def test_successfully_remove_member(self):
        self.team.add_member(Tamer=25)
        actual = self.team.remove_member("Tamer")
        self.assertEqual({}, self.team.members)
        self.assertEqual("Member Tamer removed", actual)

    def test_remove_member_with_non_existent_name(self):
        actual = self.team.remove_member("Tamer")
        self.assertEqual("Member with name Tamer does not exist", actual)

    def test__gt__(self):
        self.team.add_member(Tamer=25)
        self.other = Team("Other")
        actual = self.team.__gt__(self.other)
        self.assertEqual(True, actual)

        self.team.remove_member("Tamer")
        self.assertEqual(False, self.team.__gt__(self.other))

    def test__len__(self):
        self.assertEqual(0, self.team.__len__())

        self.team.add_member(Tamer=25)
        self.assertEqual(1, self.team.__len__())

    def test__add__(self):
        self.other = Team("Other")
        self.other.add_member(Petko=20)
        self.team.add_member(Tamer=20)

        new_team = self.team.__add__(self.other)

        self.assertEqual("TamerOther", new_team.name)
        self.assertEqual({"Tamer": 20, "Petko": 20}, new_team.members)
        self.assertEqual(2, len(new_team.members))

    def test__str__(self):
        self.team.add_member(Other=30)
        self.team.add_member(Petko=25)
        self.team.add_member(Tamer=20)

        expected = "Team name: Tamer\n" \
                   "Member: Other - 30-years old\n" \
                   "Member: Petko - 25-years old\n" \
                   "Member: Tamer - 20-years old"
        self.assertEqual(expected, str(self.team))


if __name__ == "__main__":
    main()
