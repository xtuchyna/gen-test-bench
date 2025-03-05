import unittest
from collections import defaultdict

def hashJoin(table1, index1, table2, index2):
    h = defaultdict(list)
    # hash phase
    for s in table1:
        h[s[index1]].append(s)
    # join phase
    return [(s, r) for r in table2 for s in h[r[index2]]]

class TestHashJoin(unittest.TestCase):

    def setUp(self):
        self.table1 = [(27, "Jonah"),
                       (18, "Alan"),
                       (28, "Glory"),
                       (18, "Popeye"),
                       (28, "Alan")]
        self.table2 = [("Jonah", "Whales"),
                       ("Jonah", "Spiders"),
                       ("Alan", "Ghosts"),
                       ("Alan", "Zombies"),
                       ("Glory", "Buffy")]

    def test_hash_join(self):
        expected_output = [
            ((27, "Jonah"), ("Jonah", "Whales")),
            ((27, "Jonah"), ("Jonah", "Spiders")),
            ((18, "Alan"), ("Alan", "Ghosts")),
            ((18, "Alan"), ("Alan", "Zombies")),
            ((28, "Glory"), ("Glory", "Buffy")),
            ((28, "Alan"), ("Alan", "Ghosts")),
            ((28, "Alan"), ("Alan", "Zombies"))
        ]
        result = hashJoin(self.table1, 1, self.table2, 0)
        self.assertEqual(sorted(result), sorted(expected_output))

if __name__ == '__main__':
    unittest.main()
