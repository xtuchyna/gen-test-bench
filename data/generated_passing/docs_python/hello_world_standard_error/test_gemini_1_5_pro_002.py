import sys
import io
from unittest.mock import patch

def test_standard_error_output():
    with patch('sys.stderr', new=io.StringIO()) as fake_stderr:
        # Execute the code that prints to stderr
        with open('hello_world_standard_error.py', 'r') as f:
            exec(f.read())

        # Check the captured output
        assert fake_stderr.getvalue() == "Goodbye, World!\n"
