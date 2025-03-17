import unittest

class TestAssertions(unittest.TestCase):
    
    def test_assert_equal_42(self):
        a = 42
        try:
            assert a == 42
        except AssertionError:
            self.fail("AssertionError raised unexpectedly!")

    def test_assert_not_equal_42(self):
        a = 5
        with self.assertRaises(AssertionError):
            assert a == 42

    def test_assert_with_error_message(self):
        a = 5
        with self.assertRaises(AssertionError) as context:
            assert a == 42, "Error message"
        self.assertEqual(str(context.exception), "Error message")

if __name__ == '__main__':
    unittest.main()
