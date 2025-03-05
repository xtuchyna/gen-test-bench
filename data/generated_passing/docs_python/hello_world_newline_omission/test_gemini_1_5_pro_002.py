import sys
import io
from unittest.mock import patch

def test_goodbye_world_no_newline():
    with patch('sys.stdout', new_callable=io.StringIO) as mocked_stdout:
        # Execute the code that prints to stdout
        sys.stdout.write("Goodbye, World!")

        # Check the output
        assert mocked_stdout.getvalue() == "Goodbye, World!" 
