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

    def test_basic_case(self):
        s1 = "thisisatest"
        s2 = "testing123testing"
        self.assertEqual(longest_common_substring(s1, s2), "test")

    def test_no_common_substring(self):
        s1 = "abc"
        s2 = "def"
        self.assertEqual(longest_common_substring(s1, s2), "")

    def test_identical_strings(self):
        s1 = "identical"
        s2 = "identical"
        self.assertEqual(longest_common_substring(s1, s2), "identical")

    def test_multiple_common_substrings(self):
        s1 = "abcdefgh"
        s2 = "defghijkl"
        self.assertEqual(longest_common_substring(s1, s2), "defgh")

    def test_substring_at_beginning(self):
        s1 = "hello"
        s2 = "helloworld"
        self.assertEqual(longest_common_substring(s1, s2), "hello")

    def test_substring_at_end(self):
        s1 = "world"
        s2 = "helloworld"
        self.assertEqual(longest_common_substring(s1, s2), "world")

    def test_substring_in_middle(self):
        s1 = "middle"
        s2 = "somemiddletext"
        self.assertEqual(longest_common_substring(s1, s2), "middle")

    def test_multiple_occurrences(self):
        s1 = "testtest"
        s2 = "testing123testing"
        self.assertEqual(longest_common_substring(s1, s2), "test")

    def test_empty_strings(self):
        s1 = ""
        s2 = "testing123testing"
        self.assertEqual(longest_common_substring(s1, s2), "")

    def test_both_empty_strings(self):
        s1 = ""
        s2 = ""
        self.assertEqual(longest_common_substring(s1, s2), "")

if __name__ == '__main__':
    unittest.main()
