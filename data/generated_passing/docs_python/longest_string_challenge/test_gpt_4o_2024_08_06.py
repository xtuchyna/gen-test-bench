import unittest
from io import StringIO
import sys

# Assuming the function is refactored to accept input as a list of strings
def longest_string_challenge(input_lines):
    def longer(a, b):
        try:
            b[len(a)-1]
            return False
        except:
            return True

    longest, lines = '', ''
    for x in input_lines:
        if longer(x, longest):
            lines, longest = x, x
        elif not longer(longest, x):
            lines += x

    return lines

class TestLongestStringChallenge(unittest.TestCase):

    def test_single_longest_line(self):
        input_lines = ["a", "bb", "ccc", "d", "ee"]
        expected_output = "ccc"
        self.assertEqual(longest_string_challenge(input_lines), expected_output)

    def test_multiple_longest_lines(self):
        input_lines = ["a", "bb", "ccc", "ddd", "ee", "f", "ggg"]
        expected_output = "cccdddggg"
        self.assertEqual(longest_string_challenge(input_lines), expected_output)

    def test_no_input(self):
        input_lines = []
        expected_output = ""
        self.assertEqual(longest_string_challenge(input_lines), expected_output)

    def test_all_lines_same_length(self):
        input_lines = ["aa", "bb", "cc", "dd"]
        expected_output = "aabbccdd"
        self.assertEqual(longest_string_challenge(input_lines), expected_output)

    def test_single_line_input(self):
        input_lines = ["singleline"]
        expected_output = "singleline"
        self.assertEqual(longest_string_challenge(input_lines), expected_output)

    def test_empty_lines(self):
        input_lines = ["", "", ""]
        expected_output = ""
        self.assertEqual(longest_string_challenge(input_lines), expected_output)

    def test_mixed_empty_and_non_empty_lines(self):
        input_lines = ["", "a", "", "bb", "", "ccc", ""]
        expected_output = "ccc"
        self.assertEqual(longest_string_challenge(input_lines), expected_output)

if __name__ == '__main__':
    unittest.main()
