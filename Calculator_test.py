import unittest

from PythonBudgetApp import Calculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, Calculator.add(2, 3))  # add assertion here

    def test_add_with_negative_num(self):
        self.assertEqual(-1, Calculator.add(2, -3))

    def test_add_with_two_zero(self):
        self.assertEqual(0, Calculator.add(0, 0))

    def test_sub(self):
        self.assertEqual(3, Calculator.substract(5, 2))


if __name__ == '__main__':
    unittest.main()
