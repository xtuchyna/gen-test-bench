import unittest

def gray_encode(n):
    return n ^ n >> 1

def gray_decode(n):
    m = n >> 1
    while m:
        n ^= m
        m >>= 1
    return n

class TestGrayCode(unittest.TestCase):

    def test_gray_encode(self):
        # Test encoding for all 5-bit numbers (0-31)
        expected_gray_codes = [
            0b00000, 0b00001, 0b00011, 0b00010, 0b00110, 0b00111, 0b00101, 0b00100,
            0b01100, 0b01101, 0b01111, 0b01110, 0b01010, 0b01011, 0b01001, 0b01000,
            0b11000, 0b11001, 0b11011, 0b11010, 0b11110, 0b11111, 0b11101, 0b11100,
            0b10100, 0b10101, 0b10111, 0b10110, 0b10010, 0b10011, 0b10001, 0b10000
        ]
        for i in range(32):
            with self.subTest(i=i):
                self.assertEqual(gray_encode(i), expected_gray_codes[i])

    def test_gray_decode(self):
        # Test decoding for all 5-bit Gray codes (0-31)
        expected_gray_codes = [
            0b00000, 0b00001, 0b00011, 0b00010, 0b00110, 0b00111, 0b00101, 0b00100,
            0b01100, 0b01101, 0b01111, 0b01110, 0b01010, 0b01011, 0b01001, 0b01000,
            0b11000, 0b11001, 0b11011, 0b11010, 0b11110, 0b11111, 0b11101, 0b11100,
            0b10100, 0b10101, 0b10111, 0b10110, 0b10010, 0b10011, 0b10001, 0b10000
        ]
        for i in range(32):
            with self.subTest(i=i):
                self.assertEqual(gray_decode(expected_gray_codes[i]), i)

    def test_encode_decode_consistency(self):
        # Test that encoding and then decoding returns the original number
        for i in range(32):
            with self.subTest(i=i):
                gray = gray_encode(i)
                decoded = gray_decode(gray)
                self.assertEqual(decoded, i)

if __name__ == '__main__':
    unittest.main()
