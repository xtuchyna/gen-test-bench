import unittest
from unittest.mock import patch
from turtle import *

class TestDragonCurve(unittest.TestCase):

    @patch('turtle.forward')
    @patch('turtle.right')
    @patch('turtle.left')
    def test_dcr_base_case(self, mock_left, mock_right, mock_forward):
        dcr(0, 100)
        mock_right.assert_any_call_with(45)
        mock_forward.assert_any_call_with(100)
        mock_left.assert_any_call_with(90)
        mock_forward.assert_any_call_with(100)
        mock_right.assert_any_call_with(45)

    @patch('turtle.forward')
    @patch('turtle.right')
    @patch('turtle.left')
    def test_dcl_base_case(self, mock_left, mock_right, mock_forward):
        dcl(0, 100)
        mock_left.assert_any_call_with(45)
        mock_forward.assert_any_call_with(100)
        mock_right.assert_any_call_with(90)
        mock_forward.assert_any_call_with(100)
        mock_left.assert_any_call_with(45)


    @patch('turtle.forward')
    @patch('turtle.right')
    @patch('turtle.left')
    def test_dcr_recursive_case(self, mock_left, mock_right, mock_forward):
        dcr(2, 100)  # Testing a recursive case
        self.assertTrue(mock_right.called)
        self.assertTrue(mock_left.called)
        self.assertTrue(mock_forward.called)

    @patch('turtle.forward')
    @patch('turtle.right')
    @patch('turtle.left')
    def test_dcl_recursive_case(self, mock_left, mock_right, mock_forward):
        dcl(2, 100)  # Testing a recursive case
        self.assertTrue(mock_right.called)
        self.assertTrue(mock_left.called)
        self.assertTrue(mock_forward.called)


    @patch('turtle.forward')
    @patch('turtle.right')
    @patch('turtle.left')
    def test_dragon(self, mock_left, mock_right, mock_forward):
        dragon(3, 100) #test dragon function
        self.assertTrue(mock_right.called)
        self.assertTrue(mock_left.called)
        self.assertTrue(mock_forward.called)



