import unittest
import math

class TestFactorial(unittest.TestCase):

    def test_factorial_of_zero(self):
        self.assertEqual(math.factorial(0), 1)

    def test_factorial_of_positive_integer(self):
        self.assertEqual(math.factorial(1), 1)
        self.assertEqual(math.factorial(2), 2)
        self.assertEqual(math.factorial(3), 6)
        self.assertEqual(math.factorial(4), 24)
        self.assertEqual(math.factorial(5), 120)

    def test_factorial_of_large_number(self):
        self.assertEqual(math.factorial(10), 3628800)
        self.assertEqual(math.factorial(20), 2432902008176640000)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            math.factorial(-1)

    def test_factorial_of_non_integer(self):
        with self.assertRaises(TypeError):
            math.factorial(1.5)

if __name__ == '__main__':
    unittest.main()
