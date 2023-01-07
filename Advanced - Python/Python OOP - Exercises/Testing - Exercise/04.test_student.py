from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Bro")
        self.student_with_courses = Student("Bro", {"english": ["1"]})

    def test_successful_initialization(self):
        self.assertEqual("Bro", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"english": ["1"]}, self.student_with_courses.courses)

    def test_if_course_is_already_added(self):
        expected = "Course already added. Notes have been updated."
        actual = self.student_with_courses.enroll("english", "1")
        self.assertEqual(expected, actual)

    def test_if_course_and_course_notes_have_been_added(self):
        expected = "Course and course notes have been added."
        actual = self.student_with_courses.enroll("bulgarian", "1", "Y")
        self.assertEqual(expected, actual)

    def test_if_course_and_course_notes_have_been_added_with_no_course_notes(self):
        expected = "Course and course notes have been added."
        actual = self.student_with_courses.enroll("bulgarian", "1")
        self.assertEqual(expected, actual)

    def test_if_course_name_has_been_created_with_empty_list(self):
        expected = "Course has been added."
        actual = self.student_with_courses.enroll("french", "5", "No")
        self.assertEqual(expected, actual)
        self.assertEqual([], self.student_with_courses.courses["french"])

    def test_if_notes_has_been_updated(self):
        expected = "Notes have been updated"
        actual = self.student_with_courses.add_notes("english", "2")
        self.assertEqual(expected, actual)

    def test_if_add_notes_throw_exception(self):
        expected = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.add_notes("imaginary", "X")
        self.assertEqual(expected, str(ex.exception))

    def test_if_course_has_been_removed(self):
        expected = "Course has been removed"
        actual = self.student_with_courses.leave_course("english")
        self.assertEqual(expected, actual)

    def test_if_leave_course_throws_exception(self):
        expected = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("IDK")
        self.assertEqual(expected, str(ex.exception))


if __name__ == "__main__":
    main()