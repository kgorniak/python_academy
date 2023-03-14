import unittest
from mobile.helpers import create_driver

from mobile.screens.home import HomePage


class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = create_driver("Android", "calculator.apk")
        self.home_page = HomePage(self.driver)

    def test_add_numbers(self):
        self.home_page.add_values(3, 5)
        self.assertEqual(self.home_page.get_result(), 8)

    def test_square_root_number(self):
        self.home_page.square_root(9)
        self.assertEqual(self.home_page.get_result(), 3)

    def test_natural_logarithm(self):
        self.home_page.natural_logarithm(2)
        self.assertEqual(self.home_page.get_result(), 0.69314718055)

    def test_tangent(self):
        self.home_page.tangent(3)
        self.assertEqual(self.home_page.get_result(), 0.05240777928)

    def test_add_big_numbers(self):
        self.home_page.add_big_numbers(123, 456, 789)
        self.assertEqual(self.home_page.get_result(), 1368)

    def test_add_many_numbers(self):
        self.home_page.add_many_numbers(3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(self.home_page.get_result(), 42)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
