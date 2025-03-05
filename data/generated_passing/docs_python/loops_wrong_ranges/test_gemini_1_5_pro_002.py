import unittest
import re
from itertools import islice

def generate_range(start, stop, increment):
    try:
        return list(islice(range(start, stop, increment), 999))
    except ValueError as e:
        return f"!!ERROR!! {e}"


class TestRangeGeneration(unittest.TestCase):

    def test_normal_range(self):
        self.assertEqual(generate_range(-2, 2, 1), [-2, -1, 0, 1])

    def test_zero_increment(self):
        self.assertEqual(generate_range(-2, 2, 0), "!!ERROR!! range() arg 3 must not be zero")

    def test_negative_increment(self):
        self.assertEqual(generate_range(-2, 2, -1), [])

    def test_large_increment(self):
        self.assertEqual(generate_range(-2, 2, 10), [-2])

    def test_start_greater_than_stop_positive_increment(self):
        self.assertEqual(generate_range(2, -2, 1), [])

    def test_start_equal_stop_positive_increment(self):
        self.assertEqual(generate_range(2, 2, 1), [])

    def test_start_equal_stop_negative_increment(self):
        self.assertEqual(generate_range(2, 2, -1), [])

    def test_start_equal_stop_zero_increment(self):
        self.assertEqual(generate_range(2, 2, 0), "!!ERROR!! range() arg 3 must not be zero")

    def test_start_equal_stop_equal_zero_zero_increment(self):
        self.assertEqual(generate_range(0, 0, 0), "!!ERROR!! range() arg 3 must not be zero")


