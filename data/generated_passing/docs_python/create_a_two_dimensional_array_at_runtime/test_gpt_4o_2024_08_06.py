import unittest
from unittest.mock import patch
import builtins

class TestCreateTwoDimensionalArray(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '2'])
    def test_array_creation_and_access(self, mock_input):
        # Redirect the input function to simulate user input
        width = int(input("Width of myarray: "))
        height = int(input("Height of Array: "))
        
        # Create the array
        myarray = [[0] * width for _ in range(height)]
        
        # Write to the array
        myarray[0][0] = 3.5
        
        # Check if the element is correctly written
        self.assertEqual(myarray[0][0], 3.5)
        
        # Check the dimensions of the array
        self.assertEqual(len(myarray), height)
        self.assertEqual(len(myarray[0]), width)

    @patch('builtins.input', side_effect=['0', '0'])
    def test_zero_dimensions(self, mock_input):
        # Redirect the input function to simulate user input
        width = int(input("Width of myarray: "))
        height = int(input("Height of Array: "))
        
        # Create the array
        myarray = [[0] * width for _ in range(height)]
        
        # Check if the array is empty
        self.assertEqual(len(myarray), 0)

    @patch('builtins.input', side_effect=['5', '0'])
    def test_zero_height(self, mock_input):
        # Redirect the input function to simulate user input
        width = int(input("Width of myarray: "))
        height = int(input("Height of Array: "))
        
        # Create the array
        myarray = [[0] * width for _ in range(height)]
        
        # Check if the array is empty
        self.assertEqual(len(myarray), 0)

    @patch('builtins.input', side_effect=['0', '5'])
    def test_zero_width(self, mock_input):
        # Redirect the input function to simulate user input
        width = int(input("Width of myarray: "))
        height = int(input("Height of Array: "))
        
        # Create the array
        myarray = [[0] * width for _ in range(height)]
        
        # Check if the array has correct height and zero width
        self.assertEqual(len(myarray), height)
        self.assertTrue(all(len(row) == 0 for row in myarray))

if __name__ == '__main__':
    unittest.main()
