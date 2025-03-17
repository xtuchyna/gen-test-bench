import unittest
from collections import defaultdict

class TestConwaysGameOfLife(unittest.TestCase):
    def setUp(self):
        self.printdead, self.printlive = '-#'
        self.maxgenerations = 3
        self.cellcount = 3, 3
        self.celltable = defaultdict(int, {
            (1, 2): 1,
            (1, 3): 1,
            (0, 3): 1,
        })

    def test_blinker(self):
        # Initial blinker state
        universe = defaultdict(int)
        universe[(1, 0)], universe[(1, 1)], universe[(1, 2)] = 1, 1, 1

        expected_generations = [
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 0]
            ]
        ]

        for i in range(self.maxgenerations):
            current_state = [[universe[(row, col)] for col in range(self.cellcount[0])] for row in range(self.cellcount[1])]
            self.assertEqual(current_state, expected_generations[i], f"Generation {i} failed")

            nextgeneration = defaultdict(int)
            for row in range(self.cellcount[1]):
                for col in range(self.cellcount[0]):
                    nextgeneration[(row, col)] = self.celltable[
                        (universe[(row, col)],
                         -universe[(row, col)] + sum(universe[(r, c)]
                                                     for r in range(row - 1, row + 2)
                                                     for c in range(col - 1, col + 2)))
                    ]
            universe = nextgeneration

if __name__ == '__main__':
    unittest.main()
