import unittest

class TestAssociativeArrayMerging(unittest.TestCase):

    def test_merge_associative_arrays(self):
        base = {"name": "Rocket Skates", "price": 12.75, "color": "yellow"}
        update = {"price": 15.25, "color": "red", "year": 1974}

        expected_result = {
            "name": "Rocket Skates",
            "price": 15.25,
            "color": "red",
            "year": 1974
        }

        result = {**base, **update}

        self.assertEqual(result, expected_result)

    def test_merge_associative_arrays_with_empty_update(self):
        base = {"name": "Rocket Skates", "price": 12.75, "color": "yellow"}
        update = {}

        expected_result = {
            "name": "Rocket Skates",
            "price": 12.75,
            "color": "yellow"
        }

        result = {**base, **update}

        self.assertEqual(result, expected_result)

    def test_merge_associative_arrays_with_empty_base(self):
        base = {}
        update = {"price": 15.25, "color": "red", "year": 1974}

        expected_result = {
            "price": 15.25,
            "color": "red",
            "year": 1974
        }

        result = {**base, **update}

        self.assertEqual(result, expected_result)

    def test_merge_associative_arrays_with_overlapping_keys(self):
        base = {"name": "Rocket Skates", "price": 12.75, "color": "yellow"}
        update = {"price": 15.25, "color": "red", "year": 1974}

        expected_result = {
            "name": "Rocket Skates",
            "price": 15.25,
            "color": "red",
            "year": 1974
        }

        result = {**base, **update}

        self.assertEqual(result, expected_result)

    def test_merge_associative_arrays_with_non_overlapping_keys(self):
        base = {"name": "Rocket Skates", "price": 12.75, "color": "yellow"}
        update = {"year": 1974}

        expected_result = {
            "name": "Rocket Skates",
            "price": 12.75,
            "color": "yellow",
            "year": 1974
        }

        result = {**base, **update}

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
