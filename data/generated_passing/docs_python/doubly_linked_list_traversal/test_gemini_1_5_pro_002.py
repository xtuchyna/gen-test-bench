import unittest

class List:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def append(self, data):
        if self.next == None:
            self.next = List(data, None, self)
            return self.next
        else:
            return self.next.append(data)


class TestDoublyLinkedListTraversal(unittest.TestCase):

    def test_forward_traversal(self):
        tail = head = List(10)
        for i in [20, 30, 40]:
            tail = tail.append(i)

        expected_data = [10, 20, 30, 40]
        actual_data = []
        node = head
        while node != None:
            actual_data.append(node.data)
            node = node.next

        self.assertEqual(actual_data, expected_data)


    def test_backward_traversal(self):
        tail = head = List(10)
        for i in [20, 30, 40]:
            tail = tail.append(i)
        
        expected_data = [40, 30, 20, 10]
        actual_data = []
        node = tail
        while node != None:
            actual_data.append(node.data)
            node = node.prev

        self.assertEqual(actual_data, expected_data)

    def test_single_element_list(self):
        head = tail = List(5)

        # Forward traversal
        expected_forward = [5]
        actual_forward = []
        node = head
        while node:
            actual_forward.append(node.data)
            node = node.next
        self.assertEqual(actual_forward, expected_forward)

        # Backward Traversal
        expected_backward = [5]
        actual_backward = []
        node = tail
        while node:
            actual_backward.append(node.data)
            node = node.prev
        self.assertEqual(actual_backward, expected_backward)



    def test_empty_list(self):
        head = None  # Represents an empty list
        tail = None

        # Test forward
        node = head
        actual_data_forward = []
        while node:
            actual_data_forward.append(node.data)
            node = node.next
        self.assertEqual(actual_data_forward, [])


        # Test backward
        node = tail
        actual_data_backward = []
        while node:
            actual_data_backward.append(node.data)
            node = node.prev

        self.assertEqual(actual_data_backward, [])



if __name__ == '__main__':
    unittest.main()

