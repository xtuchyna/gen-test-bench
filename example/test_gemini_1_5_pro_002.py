import unittest
from collections import deque

def simplemovingaverage(period):
    assert period == int(period) and period > 0, "Period must be an integer >0"

    summ = n = 0.0
    values = deque([0.0] * period)     # old value queue

    def sma(x):
        nonlocal summ, n

        values.append(x)
        summ += x - values.popleft()
        n = min(n+1, period)
        return summ / n

    return sma

class TestSimpleMovingAverage(unittest.TestCase):

    def test_period_1(self):
        sma = simplemovingaverage(1)
        self.assertEqual(sma(5), 5)
        self.assertEqual(sma(10), 10)
        self.assertEqual(sma(15), 15)

    def test_period_3(self):
        sma = simplemovingaverage(3)
        self.assertEqual(sma(1), 1/3)  # (0+0+1)/3
        self.assertEqual(sma(2), 1) # (0+1+2)/3
        self.assertEqual(sma(3), 2) # (1+2+3)/3
        self.assertEqual(sma(4), 3) # (2+3+4)/3

    def test_period_5_with_floats(self):
        sma = simplemovingaverage(5)
        self.assertAlmostEqual(sma(1.1), 0.22)
        self.assertAlmostEqual(sma(2.2), 0.66)
        self.assertAlmostEqual(sma(3.3), 1.32)
        self.assertAlmostEqual(sma(4.4), 2.2)
        self.assertAlmostEqual(sma(5.5), 3.3)
        self.assertAlmostEqual(sma(6.6), 4.4)

    def test_period_2_with_negative_numbers(self):
        sma = simplemovingaverage(2)
        self.assertEqual(sma(-1), -0.5)
        self.assertEqual(sma(-2), -1.5)
        self.assertEqual(sma(-3), -2.5)

    def test_invalid_period(self):
        with self.assertRaises(AssertionError):
            simplemovingaverage(0)
        with self.assertRaises(AssertionError):
            simplemovingaverage(-1)
        with self.assertRaises(AssertionError):
            simplemovingaverage(2.5)

    def test_independent_instances(self):
        sma1 = simplemovingaverage(2)
        sma2 = simplemovingaverage(2)
        self.assertEqual(sma1(1), 0.5)
        self.assertEqual(sma2(10), 5)
        self.assertEqual(sma1(2), 1.5)
        self.assertEqual(sma2(20), 15)



