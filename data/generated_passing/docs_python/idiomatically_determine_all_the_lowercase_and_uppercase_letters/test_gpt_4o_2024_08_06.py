import unittest

class TestCharacterClasses(unittest.TestCase):
    def setUp(self):
        self.classes = (str.isupper, str.islower, str.isalnum, str.isalpha, str.isdecimal,
                        str.isdigit, str.isidentifier, str.isnumeric, str.isprintable,
                        str.isspace, str.istitle)

    def test_isupper(self):
        # Test that isupper identifies uppercase letters
        uppercase_letters = ''.join(chr(i) for i in range(0x10FFFF+1) if str.isupper(chr(i)))
        expected_uppercase = ''.join(chr(i) for i in range(ord('A'), ord('Z')+1))
        self.assertTrue(all(char in uppercase_letters for char in expected_uppercase))
        self.assertTrue(all(char.isupper() for char in uppercase_letters))

    def test_islower(self):
        # Test that islower identifies lowercase letters
        lowercase_letters = ''.join(chr(i) for i in range(0x10FFFF+1) if str.islower(chr(i)))
        expected_lowercase = ''.join(chr(i) for i in range(ord('a'), ord('z')+1))
        self.assertTrue(all(char in lowercase_letters for char in expected_lowercase))
        self.assertTrue(all(char.islower() for char in lowercase_letters))

    def test_isalnum(self):
        # Test that isalnum identifies alphanumeric characters
        alnum_chars = ''.join(chr(i) for i in range(0x10FFFF+1) if str.isalnum(chr(i)))
        self.assertTrue(all(char.isalnum() for char in alnum_chars))

    def test_isalpha(self):
        # Test that isalpha identifies alphabetic characters
        alpha_chars = ''.join(chr(i) for i in range(0x10FFFF+1) if str.isalpha(chr(i)))
        self.assertTrue(all(char.isalpha() for char in alpha_chars))

    def test_isdecimal(self):
        # Test that isdecimal identifies decimal characters
        decimal_chars = ''.join(chr(i) for i in range(0x10FFFF+1) if str.isdecimal(chr(i)))
        self.assertTrue(all(char.isdecimal() for char in decimal_chars))

    def test_isdigit(self):
        # Test that isdigit identifies digit characters
        digit_chars = ''.join(chr(i) for i in range(0x10FFFF+1) if str.isdigit(chr(i)))
        self.assertTrue(all(char.isdigit() for char in digit_chars))

    def test_isidentifier(self):
        # Test that isidentifier identifies valid identifier characters
        identifier_chars = ''.join(chr(i) for i in range(0x10FFFF+1) if str.isidentifier(chr(i)))
        self.assertTrue(all(char.isidentifier() for char in identifier_chars))

    def test_isnumeric(self):
        # Test that isnumeric identifies numeric characters
        numeric_chars = ''.join(chr(i) for i in range(0x10FFFF+1) if str.isnumeric(chr(i)))
        self.assertTrue(all(char.isnumeric() for char in numeric_chars))

    def test_isprintable(self):
        # Test that isprintable identifies printable characters
        printable_chars = ''.join(chr(i) for i in range(0x10FFFF+1) if str.isprintable(chr(i)))
        self.assertTrue(all(char.isprintable() for char in printable_chars))

    def test_isspace(self):
        # Test that isspace identifies whitespace characters
        space_chars = ''.join(chr(i) for i in range(0x10FFFF+1) if str.isspace(chr(i)))
        self.assertTrue(all(char.isspace() for char in space_chars))

    def test_istitle(self):
        # Test that istitle identifies titlecase characters
        title_chars = ''.join(chr(i) for i in range(0x10FFFF+1) if str.istitle(chr(i)))
        self.assertTrue(all(char.istitle() for char in title_chars))

if __name__ == '__main__':
    unittest.main()
