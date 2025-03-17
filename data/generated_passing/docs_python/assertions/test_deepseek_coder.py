import unittest

class TestAssertions(unittest.TestCase):

    def test_assertion_equal(self):
        a = 42
        assert a == 42, "a should be equal to 42"

    def test_assertion_not_equal(self):
        a = 5
        with self.assertRaises(AssertionError) as context:
            assert a == 42, "a should be equal to 42"
        self.assertEqual(str(context.exception), "a should be equal to 42")

if __name__ == '__main__':
    unittest.main()
