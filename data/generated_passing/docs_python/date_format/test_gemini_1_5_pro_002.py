import unittest
from unittest.mock import patch
import datetime

class TestDateFormat(unittest.TestCase):

    @patch('datetime.date')
    def test_date_formats(self, mock_date):
        mock_date.today.return_value = datetime.date(2007, 11, 23)
        
        # Test isoformat
        self.assertEqual(mock_date.today().isoformat(), '2007-11-23')

        # Test strftime
        self.assertEqual(mock_date.today().strftime("%A, %B %d, %Y"), 'Friday, November 23, 2007')

        # Test string formatting with positional arguments
        d = mock_date.today()
        self.assertEqual("The date is {0:%A, %B %d, %Y}".format(d), 'The date is Friday, November 23, 2007')
        
        # Test string formatting with keyword arguments
        self.assertEqual("The date is {date:%A, %B %d, %Y}".format(date=d), 'The date is Friday, November 23, 2007')

        # Test f-string formatting (Python 3.6+)
        self.assertEqual(f"The date is {d:%A, %B %d, %Y}", 'The date is Friday, November 23, 2007')

