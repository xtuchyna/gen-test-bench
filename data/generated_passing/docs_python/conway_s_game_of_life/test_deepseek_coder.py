import unittest
from collections import defaultdict

class TestConwayGameOfLife(unittest.TestCase):

    def setUp(self):
        self.celltable = defaultdict(int, {
            (1, 2): 1,
            (1, 3): 1,
            (0, 3): 1,
        })
        self.cellcount = (3, 3)
        self.maxgenerations = 3

    def test_blinker_pattern(self):
        # Initial state of the blinker pattern
        universe = defaultdict(int)
        universe[(1, 0)], universe[(1, 1)], universe[(1, 2)] = 1, 1, 1

        expected_states = [
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

        for generation in range(self.maxgenerations):
            # Check the current state of the universe
            current_state = [[universe[(row, col)] for col in range(self.cellcount[0])] for row in range(self.cellcount[1])]
            self.assertEqual(current_state, expected_states[generation])

            # Compute the next generation
            nextgeneration = defaultdict(int)
            for row in range(self.cellcount[1]):
                for col in range(self.cellcount[0]):
                    nextgeneration[(row, col)] = self.celltable[
                        (universe[(row, col)],
                         -universe[(row, col)] + sum(universe[(r, c)]
                                                     for r in range(row - 1, row + 2)
                                                     for c in range(col - 1, col + 2))
                         )]
            universe = nextgeneration

if __name__ == '__main__':
    unittest.main()
