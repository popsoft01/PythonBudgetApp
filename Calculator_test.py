import unittest

from PythonBudgetApp import Calculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, Calculator.add(2, 3))  # add assertion here

    def test_add2(self):
        self.assertEqual(5, Calculator.add(2, -3))

    def test_sub(self):
        self.assertEqual(3, Calculator.substract(5, 2))


if __name__ == '__main__':
    unittest.main()
