import unittest

class Test100Doors(unittest.TestCase):
    def test_doors_states(self):
        doors = [False] * 100
        for i in range(100):
            for j in range(i, 100, i+1):
                doors[j] = not doors[j]
        
        # Only doors with perfect square indices should be open
        expected_open_doors = {i*i for i in range(1, 11)}  # 1, 4, 9, 16, ..., 100
        actual_open_doors = {index + 1 for index, state in enumerate(doors) if state}

        self.assertEqual(expected_open_doors, actual_open_doors)

    def test_all_doors_toggled(self):
        doors = [False] * 100
        for i in range(100):
            for j in range(i, 100, i+1):
                doors[j] = not doors[j]
        
        # Check that all doors have been toggled at least once
        toggled_doors = [False] * 100
        for i in range(100):
            for j in range(i, 100, i+1):
                toggled_doors[j] = True
        
        self.assertTrue(all(toggled_doors))

if __name__ == '__main__':
    unittest.main()
