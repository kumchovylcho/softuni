from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudent(TestCase):

    def setUp(self):
        self.student = StudentReportCard("Tamer", 12)

    def test_successful_year(self):
        self.student.school_year = 1

        self.assertEqual(1, self.student.school_year)

    def test_successful_initialization(self):
        self.assertEqual("Tamer", self.student.student_name)
        self.assertEqual(12, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_for_error_with_empty_student_name(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_for_error_with_wrong_school_year(self):
        with self.assertRaises(ValueError) as ve:
            self.student.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_successful_add_grade(self):
        subject = "123"
        grade = 6.00
        self.student.add_grade(subject, grade)
        self.assertEqual({"123": [6.00]}, self.student.grades_by_subject)
        self.student.add_grade(subject, grade)
        self.assertEqual({"123": [6.00, 6.00]}, self.student.grades_by_subject)
        self.student.add_grade("456", 6.00)
        self.assertEqual({"123": [6.00, 6.00], "456": [6.00]}, self.student.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student.add_grade("123", 6.00)
        self.student.add_grade("456", 6.00)
        self.student.add_grade("789", 6.00)
        self.assertEqual([6.00], self.student.grades_by_subject["123"])
        self.assertEqual([6.00], self.student.grades_by_subject["456"])
        self.assertEqual([6.00], self.student.grades_by_subject["789"])
        self.assertEqual(1, len(self.student.grades_by_subject["123"]))
        self.assertEqual("123: 6.00\n"
                         "456: 6.00\n"
                         "789: 6.00", self.student.average_grade_by_subject())

    def test_empty_report_average_grade(self):
        self.assertEqual("", self.student.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        self.student.add_grade("123", 6.00)
        self.student.add_grade("456", 6.00)
        actual = self.student.average_grade_for_all_subjects()
        expected = "Average Grade: 6.00"
        self.assertEqual(expected, actual)
        self.assertEqual([6.00], self.student.grades_by_subject["123"])
        self.assertEqual([6.00], self.student.grades_by_subject["456"])
        self.assertEqual(1, len(self.student.grades_by_subject["123"]))

    def test_repr(self):
        self.student.add_grade("P - Basic", 6.00)
        self.student.add_grade("P - Basic", 6.00)
        self.student.add_grade("P - Fund", 6.00)

        result = self.student.__repr__()

        self.assertEqual("Name: Tamer\n"
                         "Year: 12\n"
                         "----------\n"
                         f"{self.student.average_grade_by_subject()}\n"
                         "----------\n"
                         f"{self.student.average_grade_for_all_subjects()}", result)


if __name__ == "__main__":
    main()
