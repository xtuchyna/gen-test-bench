import unittest
from functools import cmp_to_key

# Define the maxnum function
def cmp(x, y):
    return -1 if x < y else (0 if x == y else 1)

def maxnum(x):
    return ''.join(sorted((str(n) for n in x), key=cmp_to_key(lambda x, y: cmp(y + x, x + y))))

# Unit tests
class TestMaxnum(unittest.TestCase):

    def test_case_1(self):
        numbers = (1, 34, 3, 98, 9, 76, 45, 4)
        expected_output = "998764543431"
        self.assertEqual(maxnum(numbers), expected_output)

    def test_case_2(self):
        numbers = (54, 546, 548, 60)
        expected_output = "6054854654"
        self.assertEqual(maxnum(numbers), expected_output)

    def test_single_number(self):
        numbers = (5,)
        expected_output = "5"
        self.assertEqual(maxnum(numbers), expected_output)

    def test_all_same_numbers(self):
        numbers = (2, 2, 2, 2)
        expected_output = "2222"
        self.assertEqual(maxnum(numbers), expected_output)

    def test_large_numbers(self):
        numbers = (100, 10, 1)
        expected_output = "110100"
        self.assertEqual(maxnum(numbers), expected_output)

    def test_mixed_numbers(self):
        numbers = (5, 50, 56)
        expected_output = "56550"
        self.assertEqual(maxnum(numbers), expected_output)

if __name__ == '__main__':
    unittest.main()
