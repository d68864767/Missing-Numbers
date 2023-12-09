import unittest
from missing_numbers import findMissingIDs

class TestFindMissingIDs(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(findMissingIDs(5, [2, 3, 4, 5]), [1])

    def test_no_missing_ids(self):
        self.assertEqual(findMissingIDs(5, [1, 2, 3, 4, 5]), [])

    def test_all_missing_ids(self):
        self.assertEqual(findMissingIDs(5, []), [1, 2, 3, 4, 5])

    def test_random_missing_ids(self):
        self.assertEqual(findMissingIDs(10, [1, 2, 4, 5, 7, 10]), [3, 6, 8, 9])

    def test_single_id(self):
        self.assertEqual(findMissingIDs(1, []), [1])
        self.assertEqual(findMissingIDs(1, [1]), [])

    def test_large_input(self):
        n = 10**5
        ids = [i for i in range(1, n) if i % 2 == 0]  # Even IDs exist
        expected_missing = [i for i in range(1, n + 1) if i % 2 != 0]  # Odd IDs are missing
        self.assertEqual(findMissingIDs(n, ids), expected_missing)

if __name__ == '__main__':
    unittest.main()
