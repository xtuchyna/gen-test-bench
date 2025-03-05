import unittest
import os
import shutil

class TestFileInputOutput(unittest.TestCase):

    def setUp(self):
        # Create a dummy input file
        with open("input.txt", "w") as f:
            f.write("This is a test file.\nWith multiple lines.")

    def tearDown(self):
        # Remove created files after each test
        try:
            os.remove("input.txt")
            os.remove("output.txt")
        except FileNotFoundError:
            pass


    def test_file_copy(self):
        # Test if the output file is created and contains the same content as the input file
        shutil.copyfile('input.txt', 'output.txt')
        self.assertTrue(os.path.exists("output.txt"))
        with open("input.txt", "r") as infile, open("output.txt", "r") as outfile:
            self.assertEqual(infile.read(), outfile.read())

    def test_missing_input(self):
        # Test handling when the input file is missing
        os.remove("input.txt")  # Remove the input file
        with self.assertRaises(FileNotFoundError):
            shutil.copyfile('input.txt', 'output.txt')



if __name__ == '__main__':
    unittest.main()
