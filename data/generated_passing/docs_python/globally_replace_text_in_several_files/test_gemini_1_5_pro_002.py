import unittest
import fileinput
import os
import tempfile

class TestGlobalReplace(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.file_names = ["file1.txt", "file2.txt", "file3.txt"]
        self.file_paths = []
        for file_name in self.file_names:
            file_path = os.path.join(self.temp_dir, file_name)
            self.file_paths.append(file_path)
            with open(file_path, "w") as f:
                f.write(f"Some text Goodbye London! More text\n")
                f.write(f"Another line with Goodbye London!\n")
                f.write("A line without the target text\n")

    def tearDown(self):
        for file_path in self.file_paths:
            os.remove(file_path)
        os.rmdir(self.temp_dir)


    def test_replace_in_multiple_files(self):
        for line in fileinput.input(self.file_paths, inplace=True):
            print(line.replace('Goodbye London!', 'Hello New York!'), end='')

        for file_path in self.file_paths:
            with open(file_path, "r") as f:
                content = f.read()
                self.assertIn("Hello New York!", content)
                self.assertNotIn("Goodbye London!", content)

    def test_no_target_text(self):
         # Create files without the target string
        file_paths_no_target = []
        for i in range(3):
            file_path = os.path.join(self.temp_dir, f"no_target_{i}.txt")
            file_paths_no_target.append(file_path)
            with open(file_path, "w") as f:
                f.write("Some other text\n")

        for line in fileinput.input(file_paths_no_target, inplace=True):
            print(line.replace('Goodbye London!', 'Hello New York!'), end='')

        for file_path in file_paths_no_target:
            with open(file_path, "r") as f:
                content = f.read()
                self.assertNotIn("Hello New York!", content)
                self.assertNotIn("Goodbye London!", content)

        # Clean up files without target string.
        for file_path in file_paths_no_target:
             os.remove(file_path)


    def test_empty_files(self):
        # Create empty files
        file_paths_empty = []
        for i in range(3):
            file_path = os.path.join(self.temp_dir, f"empty_{i}.txt")
            file_paths_empty.append(file_path)
            with open(file_path, "w") as f:
                pass  # Keep files empty


        for line in fileinput.input(file_paths_empty, inplace=True):
            print(line.replace('Goodbye London!', 'Hello New York!'), end='')


        for file_path in file_paths_empty:
            with open(file_path, "r") as f:
                content = f.read()
                self.assertEqual(content, "")  # Expect empty content

        # Clean up empty files.
        for file_path in file_paths_empty:
            os.remove(file_path)
