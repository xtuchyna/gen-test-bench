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

    def test_hash_join(self):
        table1 = [(27, "Jonah"),
                  (18, "Alan"),
                  (28, "Glory"),
                  (18, "Popeye"),
                  (28, "Alan")]
        table2 = [("Jonah", "Whales"),
                  ("Jonah", "Spiders"),
                  ("Alan", "Ghosts"),
                  ("Alan", "Zombies"),
                  ("Glory", "Buffy")]

        expected_output = [
            ((27, "Jonah"), ("Jonah", "Whales")),
            ((27, "Jonah"), ("Jonah", "Spiders")),
            ((18, "Alan"), ("Alan", "Ghosts")),
            ((18, "Alan"), ("Alan", "Zombies")),
            ((28, "Glory"), ("Glory", "Buffy")),
            ((28, "Alan"), ("Alan", "Ghosts")),
            ((28, "Alan"), ("Alan", "Zombies")),
        ]

        actual_output = hashJoin(table1, 1, table2, 0)
        self.assertEqual(sorted(actual_output), sorted(expected_output))  # order doesn't matter

    def test_empty_tables(self):
        self.assertEqual(hashJoin([], 0, [], 0), [])
        self.assertEqual(hashJoin([(1, "a")], 0, [], 0), [])
        self.assertEqual(hashJoin([], 0, [(1, "a")], 0), [])
        

    def test_no_match(self):
        table1 = [(1, "a"), (2, "b")]
        table2 = [(3, "c"), (4, "d")]
        self.assertEqual(hashJoin(table1, 1, table2, 0), [])


    def test_single_match(self):
        table1 = [(1, "a")]
        table2 = [("a", "x")]
        expected_output = [((1, "a"), ("a", "x"))]
        self.assertEqual(hashJoin(table1, 1, table2, 0), expected_output)

    def test_multiple_matches_on_same_key(self):
        table1 = [(1, "a"), (2, "a"), (3, "b")]
        table2 = [("a", "x"), ("a", "y"), ("b", "z")]

        expected_output = [
            ((1, "a"), ("a", "x")),
            ((1, "a"), ("a", "y")),
            ((2, "a"), ("a", "x")),
            ((2, "a"), ("a", "y")),
            ((3, "b"), ("b", "z"))
         ]
        actual_output = hashJoin(table1, 1, table2, 0)
        self.assertEqual(sorted(actual_output), sorted(expected_output))


if __name__ == "__main__":
    unittest.main()
