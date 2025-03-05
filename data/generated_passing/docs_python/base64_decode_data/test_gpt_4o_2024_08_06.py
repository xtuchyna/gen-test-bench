import unittest
import base64

class TestBase64Decode(unittest.TestCase):
    
    def test_decode_valid_base64(self):
        # This is the Base64 encoded string from the script
        encoded_data = 'VG8gZXJyIGlzIGh1bWFuLCBidXQgdG8gcmVhbGx5IGZvdWwgdGhpbmdzIHVwIHlvdSBuZWVkIGEgY29tcHV0ZXIuCiAgICAtLSBQYXVsIFIuIEVocmxpY2g='
        # Expected decoded output
        expected_output = "To err is human, but to really foul things up you need a computer.\n    -- Paul R. Ehrlich"
        
        # Decode the Base64 data
        decoded_output = base64.b64decode(encoded_data).decode('utf-8')
        
        # Assert that the decoded output matches the expected output
        self.assertEqual(decoded_output, expected_output)

    def test_decode_invalid_base64(self):
        # This is an invalid Base64 encoded string
        invalid_encoded_data = 'InvalidBase64=='
        
        # Attempt to decode the invalid Base64 data should raise an exception
        with self.assertRaises(base64.binascii.Error):
            base64.b64decode(invalid_encoded_data).decode('utf-8')

    def test_decode_empty_string(self):
        # Test decoding an empty string
        empty_encoded_data = ''
        
        # Decoding an empty string should return an empty string
        decoded_output = base64.b64decode(empty_encoded_data).decode('utf-8')
        self.assertEqual(decoded_output, '')

if __name__ == '__main__':
    unittest.main()
