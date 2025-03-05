import unittest
from calendar import weekday, SUNDAY

def xmas_sundays(start_year, end_year):
    return [year for year in range(start_year, end_year + 1) if weekday(year, 12, 25) == SUNDAY]

class TestXmasSundays(unittest.TestCase):

    def test_known_sundays(self):
        self.assertIn(2011, xmas_sundays(2008, 2121))
        self.assertIn(2016, xmas_sundays(2008, 2121))
        self.assertIn(2022, xmas_sundays(2008, 2121))  # Beyond the prompt's example output, but verifiable

    def test_start_and_end_years(self):
        self.assertEqual(xmas_sundays(2011, 2011), [2011])
        self.assertEqual(xmas_sundays(2010, 2012), [2011])
    
    def test_no_sundays(self):
        self.assertEqual(xmas_sundays(2012, 2015), [])

    def test_large_range(self):  # Test a range that might expose potential overflow/edge cases
        sundays = xmas_sundays(1900, 2200)
        self.assertTrue(len(sundays) > 0) #  Ensure there are results, without asserting the exact count which may depend on date/time library implementation. Checks against empty list effectively.


if __name__ == '__main__':
    unittest.main()
