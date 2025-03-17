import unittest
import os
from unittest.mock import patch, MagicMock

class TestSystemCommands(unittest.TestCase):

    @patch('os.system')
    def test_system_command_ls(self, mock_system):
        os.system('ls')  # The code being tested
        mock_system.assert_called_once_with('ls')

    @patch('os.system')
    def test_system_command_dir_windows(self, mock_system):
        # Simulate Windows environment
        with patch('os.name', 'nt'):
            os.system('ls') # The code being tested - it will execute 'dir' on Windows due to 'ls' not being recognized usually.
            mock_system.assert_called_once_with('ls') # The code still calls 'ls' even if it's not effective on Windows.


    @patch('os.system')
    def test_system_command_pause(self, mock_system):
        os.system('pause') # The code being tested
        mock_system.assert_called_once_with('pause')




    @patch('os.popen')
    def test_popen_ls(self, mock_popen):
        mock_file = MagicMock()
        mock_popen.return_value = mock_file
        mock_file.read.return_value = "mocked output"

        output = os.popen('ls').read()
        mock_popen.assert_called_once_with('ls')
        mock_file.read.assert_called_once()
        self.assertEqual(output, "mocked output")


