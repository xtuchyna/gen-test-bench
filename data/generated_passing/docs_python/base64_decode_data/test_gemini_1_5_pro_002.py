import unittest
import base64

class TestBase64Decode(unittest.TestCase):

    def test_decode_valid_data(self):
        data = 'VG8gZXJyIGlzIGh1bWFuLCBidXQgdG8gcmVhbGx5IGZvdWwgdGhpbmdzIHVwIHlvdSBuZWVkIGEgY29tcHV0ZXIuCiAgICAtLSBQYXVsIFIuIEVocmxpY2g='
        expected_output = 'To err is human, but to really foul things up you need a computer.\n      -- Paul R. Ehrlich'
        self.assertEqual(base64.b64decode(data).decode('utf-8'), expected_output)

    def test_decode_empty_string(self):
        data = ''
        expected_output = ''
        self.assertEqual(base64.b64decode(data).decode('utf-8'), expected_output)

    def test_decode_data_with_padding(self):
        data = 'SGVsbG8gV29ybGQh'  # "Hello World!" encoded with padding
        expected_output = 'Hello World!'
        self.assertEqual(base64.b64decode(data).decode('utf-8'), expected_output)

    def test_decode_data_without_padding(self):
        data = 'SGVsbG8gV29ybGQ' # "Hello World" encoded without padding
        expected_output = 'Hello World'
        self.assertEqual(base64.b64decode(data).decode('utf-8'), expected_output)


    def test_decode_data_with_newline(self):
        data = 'SGVsbG8gV29ybGQhCg=='  # "Hello World!\n" encoded
        expected_output = 'Hello World!\n'
        self.assertEqual(base64.b64decode(data).decode('utf-8'), expected_output)

    def test_decode_unicode_data(self):
        data = 'w6TDtsO8w4XCp8K7w7bCvMOCw4XDhsOcw4bCgMK7w7bCvMOEw4XCp8K7w7nDhcKjw6TDtsOfw4bCgMK7w67DgcOnw4XDhcKjw4/DhcOjw4bCgMK7w7bCvMOEw4XCp8K7w7PDhcKjw4bC'  # Unicode string encoded
        expected_output = '你好世界！\n世界你好！\n你好世界！\n世界你好！\n你好世界！'
        self.assertEqual(base64.b64decode(data).decode('utf-8'), expected_output)



