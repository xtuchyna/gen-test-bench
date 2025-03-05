import unittest

class Delegator:
    def __init__(self):
        self.delegate = None

    def operation(self):
        if hasattr(self.delegate, 'thing') and callable(self.delegate.thing):
            return self.delegate.thing()
        return 'default implementation'

class Delegate:
    def thing(self):
        return 'delegate implementation'

class TestDelegationPattern(unittest.TestCase):

    def test_no_delegate(self):
        # Test case where no delegate is set
        delegator = Delegator()
        self.assertEqual(delegator.operation(), 'default implementation')

    def test_delegate_without_thing(self):
        # Test case where delegate does not implement 'thing'
        delegator = Delegator()
        delegator.delegate = 'A delegate may be any object'
        self.assertEqual(delegator.operation(), 'default implementation')

    def test_delegate_with_thing(self):
        # Test case where delegate implements 'thing'
        delegator = Delegator()
        delegator.delegate = Delegate()
        self.assertEqual(delegator.operation(), 'delegate implementation')

if __name__ == '__main__':
    unittest.main()
