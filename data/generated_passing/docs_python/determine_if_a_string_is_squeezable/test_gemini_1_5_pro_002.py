import unittest
from itertools import groupby

def squeezer(s, txt):
    return ''.join(item if item == s else ''.join(grp)
                   for item, grp in groupby(txt))

class TestSqueezer(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(squeezer(' ', ""), "")

    def test_no_repeats(self):
        self.assertEqual(squeezer('-', '"If I were two-faced, would I be wearing this one?" --- Abraham Lincoln '), '"If I were two-faced, would I be wearing this one?" --- Abraham Lincoln ')

    def test_repeats_at_end(self):
        self.assertEqual(squeezer('7', "..1111111111111111111111111111111111111111111111111111111111111117777888"), "..1111111111111111111111111111111111111111111111111111111111111117888")

    def test_single_repeat(self):
        self.assertEqual(squeezer('.', "I never give 'em hell, I just tell the truth, and they think it's hell. "), "I never give 'em hell, I just tell the truth, and they think it's hell. ")


    def test_multiple_repeats(self):
        self.assertEqual(squeezer(' ', "                                                   ---  Harry S Truman  "), "                                    ---  Harry S Truman  ")
        self.assertEqual(squeezer('-', "                                                   ---  Harry S Truman  "), "                                                   -  Harry S Truman  ")
        self.assertEqual(squeezer('r', "                                                   ---  Harry S Truman  "), "                                                   ---  Hary S Truman  ")

    def test_mid_string_repeats(self):
        self.assertEqual(squeezer('e', "The better the 4-wheel drive, the further you'll be from help when ya get stuck!"), "The beter the 4-wheel drive, the further you'll be from help when ya get stuck!")

    def test_consecutive_repeats(self):
        self.assertEqual(squeezer('s', "headmistressship"), "headmistreship")

    def test_no_target_char(self):
        self.assertEqual(squeezer('z', "aardvark"), "aardvark")

    def test_unicode(self):
        self.assertEqual(squeezer('😍', "😍😀🙌💃😍😍😍🙌"), "😍😀🙌💃😍🙌")

