import unittest
from oop.travel import Travel


class TravelTests(unittest.TestCase):

    def setUp(self) -> None:
        self.traveler = Travel("adam", "testowy", year_of_birth=1980, distance=9999)
        self.baby_traveler = Travel("baby", "yoda", 2021, 99999)
        self.student_traveler = Travel("jan", "student", 2000, 9999)

    def test_calculate_cost_without_discount(self):
        self.assertEqual(1000, self.traveler.calculate_cost())

    def test_calculate_cost_discount_for_baby(self):
        self.assertEqual(0, self.baby_traveler.calculate_cost())

    def test_calculate_cost_for_student(self):
        self.assertEqual(490, self.student_traveler.calculate_cost())

    def test_add_countries_and_print_passport(self):
        self.assertFalse(self.traveler.passport)
        self.traveler.passport = ["Japan", "Korea", "Japan", "Thailand"]
        self.assertEqual({'Japan': 2, 'Korea': 1, 'Thailand': 1}, self.traveler.passport)
        self.traveler.passport = ["Korea", "Japan", "Japan"]
        self.assertEqual({'Japan': 4, 'Korea': 2, 'Thailand': 1}, self.traveler.passport)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
