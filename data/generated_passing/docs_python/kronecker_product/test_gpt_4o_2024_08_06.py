import unittest

def kronecker(matrix1, matrix2):
    final_list = []
    sub_list = []
    count = len(matrix2)
    for elem1 in matrix1:
        counter = 0
        check = 0
        while check < count:
            for num1 in elem1:
                for num2 in matrix2[counter]:
                    sub_list.append(num1 * num2)
            counter += 1
            final_list.append(sub_list)
            sub_list = []
            check += 1
    return final_list

class TestKroneckerProduct(unittest.TestCase):

    def test_sample1(self):
        a1 = [[1, 2], [3, 4]]
        b1 = [[0, 5], [6, 7]]
        expected_result1 = [
            [0, 5, 0, 10],
            [6, 7, 12, 14],
            [0, 15, 0, 20],
            [18, 21, 24, 28]
        ]
        result1 = kronecker(a1, b1)
        self.assertEqual(result1, expected_result1)

    def test_sample2(self):
        a2 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        b2 = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
        expected_result2 = [
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
        ]
        result2 = kronecker(a2, b2)
        self.assertEqual(result2, expected_result2)

if __name__ == '__main__':
    unittest.main()
