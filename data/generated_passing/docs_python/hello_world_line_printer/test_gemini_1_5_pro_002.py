import unittest
from unittest.mock import patch, mock_open
import io

class TestHelloWorldLinePrinter(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_prints_hello_world(self, mock_file):
        # Execute the code that interacts with the line printer
        with patch('sys.stdout', new=io.StringIO()) as stdout:  # Suppress print to console during test if any
             import hello_world_line_printer

        # Assert that the file was opened with the correct path and mode
        mock_file.assert_called_once_with("/dev/lp0", "w")  # Default mode is 'w', make it explicit

        # Assert that "Hello World!\n" was written to the file
        mock_file().write.assert_called_once_with("Hello World!\n")

        # Assert that the file was closed
        mock_file().close.assert_called_once()
