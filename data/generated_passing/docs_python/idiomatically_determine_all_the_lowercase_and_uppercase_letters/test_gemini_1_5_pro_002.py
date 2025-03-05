import unittest
import sys

def get_letters():
    """
    Returns a tuple containing two sets: lowercase and uppercase letters.
    """
    lowercase_letters = set()
    uppercase_letters = set()

    for i in range(sys.maxunicode + 1):
        char = chr(i)
        if 'a' <= char <= 'z':
            lowercase_letters.add(char)
        elif 'A' <= char <= 'Z':
            uppercase_letters.add(char)
    
    return lowercase_letters, uppercase_letters



class TestGetLetters(unittest.TestCase):

    def test_ascii(self):
        lowercase_expected = set(chr(i) for i in range(ord('a'), ord('z') + 1))
        uppercase_expected = set(chr(i) for i in range(ord('A'), ord('Z') + 1))
        lowercase_actual, uppercase_actual = get_letters()
        self.assertEqual(lowercase_actual, lowercase_expected)
        self.assertEqual(uppercase_actual, uppercase_expected)

    def test_empty_if_no_letters_exist(self):
        # Simulate an environment without standard Latin alphabet (for demonstration)
        original_chr = chr

        def mock_chr(i):
            if ord('a') <= i <= ord('z') or ord('A') <= i <= ord('Z'):
                return '' #  Returning empty string instead of a letter
            else: 
               return original_chr(i)
               
        try:
          chr = mock_chr  # Monkey patch chr()
          lowercase, uppercase = get_letters()
          self.assertEqual(lowercase, set())
          self.assertEqual(uppercase, set())
        finally:
          chr = original_chr  # Restore original chr()


    def test_subset_of_letters(self):
        original_chr = chr
        #Simulate a limited character set containing only a,b,A,B
        mock_chr_limited = lambda i: original_chr(i) if i in [ord('a'), ord('b'), ord('A'), ord('B')]  else ''
        try:
            chr = mock_chr_limited
            lowercase, uppercase = get_letters()
            self.assertEqual(lowercase, set('ab'))
            self.assertEqual(uppercase, set('AB'))

        finally:
            chr = original_chr

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


