import unittest
from dataclasses import dataclass

@dataclass
class Node:
    data: int
    next = None
    prev = None

class TestInsert(unittest.TestCase):

    def test_insert_empty_list(self):
        anchor = Node(0)
        anchor.next = anchor
        anchor.prev = anchor
        new_node = Node(1)
        insert(anchor, new_node)
        self.assertEqual(anchor.next, new_node)
        self.assertEqual(anchor.prev, new_node)
        self.assertEqual(new_node.next, anchor)
        self.assertEqual(new_node.prev, anchor)

    def test_insert_beginning_of_list(self):
        anchor = Node(0)
        node1 = Node(1)
        anchor.next = node1
        anchor.prev = node1
        node1.next = anchor
        node1.prev = anchor
        new_node = Node(2)
        insert(anchor, new_node)
        self.assertEqual(anchor.next, new_node)
        self.assertEqual(new_node.next, node1)
        self.assertEqual(node1.prev, new_node)
        self.assertEqual(new_node.prev, anchor)


    def test_insert_middle_of_list(self):
        anchor = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        anchor.next = node1
        node1.next = node2
        node2.next = anchor
        anchor.prev = node2
        node1.prev = anchor
        node2.prev = node1

        new_node = Node(3)
        insert(node1, new_node)

        self.assertEqual(node1.next, new_node)
        self.assertEqual(new_node.next, node2)
        self.assertEqual(node2.prev, new_node)
        self.assertEqual(new_node.prev, node1)



def insert(anchor, new):
    new.next = anchor.next
    new.prev = anchor
    anchor.next.prev = new
    anchor.next = new
