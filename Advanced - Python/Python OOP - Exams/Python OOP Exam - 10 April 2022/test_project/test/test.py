from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("Tamer", 2000, 10.0)

    def test_successful_initialization(self):
        self.assertEqual("Tamer", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(10.0, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_value_error_with_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_setter_value_error_with_year_lower_than_1887(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_successful_add_actor(self):
        self.movie.add_actor("Tamer")
        self.assertEqual(["Tamer"], self.movie.actors)
        self.assertEqual(1, len(self.movie.actors))

    def test_add_actor_already_added(self):
        self.movie.add_actor("Tamer")
        actual = self.movie.add_actor("Tamer")

        self.assertEqual("Tamer is already added in the list of actors!", actual)

    def test__gt__(self):
        self.other_movie = Movie("Other", 2000, 8.5)
        actual = self.movie.__gt__(self.other_movie)
        self.assertEqual('"Tamer" is better than "Other"', actual)

        self.other_movie.rating = 20
        actual_two = self.movie.__gt__(self.other_movie)
        self.assertEqual('"Other" is better than "Tamer"', actual_two)

    def test__repr__(self):
        self.movie.add_actor("Tamer")

        actual = self.movie.__repr__()
        expected = f"Name: Tamer\n" \
                   f"Year of Release: 2000\n" \
                   f"Rating: 10.00\n" \
                   f"Cast: Tamer"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
