import unittest
from itertools import islice

class TestRangeFunction(unittest.TestCase):

    def test_normal(self):
        start, stop, increment = -2, 2, 1
        expected = [-2, -1, 0, 1]
        result = list(islice(range(start, stop, increment), 999))
        self.assertEqual(result, expected)

    def test_zero_increment(self):
        start, stop, increment = -2, 2, 0
        with self.assertRaises(ValueError):
            list(islice(range(start, stop, increment), 999))

    def test_increments_away_from_stop_value(self):
        start, stop, increment = -2, 2, -1
        expected = []
        result = list(islice(range(start, stop, increment), 999))
        self.assertEqual(result, expected)

    def test_first_increment_beyond_stop_value(self):
        start, stop, increment = -2, 2, 10
        expected = [-2]
        result = list(islice(range(start, stop, increment), 999))
        self.assertEqual(result, expected)

    def test_start_more_than_stop_positive_increment(self):
        start, stop, increment = 2, -2, 1
        expected = []
        result = list(islice(range(start, stop, increment), 999))
        self.assertEqual(result, expected)

    def test_start_equal_stop_positive_increment(self):
        start, stop, increment = 2, 2, 1
        expected = []
        result = list(islice(range(start, stop, increment), 999))
        self.assertEqual(result, expected)

    def test_start_equal_stop_negative_increment(self):
        start, stop, increment = 2, 2, -1
        expected = []
        result = list(islice(range(start, stop, increment), 999))
        self.assertEqual(result, expected)

    def test_start_equal_stop_zero_increment(self):
        start, stop, increment = 2, 2, 0
        with self.assertRaises(ValueError):
            list(islice(range(start, stop, increment), 999))

    def test_start_equal_stop_equal_zero_zero_increment(self):
        start, stop, increment = 0, 0, 0
        with self.assertRaises(ValueError):
            list(islice(range(start, stop, increment), 999))

if __name__ == '__main__':
    unittest.main()
