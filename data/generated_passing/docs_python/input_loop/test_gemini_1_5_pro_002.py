import unittest
from unittest.mock import patch
import io

class TestInputLoop(unittest.TestCase):

    @patch('builtins.input', side_effect=['25', '30', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_multiple_inputs(self, mock_stdout, mock_input):
        # Simulate Ctrl+D or an empty input to break the loop
        try:
             import input_loop # The code to be tested
        except EOFError: 
            pass #Expected behavior for Ctrl+D 
        self.assertEqual(mock_stdout.getvalue(), "25\n30\n")

    @patch('builtins.input', side_effect=['42', EOFError])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_eof_input(self, mock_stdout, mock_input):
        try:
            import input_loop  # The code to be tested
        except EOFError:
            pass

        self.assertEqual(mock_stdout.getvalue(), "42\n")



