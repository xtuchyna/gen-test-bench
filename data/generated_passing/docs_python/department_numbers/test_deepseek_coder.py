import unittest
from itertools import permutations

def solve():
    valid_combinations = []
    for p, f, s in permutations(range(1, 8), r=3):
        if p + s + f == 12 and p % 2 == 0:
            valid_combinations.append((p, f, s))
    return valid_combinations

class TestDepartmentNumbers(unittest.TestCase):

    def test_valid_combinations(self):
        valid_combinations = solve()
        self.assertEqual(len(valid_combinations), 14)

    def test_unique_numbers(self):
        valid_combinations = solve()
        for p, f, s in valid_combinations:
            self.assertNotEqual(p, f)
            self.assertNotEqual(p, s)
            self.assertNotEqual(f, s)

    def test_sum_equals_12(self):
        valid_combinations = solve()
        for p, f, s in valid_combinations:
            self.assertEqual(p + f + s, 12)

    def test_police_even(self):
        valid_combinations = solve()
        for p, f, s in valid_combinations:
            self.assertEqual(p % 2, 0)

    def test_number_range(self):
        valid_combinations = solve()
        for p, f, s in valid_combinations:
            self.assertTrue(1 <= p <= 7)
            self.assertTrue(1 <= f <= 7)
            self.assertTrue(1 <= s <= 7)

if __name__ == '__main__':
    unittest.main()
