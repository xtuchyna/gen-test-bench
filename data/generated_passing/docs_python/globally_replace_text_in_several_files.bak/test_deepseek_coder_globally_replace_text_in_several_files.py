import unittest
import tempfile
import os
import fileinput

class TestGlobalReplaceTextInFiles(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory to store test files
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_files = [
            os.path.join(self.temp_dir.name, 'file1.txt'),
            os.path.join(self.temp_dir.name, 'file2.txt')
        ]

        # Create test files with initial content
        with open(self.test_files[0], 'w') as f:
            f.write("Goodbye London!\nHello World!\nGoodbye London!")
        with open(self.test_files[1], 'w') as f:
            f.write("Goodbye London!\nGoodbye London!\nHello World!")

    def tearDown(self):
        # Clean up the temporary directory
        self.temp_dir.cleanup()

    def test_replace_text_in_files(self):
        # Run the code to replace text in files
        with fileinput.input(files=self.test_files, inplace=True) as file:
            for line in file:
                print(line.replace('Goodbye London!', 'Hello New York!'), end='')

        # Verify the content of the files after replacement
        with open(self.test_files[0], 'r') as f:
            content1 = f.read()
        with open(self.test_files[1], 'r') as f:
            content2 = f.read()

        expected_content1 = "Hello New York!\nHello World!\nHello New York!"
        expected_content2 = "Hello New York!\nHello New York!\nHello World!"

        self.assertEqual(content1, expected_content1)
        self.assertEqual(content2, expected_content2)

if __name__ == '__main__':
    unittest.main()
