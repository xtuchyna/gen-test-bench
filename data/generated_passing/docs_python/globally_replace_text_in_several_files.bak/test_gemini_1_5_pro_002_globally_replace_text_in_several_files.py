import unittest
import fileinput
import os
import tempfile

class TestGlobalReplace(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.file_paths = []
        self.num_files = 3

        for i in range(self.num_files):
            file_path = os.path.join(self.temp_dir, f"file_{i}.txt")
            with open(file_path, "w") as f:
                if i == 0:
                    f.write("Goodbye London!\nThis is a test file.\nGoodbye London!") # Multiple occurrences in one file
                elif i == 1:
                    f.write("This file does not contain the target text.") # No occurrences
                else:
                    f.write("Another file with Goodbye London! at the end.\n") # Single occurrence


            self.file_paths.append(file_path)

    def tearDown(self):
        for file_path in self.file_paths:
            os.remove(file_path)
        os.rmdir(self.temp_dir)

    def test_replace_in_files(self):
        for line in fileinput.input(self.file_paths, inplace=True):
            print(line.replace('Goodbye London!', 'Hello New York!'), end='')


        for i in range(self.num_files):
            with open(self.file_paths[i], 'r') as f:
                content = f.read()
                if i == 0:
                    self.assertEqual(content, "Hello New York!\nThis is a test file.\nHello New York!")
                elif i == 1:
                    self.assertEqual(content, "This file does not contain the target text.")
                else:
                    self.assertEqual(content, "Another file with Hello New York! at the end.\n")

    def test_no_files_provided(self):
         # Test scenario where no files are provided.  Expect no changes and no errors.
        # fileinput.input will use stdin if no files are provided, but we are not writing to stdin in the test
        for line in fileinput.input(inplace=True): 
            print(line.replace('Goodbye London!', 'Hello New York!'), end='')



