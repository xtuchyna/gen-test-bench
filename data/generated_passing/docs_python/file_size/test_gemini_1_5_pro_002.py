import os
import unittest
from unittest.mock import patch, mock_open

class TestFileSize(unittest.TestCase):

    def setUp(self):
        self.current_dir_file_content = "test content"
        self.root_dir_file_content = "root content"


    @patch('os.path.getsize')
    def test_current_dir_file_size(self, mock_getsize):
        # Set up mock return values
        mock_getsize.side_effect = [len(self.current_dir_file_content), len(self.root_dir_file_content)]


        # Execute code under test (indirectly through import)
        import file_size


        # Assertions
        mock_getsize.assert_any_call('input.txt')  # Check that getsize was called with the correct path.
        mock_getsize.assert_any_call('/input.txt') # Check that getsize was called for root


    @patch('os.path.getsize', side_effect=FileNotFoundError)
    def test_file_not_found_current_dir(self, mock_getsize):
        with self.assertRaises(FileNotFoundError):
            import file_size



    @patch('os.path.getsize')
    def test_file_not_found_root(self, mock_getsize):

        mock_getsize.side_effect = [10, FileNotFoundError()]  # Simulate root file not found

        with self.assertRaises(FileNotFoundError):
             import file_size





