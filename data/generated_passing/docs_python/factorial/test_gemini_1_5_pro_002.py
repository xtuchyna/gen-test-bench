import unittest
import math

class TestFactorial(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(math.factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(math.factorial(1), 1)
        self.assertEqual(math.factorial(2), 2)
        self.assertEqual(math.factorial(5), 120)
        self.assertEqual(math.factorial(10), 3628800)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            math.factorial(-1)
        with self.assertRaises(ValueError):
            math.factorial(-5)
