import unittest
from datetime import date

class TestDateFormat(unittest.TestCase):

    def setUp(self):
        self.today = date.today()

    def test_isoformat(self):
        expected_format = self.today.isoformat()
        self.assertEqual(self.today.isoformat(), expected_format)

    def test_strftime_format(self):
        expected_format = self.today.strftime("%A, %B %d, %Y")
        self.assertEqual(self.today.strftime("%A, %B %d, %Y"), expected_format)

    def test_strftime_positional_format(self):
        expected_format = self.today.strftime("%A, %B %d, %Y")
        formatted_string = "The date is {0:%A, %B %d, %Y}".format(self.today)
        self.assertEqual(formatted_string, f"The date is {expected_format}")

    def test_strftime_keyword_format(self):
        expected_format = self.today.strftime("%A, %B %d, %Y")
        formatted_string = "The date is {date:%A, %B %d, %Y}".format(date=self.today)
        self.assertEqual(formatted_string, f"The date is {expected_format}")

    def test_fstring_format(self):
        expected_format = self.today.strftime("%A, %B %d, %Y")
        formatted_string = f"The date is {self.today:%A, %B %d, %Y}"
        self.assertEqual(formatted_string, f"The date is {expected_format}")

if __name__ == '__main__':
    unittest.main()
