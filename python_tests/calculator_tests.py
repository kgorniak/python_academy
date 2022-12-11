import unittest
from oop.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(3, self.calculator.add(1, 3))

    def test_devide_by_0(self):
        self.assertEqual(False, self.calculator.devide(5, 0))

    def test_inverted_by_zero(self):
        self.assertEqual(False, self.calculator.inverted(0))

    def test_string(self):
        self.assertEqual(False, self.calculator.add("string", 5))

    def test_string2(self):
        self.assertEqual(False, self.calculator.add("string", "test"))

    def test_factorial_zero(self):
        self.assertEqual(1, self.calculator.factorial(0))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
