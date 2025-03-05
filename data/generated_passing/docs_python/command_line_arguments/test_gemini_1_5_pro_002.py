import unittest
import sys
from io import StringIO
from contextlib import redirect_stdout

# Mocking sys.argv for testing purposes
class TestCommandLineArguments(unittest.TestCase):

    def test_no_arguments(self):
        sys.argv = ['myprogram']
        with redirect_stdout(StringIO()) as f:
            import command_line_arguments  # Import the module under test
        self.assertEqual(command_line_arguments.program_name, 'myprogram')
        self.assertEqual(command_line_arguments.arguments, [])
        self.assertEqual(command_line_arguments.count, 0)

    def test_multiple_arguments(self):
        sys.argv = ['myprogram', '-c', "alpha beta", '-h', "gamma"]
        with redirect_stdout(StringIO()) as f:
            import command_line_arguments
        self.assertEqual(command_line_arguments.program_name, 'myprogram')
        self.assertEqual(command_line_arguments.arguments, ['-c', "alpha beta", '-h', "gamma"])
        self.assertEqual(command_line_arguments.count, 4)

    def test_single_argument(self):
        sys.argv = ['myprogram', 'argument1']
        with redirect_stdout(StringIO()) as f:
            import command_line_arguments
        self.assertEqual(command_line_arguments.program_name, 'myprogram')
        self.assertEqual(command_line_arguments.arguments, ['argument1'])
        self.assertEqual(command_line_arguments.count, 1)

    def test_arguments_with_spaces(self):
        sys.argv = ['myprogram', 'argument with spaces']
        with redirect_stdout(StringIO()) as f:
            import command_line_arguments
        self.assertEqual(command_line_arguments.program_name, 'myprogram')
        self.assertEqual(command_line_arguments.arguments, ['argument with spaces'])
        self.assertEqual(command_line_arguments.count, 1)
