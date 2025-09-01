import unittest
from oop.person import Person, Student


class PersonTests(unittest.TestCase):

    def setUp(self) -> None:
        self.person = Person("Adam", "Testowy", 1990)

    def test_full_name(self):
        self.assertEqual("Adam Testowy", self.person.print_full_name())

    def test_return_age(self):
        self.assertEqual(str, type(self.person.return_age()))

    def test_change_name(self):
        self.person.surname = "Nietestowy"
        self.assertEqual("Nietestowy", self.person.surname)

    def tearDown(self) -> None:
        pass


class StudentTests(unittest.TestCase):

    def setUp(self) -> None:
        self.andrzej = Student("Andrzej", "Test", 1991, "#321")

    def test_no_grades(self):
        self.assertFalse(self.andrzej.initial_grades)

    def test_cleaning_grades(self):
        self.andrzej.add_grade(5)
        self.assertEqual(self.andrzej.calculate_final_grade(), 5)
        self.andrzej.clear_all_grades()
        self.assertFalse(self.andrzej.initial_grades)


if __name__ == '__main__':
    unittest.main()
