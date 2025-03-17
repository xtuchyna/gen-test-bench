import unittest
import os
from unittest.mock import patch

class TestFileSize(unittest.TestCase):

    @patch('os.path.getsize')
    def test_file_size_in_current_directory(self, mock_getsize):
        # Mock the return value for the current directory file
        mock_getsize.return_value = 1024  # Assume the file size is 1024 bytes
        size = os.path.getsize('input.txt')
        self.assertEqual(size, 1024)
        mock_getsize.assert_called_with('input.txt')

    @patch('os.path.getsize')
    def test_file_size_in_root_directory(self, mock_getsize):
        # Mock the return value for the root directory file
        mock_getsize.return_value = 2048  # Assume the file size is 2048 bytes
        size = os.path.getsize('/input.txt')
        self.assertEqual(size, 2048)
        mock_getsize.assert_called_with('/input.txt')

if __name__ == '__main__':
    unittest.main()
