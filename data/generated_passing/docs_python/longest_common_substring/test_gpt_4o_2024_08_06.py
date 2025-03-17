import unittest

def longest_common_substring(s1, s2):
    len1, len2 = len(s1), len(s2)
    ir, jr = 0, -1
    for i1 in range(len1):
        i2 = s2.find(s1[i1])
        while i2 >= 0:
            j1, j2 = i1, i2
            while j1 < len1 and j2 < len2 and s2[j2] == s1[j1]:
                if j1 - i1 >= jr - ir:
                    ir, jr = i1, j1
                j1 += 1
                j2 += 1
            i2 = s2.find(s1[i1], i2 + 1)
    return s1[ir:jr + 1]

class TestLongestCommonSubstring(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(longest_common_substring("thisisatest", "testing123testing"), "test")

    def test_no_common_substring(self):
        self.assertEqual(longest_common_substring("abc", "def"), "")

    def test_identical_strings(self):
        self.assertEqual(longest_common_substring("abc", "abc"), "abc")

    def test_one_empty_string(self):
        self.assertEqual(longest_common_substring("", "abc"), "")
        self.assertEqual(longest_common_substring("abc", ""), "")

    def test_both_empty_strings(self):
        self.assertEqual(longest_common_substring("", ""), "")

    def test_substring_at_start(self):
        self.assertEqual(longest_common_substring("abcde", "abfgh"), "ab")

    def test_substring_at_end(self):
        self.assertEqual(longest_common_substring("xyzabc", "123abc"), "abc")

    def test_multiple_common_substrings(self):
        self.assertEqual(longest_common_substring("abcxyzabc", "xyzabcxyz"), "xyzabc")

    def test_case_sensitivity(self):
        self.assertEqual(longest_common_substring("abc", "ABC"), "")

if __name__ == '__main__':
    unittest.main()
