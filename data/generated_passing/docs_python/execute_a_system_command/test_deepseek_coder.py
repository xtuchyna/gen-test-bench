import unittest
from unittest.mock import patch, MagicMock
import os

class TestSystemCommandExecution(unittest.TestCase):

    @patch('os.system')
    def test_execute_system_command_ls(self, mock_system):
        # Arrange
        mock_system.return_value = 0  # Simulate success

        # Act
        exit_code = os.system('ls')

        # Assert
        mock_system.assert_called_once_with('ls')
        self.assertEqual(exit_code, 0)

    @patch('os.system')
    def test_execute_system_command_dir(self, mock_system):
        # Arrange
        mock_system.return_value = 0  # Simulate success

        # Act
        exit_code = os.system('dir')

        # Assert
        mock_system.assert_called_once_with('dir')
        self.assertEqual(exit_code, 0)

    @patch('os.system')
    def test_execute_system_command_pause(self, mock_system):
        # Arrange
        mock_system.return_value = 0  # Simulate success

        # Act
        exit_code = os.system('pause')

        # Assert
        mock_system.assert_called_once_with('pause')
        self.assertEqual(exit_code, 0)

    @patch('os.system')
    def test_execute_system_command_failure(self, mock_system):
        # Arrange
        mock_system.return_value = 1  # Simulate failure

        # Act
        exit_code = os.system('ls')

        # Assert
        mock_system.assert_called_once_with('ls')
        self.assertEqual(exit_code, 1)

    @patch('os.popen')
    def test_get_system_command_output(self, mock_popen):
        # Arrange
        mock_popen.return_value.read.return_value = 'test_output'

        # Act
        output = os.popen('ls').read()

        # Assert
        mock_popen.assert_called_once_with('ls')
        self.assertEqual(output, 'test_output')

    @patch('os.popen')
    def test_get_system_command_output_empty(self, mock_popen):
        # Arrange
        mock_popen.return_value.read.return_value = ''

        # Act
        output = os.popen('ls').read()

        # Assert
        mock_popen.assert_called_once_with('ls')
        self.assertEqual(output, '')

if __name__ == '__main__':
    unittest.main()
