import unittest
import subprocess

class TestEmptyProgram(unittest.TestCase):

    def test_program_exits_with_zero(self):
        process = subprocess.Popen(["python", "empty_program.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        returncode = process.wait()
        self.assertEqual(returncode, 0, "Program should exit with code 0")
