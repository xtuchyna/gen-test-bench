import unittest
import os
import fileinput

class TestCSVManipulation(unittest.TestCase):

    def setUp(self):
        self.csv_file = 'test_csv_data_manipulation.csv'
        with open(self.csv_file, 'w') as f:
            f.write("C1,C2,C3,C4,C5\n")
            f.write("1,5,9,13,17\n")
            f.write("2,6,10,14,18\n")
            f.write("3,7,11,15,19\n")
            f.write("4,8,12,16,20\n")

    def tearDown(self):
        os.remove(self.csv_file)

    def test_modify_cell(self):
        changerow, changecolumn, changevalue = 2, 4, '"Spam"'

        with fileinput.input(self.csv_file, inplace=True) as f:
            for line in f:
                if fileinput.filelineno() == changerow:
                    fields = line.rstrip().split(',')
                    fields[changecolumn - 1] = changevalue
                    line = ','.join(fields) + '\n'
                print(line, end='')

        with open(self.csv_file, 'r') as f:
            lines = f.readlines()
            self.assertEqual(lines[1], "1,5,9,13,17\n")
            self.assertEqual(lines[2-1], "1,5,9,\"Spam\",17\n") # Check modified line
            self.assertEqual(lines[3-1], "3,7,11,15,19\n")
            self.assertEqual(lines[4-1], "4,8,12,16,20\n")


    def test_first_row_unchanged(self):
          changerow, changecolumn, changevalue = 2, 4, '"Spam"'

          with fileinput.input(self.csv_file, inplace=True) as f:
              for line in f:
                  if fileinput.filelineno() == changerow:
                      fields = line.rstrip().split(',')
                      fields[changecolumn - 1] = changevalue
                      line = ','.join(fields) + '\n'
                  print(line, end='')
          with open(self.csv_file, 'r') as f:
              lines = f.readlines()
              self.assertEqual(lines[0], "C1,C2,C3,C4,C5\n")

    def test_last_row_unchanged_when_modifying_earlier_row(self):
          changerow, changecolumn, changevalue = 2, 4, '"Spam"'

          with fileinput.input(self.csv_file, inplace=True) as f:
              for line in f:
                  if fileinput.filelineno() == changerow:
                      fields = line.rstrip().split(',')
                      fields[changecolumn - 1] = changevalue
                      line = ','.join(fields) + '\n'
                  print(line, end='')
          with open(self.csv_file, 'r') as f:
              lines = f.readlines()
              self.assertEqual(lines[-1], "4,8,12,16,20\n")        
