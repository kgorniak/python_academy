import unittest
from oop.calculate_fuel import calculate_fuel


class MyTestCase(unittest.TestCase):

    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here
    #
    # def test_something2(self):
    #     self.assertEqual(True, True)
    #
    # def test_3(self):
    #     self.assertEqual(1, 2)

    def test_calc_fuel_1(self):
        self.assertEqual(2, calculate_fuel(12))

    def test_calc_fuel_2(self):
        self.assertEqual(654, calculate_fuel(1969))

    def test_calc_fuel_3(self):
        self.assertEqual(False, calculate_fuel(-1))

    def test_calc_fuel_4(self):
        self.assertEqual(False, calculate_fuel(0))

    def test_calc_fuel_5(self):
        self.assertEqual(False, calculate_fuel("test"))

    # def test_calc_fuel_6(self):
    #     self.assertEqual(False, calculate_fuel(1, 2))

    def test_calc_fuel_7(self):
        self.assertEqual(1, calculate_fuel(1))

    def test_calc_fuel_8(self):
        self.assertEqual(False, calculate_fuel(12.5))


if __name__ == '__main__':
    unittest.main()
