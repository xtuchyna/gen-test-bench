import unittest
from unittest.mock import patch, Mock
import requests

class TestMacVendorLookup(unittest.TestCase):

    @patch('requests.get')
    def test_valid_mac_address(self, mock_get):
        # Mocking a successful response for a valid MAC address
        mock_get.return_value = Mock(status_code=200, text='Apple, Inc.')
        
        addr = '88:53:2E:67:07:BE'
        response = requests.get('http://api.macvendors.com/' + addr)
        self.assertEqual(response.text, 'Apple, Inc.')

    @patch('requests.get')
    def test_invalid_mac_address(self, mock_get):
        # Mocking a response for an invalid MAC address
        mock_get.return_value = Mock(status_code=404, text='N/A')
        
        addr = '23:45:67'
        response = requests.get('http://api.macvendors.com/' + addr)
        self.assertEqual(response.text, 'N/A')

    @patch('requests.get')
    def test_network_error(self, mock_get):
        # Mocking a network error
        mock_get.side_effect = requests.exceptions.ConnectionError
        
        addr = '88:53:2E:67:07:BE'
        try:
            response = requests.get('http://api.macvendors.com/' + addr)
        except requests.exceptions.ConnectionError:
            response = None
        self.assertIsNone(response)

    @patch('requests.get')
    def test_api_throttling(self, mock_get):
        # Mocking a throttling response
        mock_get.return_value = Mock(status_code=429, text='{"errors":{"detail":"Too Many Requests","message":"Please slow down your requests or upgrade your plan at https://macvendors.com"}}')
        
        addr = '88:53:2E:67:07:BE'
        response = requests.get('http://api.macvendors.com/' + addr)
        self.assertIn('Too Many Requests', response.text)

if __name__ == '__main__':
    unittest.main()
