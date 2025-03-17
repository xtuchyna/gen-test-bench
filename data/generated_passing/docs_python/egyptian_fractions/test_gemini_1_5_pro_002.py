import unittest
from fractions import Fraction
from math import ceil

class Fr(Fraction):
    def __repr__(self):
        return '%s/%s' % (self.numerator, self.denominator)

def ef(fr):
    ans = []
    if fr >= 1:
        if fr.denominator == 1:
            return [[int(fr)], Fr(0, 1)]
        intfr = int(fr)
        ans, fr = [[intfr]], fr - intfr
    x, y = fr.numerator, fr.denominator
    while x != 1:
        ans.append(Fr(1, ceil(1/fr)))
        fr = Fr(-y % x, y* ceil(1/fr))
        x, y = fr.numerator, fr.denominator
    ans.append(fr)
    return ans


class TestEgyptianFractions(unittest.TestCase):

    def test_given_fractions(self):
        self.assertEqual(ef(Fr(43, 48)), [Fr(1, 2), Fr(1, 3), Fr(1, 16)])
        self.assertEqual(ef(Fr(5, 121)), [Fr(1, 25), Fr(1, 726), Fr(1, 18150), Fr(1, 36300)])
        self.assertEqual(ef(Fr(2014, 59)), [[34], Fr(1, 2), Fr(1, 9), Fr(1, 174), Fr(1, 3042), Fr(1, 51714)])

    def test_improper_fractions(self):
        self.assertEqual(ef(Fr(5, 2)), [[2], Fr(1, 2)])
        self.assertEqual(ef(Fr(12, 5)), [[2], Fr(1, 3), Fr(1, 15)])
        self.assertEqual(ef(Fr(7, 1)), [[7], Fr(0, 1)])

    def test_proper_fractions(self):
        self.assertEqual(ef(Fr(1, 2)), [Fr(1, 2)])
        self.assertEqual(ef(Fr(3, 4)), [Fr(1, 2), Fr(1, 4)])
        self.assertEqual(ef(Fr(2, 5)), [Fr(1, 3), Fr(1, 15)])
        

    def test_sum_of_egyptian_fractions(self):
        for a in range(1, 100):
            for b in range(a + 1, 100):  # Proper fractions only
                e = ef(Fr(a, b))
                self.assertEqual(sum((f[0] if type(f) is list else f) for f in e), Fr(a, b))



