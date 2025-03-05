import unittest
from itertools import chain

def _range(x, y, z=1):
    return range(x, y + (1 if z > 0 else -1), z)

class TestLoopsWithMultipleRanges(unittest.TestCase):

    def test_ranges(self):
        prod, sum_, x, y, z, one, three, seven = 1, 0, 5, -5, -2, 1, 3, 7

        expected_ranges = [
            list(_range(-three, 3**3, three)),
            list(_range(-seven, seven, x)),
            list(_range(555, 550 - y)),
            list(_range(22, -28, -three)),
            list(_range(1927, 1939)),
            list(_range(x, y, z)),
            list(_range(11**x, 11**x + 1))
        ]

        expected_sum = sum(abs(j) for j in chain(*expected_ranges))
        expected_prod = 1
        for j in chain(*expected_ranges):
            if abs(expected_prod) < 2**27 and j != 0:
                expected_prod *= j

        for j in chain(_range(-three, 3**3, three), _range(-seven, seven, x), 
                       _range(555, 550 - y), _range(22, -28, -three),
                       _range(1927, 1939), _range(x, y, z),
                       _range(11**x, 11**x + 1)):
            sum_ += abs(j)
            if abs(prod) < 2**27 and (j != 0):
                prod *= j

        self.assertEqual(sum_, expected_sum)
        self.assertEqual(prod, expected_prod)

if __name__ == '__main__':
    unittest.main()
