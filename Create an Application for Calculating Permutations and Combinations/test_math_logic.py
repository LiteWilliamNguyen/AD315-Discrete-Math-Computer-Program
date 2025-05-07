import unittest
from math_logic import calculate_combination, calculate_permutation

class TestPermutationAndCombinationFunctions(unittest.TestCase):

    def test_permutation_normal(self):
        self.assertEqual(calculate_permutation(5, 3), 60)
        self.assertEqual(calculate_permutation(4, 2), 12)

    def test_combination_normal(self):
        self.assertEqual(calculate_combination(6, 2), 15)

    def test_permutation_large_number(self):
        result = calculate_permutation(100, 50)
        self.assertGreater(result, 0)  # Check if result is a positive number

    def test_combination_large_number(self):
        result = calculate_combination(100, 50)
        self.assertGreater(result, 0)  # Check if result is a positive number


    def test_permutation_edge_r_zero(self):
        self.assertEqual(calculate_permutation(5, 0), 1)

    def test_permutation_edge_r_equals_n(self):
        self.assertEqual(calculate_permutation(4, 4), 24)

    def test_permutation_edge_n_zero(self):
        with self.assertRaises(ValueError):
            calculate_permutation(0, 2)

if __name__ == '__main__':
    unittest.main()