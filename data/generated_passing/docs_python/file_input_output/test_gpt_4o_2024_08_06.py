import unittest
import os

class TestFileInputOutput(unittest.TestCase):

    def setUp(self):
        # Create a sample input file
        with open('input.txt', 'w') as f:
            f.write('This is a test content.')

    def tearDown(self):
        # Clean up files after tests
        if os.path.exists('input.txt'):
            os.remove('input.txt')
        if os.path.exists('output.txt'):
            os.remove('output.txt')

    def test_file_copy(self):
        # Read from input.txt into a variable
        with open('input.txt', 'r') as f:
            content = f.read()

        # Write the variable's contents into output.txt
        with open('output.txt', 'w') as f:
            f.write(content)

        # Verify that output.txt has the same content as input.txt
        with open('output.txt', 'r') as f:
            output_content = f.read()

        self.assertEqual(content, output_content)

    def test_output_file_creation(self):
        # Ensure output.txt is created
        with open('input.txt', 'r') as f:
            content = f.read()

        with open('output.txt', 'w') as f:
            f.write(content)

        self.assertTrue(os.path.exists('output.txt'))

    def test_content_integrity(self):
        # Ensure content integrity after copying
        with open('input.txt', 'r') as f:
            original_content = f.read()

        with open('output.txt', 'w') as f:
            f.write(original_content)

        with open('output.txt', 'r') as f:
            copied_content = f.read()

        self.assertEqual(original_content, copied_content)

if __name__ == '__main__':
    unittest.main()
