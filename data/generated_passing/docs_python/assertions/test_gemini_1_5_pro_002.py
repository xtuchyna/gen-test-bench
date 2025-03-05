import unittest

class TestAssertions(unittest.TestCase):

    def test_assertion_pass(self):
        a = 42
        try:
            assert a == 42
        except AssertionError:
            self.fail("Assertion should not have failed")

    def test_assertion_fail(self):
        a = 5
        with self.assertRaisesRegex(AssertionError, ""):  # No specific message expected
            assert a == 42

    def test_assertion_fail_with_message(self):
        a = 5
        with self.assertRaisesRegex(AssertionError, "Error message"):
            assert a == 42, "Error message"

    def test_assertion_fail_with_formatted_message(self):
        a = 5
        with self.assertRaisesRegex(AssertionError, "Value of a: 5"):
            assert a == 42, f"Value of a: {a}"

