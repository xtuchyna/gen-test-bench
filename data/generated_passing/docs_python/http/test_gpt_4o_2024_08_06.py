import unittest
from unittest.mock import patch, MagicMock
import urllib.request

class TestHttpRequest(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_urlopen_success(self, mock_urlopen):
        # Mock the response to simulate a successful HTTP request
        mock_response = MagicMock()
        mock_response.read.return_value = b'This is a test response'
        mock_urlopen.return_value = mock_response

        # Call the function that uses urlopen
        response = urllib.request.urlopen("http://rosettacode.org").read()

        # Assert that urlopen was called with the correct URL
        mock_urlopen.assert_called_with("http://rosettacode.org")

        # Assert that the response is as expected
        self.assertEqual(response, b'This is a test response')

    @patch('urllib.request.urlopen')
    def test_urlopen_failure(self, mock_urlopen):
        # Simulate an HTTP error
        mock_urlopen.side_effect = urllib.error.URLError('Failed to reach server')

        # Call the function and handle the exception
        with self.assertRaises(urllib.error.URLError):
            urllib.request.urlopen("http://rosettacode.org").read()

# Run the tests
if __name__ == '__main__':
    unittest.main()
